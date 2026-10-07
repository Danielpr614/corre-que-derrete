"""Técnicas visuais e ciclo dos efeitos; execução sem desktop com SDL dummy."""

import os
import unittest
from dataclasses import asdict

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")
os.environ.setdefault("PYGAME_HIDE_SUPPORT_PROMPT", "1")

import pygame

from game import settings as S
from game.animation import CourierAnimation
from game.app import App
from game.entities import WorldObject
from game.graphics import Renderer
from game.parallax import Parallax, layer_offset
from game.particles import Effects
from game.run import Run


class TechniqueTests(unittest.TestCase):
    def test_parallax_factors_and_wrapping(self):
        background = Parallax()
        self.assertEqual([factor for _, factor in background.layers], [.15, .35, .7])
        offsets = [layer_offset(100, factor, tile.get_width())
                   for tile, factor in background.layers]
        self.assertEqual(offsets, [15, 35, 70])
        for tile, factor in background.layers:
            self.assertAlmostEqual(layer_offset(tile.get_width() / factor, factor,
                                                tile.get_width()), 0)

    def test_running_frames_are_distinct_and_time_selected(self):
        animation = CourierAnimation()
        run = Run()
        images = [pygame.image.tobytes(frame, "RGBA") for frame in animation.running]
        self.assertEqual(len(set(images)), 6)
        self.assertEqual(animation.frame_index(run.player, .05), ("running", 0))
        self.assertEqual(animation.frame_index(run.player, .15), ("running", 1))
        self.assertEqual(animation.frame_index(run.player, .65), ("running", 0))

    def test_jump_has_rise_and_fall_frames_without_altering_hitbox(self):
        animation = CourierAnimation()
        run = Run()
        run.jump()
        before = run.player.rect(0)
        self.assertEqual(animation.frame_index(run.player, 0), ("jumping", 0))
        self.assertEqual(run.player.rect(0), before)
        run.player.velocity_y = 100
        self.assertEqual(animation.frame_index(run.player, 0), ("jumping", 1))
        self.assertNotEqual(pygame.image.tobytes(animation.jumping[0], "RGBA"),
                            pygame.image.tobytes(animation.jumping[1], "RGBA"))

    def test_particle_lifetime_motion_and_capacity(self):
        effects = Effects()
        effects.emit("ice", 200, 300, 150)
        self.assertEqual(len(effects.particles), effects.LIMIT)
        initial = asdict(effects.particles[0])
        effects.update(.1, False, 0, 0)
        self.assertNotEqual(effects.particles[0].y, initial["y"])
        self.assertLess(effects.particles[0].remaining, initial["remaining"])
        effects.update(1, False, 0, 0)
        self.assertEqual(effects.particles, [])

    def test_low_conservation_emits_drops_and_stops_when_recovered(self):
        effects = Effects()
        effects.update(.13, True, 255, 300)
        self.assertEqual(len(effects.particles), 2)
        self.assertTrue(all(p.kind == "melt" for p in effects.particles))
        effects.update(1, False, 0, 0)
        self.assertEqual(effects.particles, [])
        self.assertEqual(effects.melt_timer, 0)

    def test_ice_and_real_damage_emit_different_effects(self):
        for kind, expected in (("ice", "ice"), ("box", "impact")):
            run = Run()
            run.objects = [WorldObject(kind, S.PLAYER_SCREEN_X + 10,
                                       S.GROUND_Y - 32, 32, 32)]
            run.update(S.FIXED_STEP)
            self.assertTrue(run.effects.particles)
            self.assertEqual(run.effects.flash_kind, expected)
            self.assertTrue(all(p.kind == expected for p in run.effects.particles))
        run.objects.append(WorldObject("box", run.distance + S.PLAYER_SCREEN_X + 10,
                                       S.GROUND_Y - 32, 32, 32))
        count = len(run.effects.particles)
        run.update(S.FIXED_STEP)
        self.assertEqual(len(run.effects.particles), count)

    def test_simultaneous_bursts_keep_damage_feedback_and_both_shapes(self):
        effects = Effects()
        effects.burst("impact", 200, 300)
        effects.burst("ice", 200, 300)
        self.assertEqual(effects.flash_kind, "impact")
        self.assertEqual({p.kind for p in effects.particles}, {"impact", "ice"})
        effects.update(1, False, 0, 0)
        self.assertEqual(effects.flash_time, 0)

    def test_pause_freezes_effects_and_restart_discards_them(self):
        app = App()
        app.start()
        app.run.conservation = 20
        app.run.jump()
        app.run.effects.burst("ice", 250, 300)
        app.update(.13)
        app.set_state("paused")
        particles = [asdict(p) for p in app.run.effects.particles]
        elapsed, flash = app.run.elapsed, app.run.effects.flash_time
        for _ in range(60):
            app.update(1)
        self.assertEqual(particles, [asdict(p) for p in app.run.effects.particles])
        self.assertEqual((elapsed, flash), (app.run.elapsed, app.run.effects.flash_time))
        app.start()
        self.assertEqual(app.run.effects.particles, [])
        self.assertEqual(app.run.effects.flash_time, 0)

    def test_particle_randomness_does_not_change_game_rules(self):
        first, second = Run(), Run()
        for index in range(90):
            if index % 10 == 0:
                first.effects.burst("ice", 200, 300)
            first.update(S.FIXED_STEP)
            second.update(S.FIXED_STEP)
        self.assertEqual((first.distance, first.conservation, first.score, first.hits),
                         (second.distance, second.conservation, second.score, second.hits))

    def test_arrival_feedback_and_animated_scene_render(self):
        pygame.display.init()
        pygame.font.init()
        try:
            screen = pygame.display.set_mode((S.WIDTH, S.HEIGHT))
            renderer = Renderer(screen)
            app = App()
            app.start()
            # Duas poses aéreas, efeitos e conservação baixa.
            app.run.jump()
            app.run.conservation = 20
            app.update(.15)
            app.run.effects.burst("ice", 255, 320)
            app.run.effects.burst("impact", 225, 355)
            for velocity in (-100, 100):
                app.run.player.velocity_y = velocity
                renderer.draw(app)
            app.run.notice_time = 0
            renderer.draw(app)
            self.assertTrue(any("Conservação baixa" in message
                                for message, _ in renderer.text_rects))
            app.run.distance = S.ROUTE_LENGTH - 300
            renderer.draw(app)
            self.assertTrue(any(message == "CLIENTE" for message, _ in renderer.text_rects))
            app.run.distance = S.ROUTE_LENGTH
            app.run.result = "victory"
            app.set_state("result")
            renderer.draw(app)
            self.assertTrue(any(message == "Sorvete entregue!"
                                for message, _ in renderer.text_rects))
            app.run.result = "defeat"
            renderer.draw(app)
            self.assertFalse(any(message == "Sorvete entregue!"
                                 for message, _ in renderer.text_rects))
        finally:
            pygame.quit()


if __name__ == "__main__":
    unittest.main()
