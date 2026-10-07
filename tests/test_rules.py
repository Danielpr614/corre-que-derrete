"""Regras e estados usando SDL dummy: sem validação visual humana."""

import os
import unittest

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")
os.environ.setdefault("PYGAME_HIDE_SUPPORT_PROMPT", "1")

import pygame

from game import settings as S
from game.app import App
from game.entities import WorldObject, build_route
from game.graphics import Renderer
from game.run import Run


def press(app, key):
    app.handle_event(pygame.event.Event(pygame.KEYDOWN, key=key))


def contact_object(run, kind):
    # Posicionar um objeto na frente do jogador para o próximo passo.
    return WorldObject(kind, run.distance + S.PLAYER_SCREEN_X + 10,
                       S.GROUND_Y - 32, 32, 32)


class RuleTests(unittest.TestCase):
    def test_auto_run_melts_and_scores(self):
        run = Run()
        run.objects = []
        for _ in range(60):
            run.update(S.FIXED_STEP)
        self.assertAlmostEqual(run.distance, 260)
        self.assertAlmostEqual(run.conservation, 98)
        self.assertEqual(run.score, 26)

    def test_jump_no_double_jump_and_landing(self):
        run = Run()
        initial_y = run.player.y
        self.assertTrue(run.jump())
        self.assertFalse(run.jump())
        run.update(S.FIXED_STEP)
        self.assertLess(run.player.y, initial_y)
        for _ in range(90):
            run.update(S.FIXED_STEP)
        self.assertEqual(run.player.y, initial_y)
        self.assertTrue(run.player.grounded)
        self.assertEqual(run.player.velocity_y, 0)
        self.assertTrue(run.jump())

    def test_each_obstacle_damages_once(self):
        for kind in ("cone", "box"):
            with self.subTest(kind=kind):
                run = Run()
                run.objects = [contact_object(run, kind)]
                run.update(S.FIXED_STEP)
                self.assertAlmostEqual(run.conservation, 80 - S.MELT_RATE * S.FIXED_STEP)
                self.assertEqual(run.hits, 1)
                for _ in range(120):
                    run.update(S.FIXED_STEP)
                self.assertEqual(run.hits, 1)

    def test_invulnerability_prevents_overlapping_damage(self):
        run = Run()
        run.objects = [contact_object(run, "cone"), contact_object(run, "box")]
        run.update(S.FIXED_STEP)
        self.assertEqual(run.hits, 1)
        run.objects.append(contact_object(run, "box"))
        run.update(S.FIXED_STEP)
        self.assertEqual(run.hits, 1)
        for _ in range(60):
            run.update(S.FIXED_STEP)
        run.objects.append(contact_object(run, "box"))
        run.update(S.FIXED_STEP)
        self.assertEqual(run.hits, 2)

    def test_jump_avoids_ground_obstacle(self):
        run = Run()
        run.objects = [WorldObject("box", S.PLAYER_SCREEN_X + 105,
                                   S.GROUND_Y - 58, 50, 58)]
        run.jump()
        for _ in range(45):
            run.update(S.FIXED_STEP)
        self.assertEqual(run.hits, 0)

    def test_ice_recovers_once_and_scores(self):
        run = Run()
        run.conservation = 50
        run.objects = [contact_object(run, "ice")]
        run.update(S.FIXED_STEP)
        self.assertAlmostEqual(run.conservation, 65 - S.MELT_RATE * S.FIXED_STEP)
        self.assertEqual(run.ices, 1)
        self.assertEqual(run.score, S.ICE_SCORE)
        for _ in range(5):
            run.update(S.FIXED_STEP)
        self.assertEqual(run.ices, 1)

    def test_ice_caps_at_100(self):
        run = Run()
        run.objects = [contact_object(run, "ice")]
        run.update(S.FIXED_STEP)
        self.assertEqual(run.conservation, 100)

    def test_collision_is_spatial(self):
        run = Run()
        obj = contact_object(run, "ice")
        obj.y = 0
        run.objects = [obj]
        run.update(S.FIXED_STEP)
        self.assertEqual(run.ices, 0)

    def test_stage_boundaries_and_speeds(self):
        run = Run()
        for distance, stage, speed in ((5999, 0, 260), (6000, 1, 300),
                                       (11999, 1, 300), (12000, 2, 340),
                                       (18000, 2, 340)):
            run.distance = distance
            self.assertEqual(run.stage, stage)
            self.assertEqual(run.speed, speed)
        route = build_route()
        stages = [[obj for obj in route if obj.kind != "ice" and
                   stage * 6000 <= obj.x - S.PLAYER_SCREEN_X < (stage + 1) * 6000]
                  for stage in range(3)]
        spacings = [objects[1].x - objects[0].x for objects in stages]
        self.assertEqual(spacings, [1200, 950, 650])

    def test_victory_at_destination(self):
        run = Run()
        run.objects = []
        run.distance = S.ROUTE_LENGTH - 1
        run.update(S.FIXED_STEP)
        self.assertEqual(run.result, "victory")
        self.assertEqual(run.distance, S.ROUTE_LENGTH)

    def test_defeat_clamps_at_zero(self):
        run = Run()
        run.objects = []
        run.conservation = .01
        run.update(S.FIXED_STEP)
        self.assertEqual(run.result, "defeat")
        self.assertEqual(run.conservation, 0)

    def test_defeat_has_priority_at_destination(self):
        run = Run()
        run.objects = []
        run.distance = S.ROUTE_LENGTH - 1
        run.conservation = .01
        run.update(S.FIXED_STEP)
        self.assertEqual(run.result, "defeat")

    def test_same_step_ice_can_save_delivery(self):
        run = Run()
        run.distance = S.ROUTE_LENGTH - 1
        run.conservation = .01
        run.objects = [contact_object(run, "ice")]
        run.update(S.FIXED_STEP)
        self.assertEqual(run.result, "victory")
        self.assertGreater(run.conservation, 0)

    def test_impact_before_ice_in_same_step(self):
        run = Run()
        run.conservation = 10
        # Inverter a lista não deve inverter a prioridade das regras.
        run.objects = [contact_object(run, "ice"), contact_object(run, "box")]
        run.update(S.FIXED_STEP)
        self.assertAlmostEqual(run.conservation, 5 - S.MELT_RATE * S.FIXED_STEP)
        self.assertIsNone(run.result)

    def test_result_freezes_simulation(self):
        run = Run()
        run.result = "defeat"
        before = (run.distance, run.conservation, run.elapsed)
        run.update(1)
        self.assertEqual(before, (run.distance, run.conservation, run.elapsed))
        self.assertFalse(run.jump())

    def test_no_input_loses_on_real_route(self):
        run = Run()
        for _ in range(5000):
            run.update(S.FIXED_STEP)
            if run.result:
                break
        self.assertEqual(run.result, "defeat")
        self.assertGreater(run.hits, 0)

    def test_real_route_has_winning_scripted_path(self):
        # Agente determinístico vê dados da rota: prova possibilidade lógica,
        # não facilidade, reação humana ou equilíbrio da jogabilidade.
        run = Run()
        for _ in range(5000):
            player_x = run.distance + S.PLAYER_SCREEN_X
            targets = [obj for obj in run.objects if not obj.consumed and
                       obj.x + obj.width >= player_x and
                       (obj.kind != "ice" or obj.y < S.GROUND_Y - 80)]
            if targets and run.player.grounded:
                ahead = min(targets, key=lambda obj: obj.x)
                if 0 < ahead.x - player_x <= run.speed * .33:
                    run.jump()
            run.update(S.FIXED_STEP)
            if run.result:
                break
        self.assertEqual(run.result, "victory")
        self.assertEqual(run.hits, 0)
        self.assertEqual(run.ices, 6)


class StateTests(unittest.TestCase):
    def test_menu_instructions_and_exit(self):
        app = App()
        press(app, pygame.K_DOWN)
        press(app, pygame.K_RETURN)
        self.assertEqual(app.state, "instructions")
        press(app, pygame.K_ESCAPE)
        self.assertEqual(app.state, "menu")
        press(app, pygame.K_ESCAPE)
        self.assertFalse(app.running)

    def test_both_jump_keys(self):
        for key in (pygame.K_SPACE, pygame.K_UP):
            app = App()
            press(app, pygame.K_RETURN)
            press(app, key)
            self.assertFalse(app.run.player.grounded)

    def test_pause_freezes_all_timers_and_resume(self):
        app = App()
        app.start()
        app.run.invulnerable = .5
        press(app, pygame.K_SPACE)
        app.update(.1)
        press(app, pygame.K_p)
        before = vars(app.run).copy()
        player_before = vars(app.run.player).copy()
        for _ in range(60):
            app.update(1)
        self.assertEqual(vars(app.run), before)
        self.assertEqual(vars(app.run.player), player_before)
        press(app, pygame.K_ESCAPE)
        app.update(S.FIXED_STEP)
        self.assertGreater(app.run.distance, before["distance"])

    def test_result_then_restart_restores_run(self):
        app = App()
        app.start()
        for _ in range(3):
            old_run = app.run
            app.run.objects[0].consumed = True
            app.run.ices = 3
            app.run.hits = 2
            app.run.conservation = .01
            app.update(S.FIXED_STEP)
            self.assertEqual(app.state, "result")
            press(app, pygame.K_RETURN)
            self.assertEqual(app.state, "playing")
            self.assertIsNot(app.run, old_run)
            self.assertEqual(app.run.conservation, 100)
            self.assertEqual(app.run.distance, 0)
            self.assertEqual(app.run.ices, 0)
            self.assertEqual(app.run.hits, 0)
            self.assertTrue(app.run.player.grounded)
            self.assertTrue(all(not obj.consumed for obj in app.run.objects))

    def test_menu_from_pause_and_result(self):
        for state in ("paused", "result"):
            app = App()
            app.set_state(state)
            press(app, pygame.K_m)
            self.assertEqual(app.state, "menu")

    def test_exit_option_and_window_close_every_state(self):
        for state in ("menu", "paused", "result"):
            app = App()
            app.set_state(state)
            app.selection = 2
            press(app, pygame.K_RETURN)
            self.assertFalse(app.running)
        for state in ("menu", "instructions", "playing", "paused", "result"):
            app = App()
            app.set_state(state)
            app.handle_event(pygame.event.Event(pygame.QUIT))
            self.assertFalse(app.running)

    def test_time_based_movement_at_different_frame_rates(self):
        results = []
        for fps in (30, 60, 144):
            app = App()
            app.start()
            app.run.objects = []
            for _ in range(fps * 10):
                app.update(1 / fps)
            results.append((app.run.distance, app.run.conservation, app.run.elapsed))
        for actual in results:
            self.assertAlmostEqual(actual[0], 2600)
            self.assertAlmostEqual(actual[1], 80)
            self.assertAlmostEqual(actual[2], 10)

    def test_long_frame_is_limited(self):
        app = App()
        app.start()
        app.update(20)
        self.assertAlmostEqual(app.run.elapsed, S.MAX_FRAME_TIME)

    def test_repeated_key_event_is_ignored(self):
        app = App()
        app.start()
        app.handle_event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_p, repeat=True))
        self.assertEqual(app.state, "playing")


class RenderingSmokeTests(unittest.TestCase):
    def test_all_screens_render_with_dummy_driver(self):
        pygame.display.init()
        pygame.font.init()
        try:
            screen = pygame.display.set_mode((S.WIDTH, S.HEIGHT))
            renderer = Renderer(screen)
            app = App()
            for state in ("menu", "instructions", "playing", "paused", "result"):
                app.set_state(state)
                for result in ("victory", "defeat"):
                    app.run.result = result
                    renderer.draw(app)
                    pygame.display.flip()
            # Percorrer a rota cobre os desenhos de gelo, caixa, cone e destino.
            app.set_state("playing")
            for distance in (1000, 4300, 7000, 12300, 17990):
                app.run.distance = distance
                renderer.draw(app)
            app.run.conservation = 1
            app.run.invulnerable = .5
            app.run.notice_time = 0
            renderer.draw(app)
        finally:
            pygame.quit()


if __name__ == "__main__":
    unittest.main()
