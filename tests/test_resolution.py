"""Renderização nativa e independência da simulação em Full HD."""

import os
import unittest
from unittest.mock import patch

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")
os.environ.setdefault("PYGAME_HIDE_SUPPORT_PROMPT", "1")

import pygame

from game.app import App
from game.graphics import Renderer
from game.window import Window, viewport_rect


class NativeResolutionTests(unittest.TestCase):
    def setUp(self):
        pygame.display.init()
        pygame.font.init()

    def tearDown(self):
        pygame.quit()

    def test_full_hd_fonts_frames_and_layers_have_native_detail(self):
        renderer = Renderer(pygame.Surface((960, 540)))
        small_font_height = renderer.small.get_height()
        renderer.resize(pygame.Surface((1920, 1080)))
        self.assertGreater(renderer.small.get_height(), small_font_height * 1.8)
        self.assertEqual(renderer.courier.running[0].get_size(), (164, 176))
        self.assertEqual(renderer.background.layers[0][0].get_size(), (1400, 1080))
        self.assertEqual(renderer.effect_layer.get_size(), (1920, 1080))
        app = App()
        renderer.draw(app)
        title = next(rect for message, rect in renderer.physical_text_rects
                     if message == "CORRE QUE DERRETE!")
        self.assertEqual(title.centerx, 960)
        self.assertGreater(title.height, 70)

    def test_present_copies_native_image_without_resampling(self):
        window = Window()
        window.screen = pygame.display.set_mode((1920, 1080), pygame.RESIZABLE)
        canvas = window.prepare_frame()
        self.assertEqual(canvas.get_size(), (1920, 1080))
        canvas.fill((100, 110, 120))
        # Uma linha de um pixel não pode ser duplicada ou interpolada.
        pygame.draw.line(canvas, (250, 30, 40), (25, 0), (25, 1079), 1)
        with patch("pygame.transform.smoothscale", side_effect=AssertionError("ampliação indevida")), \
             patch("pygame.transform.scale", side_effect=AssertionError("ampliação indevida")):
            window.present()
        self.assertEqual(window.screen.get_at((25, 500))[:3], (250, 30, 40))
        self.assertEqual(window.screen.get_at((26, 500))[:3], (100, 110, 120))

    def test_resource_cache_reused_then_regenerated_after_resize(self):
        renderer = Renderer(pygame.Surface((960, 540)))
        original = (renderer.background, renderer.courier, renderer.font)
        renderer.resize(pygame.Surface((960, 540)))
        self.assertEqual(original, (renderer.background, renderer.courier, renderer.font))
        renderer.resize(pygame.Surface((1920, 1080)))
        self.assertIsNot(original[0], renderer.background)
        self.assertIsNot(original[1], renderer.courier)
        self.assertIsNot(original[2], renderer.font)

    def test_rendering_and_resizing_do_not_mutate_rules_or_effects(self):
        window = Window()
        renderer = Renderer(window.canvas)
        app = App()
        app.start()
        app.run.jump()
        app.run.effects.burst("ice", 230, 330)
        app.update(.1)
        before = (app.run.distance, app.run.conservation, app.run.player.y,
                  app.run.player.velocity_y, app.run.score, app.run.elapsed,
                  [(p.x, p.y, p.remaining) for p in app.run.effects.particles])
        for size in ((1920, 1080), (800, 600), (600, 900), (960, 540)):
            window.screen = pygame.display.set_mode(size, pygame.RESIZABLE)
            renderer.resize(window.prepare_frame())
            renderer.draw(app)
            window.present()
            self.assertEqual(window.canvas.get_size(), viewport_rect(size).size)
            after = (app.run.distance, app.run.conservation, app.run.player.y,
                     app.run.player.velocity_y, app.run.score, app.run.elapsed,
                     [(p.x, p.y, p.remaining) for p in app.run.effects.particles])
            self.assertEqual(before, after)


if __name__ == "__main__":
    unittest.main()
