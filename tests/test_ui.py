"""Geometria, textos e modos de janela com SDL dummy; sem desktop real."""

import os
import unittest

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")
os.environ.setdefault("PYGAME_HIDE_SUPPORT_PROMPT", "1")

import pygame

from game.app import App
from game.graphics import Renderer, format_conservation
from game.window import Window, viewport_rect


SIZES = ((320, 240), (640, 360), (960, 540), (1280, 720),
         (1366, 768), (1920, 1080), (800, 600), (600, 900))


class ViewportTests(unittest.TestCase):
    def test_proportion_centering_and_no_crop(self):
        for size in SIZES:
            with self.subTest(size=size):
                viewport = viewport_rect(size)
                bounds = pygame.Rect((0, 0), size)
                self.assertTrue(bounds.contains(viewport))
                self.assertEqual(viewport.width * 9, viewport.height * 16)
                self.assertEqual(viewport.center, bounds.center)
                self.assertLess(min(size[0] - viewport.width,
                                    size[1] - viewport.height), 16)

    def test_tiny_window_does_not_produce_negative_dimensions(self):
        for size in ((0, 0), (1, 1), (15, 8)):
            self.assertEqual(viewport_rect(size).size, (0, 0))

    def test_brazilian_conservation_precision(self):
        self.assertEqual(format_conservation(18.5), "18,5%")
        self.assertEqual(format_conservation(0), "0,0%")
        self.assertEqual(format_conservation(100), "100,0%")


class WindowTests(unittest.TestCase):
    def setUp(self):
        pygame.display.init()
        pygame.font.init()

    def tearDown(self):
        pygame.quit()

    def test_f11_restores_window_size_without_changing_run(self):
        window = Window()
        window.screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
        window.handle_event(pygame.event.Event(pygame.WINDOWSIZECHANGED, x=800, y=600))
        app = App()
        app.start()
        app.run.jump()
        app.update(.1)
        before = (app.run.distance, app.run.conservation, app.run.player.rect(app.run.distance),
                  app.run.player.velocity_y, app.accumulator)
        for _ in range(2):
            self.assertTrue(window.handle_event(
                pygame.event.Event(pygame.KEYDOWN, key=pygame.K_F11)))
            window.present()
        self.assertFalse(window.fullscreen)
        self.assertEqual(window.screen.get_size(), (800, 600))
        self.assertEqual(window.canvas.get_size(), (800, 450))
        after = (app.run.distance, app.run.conservation, app.run.player.rect(app.run.distance),
                 app.run.player.velocity_y, app.accumulator)
        self.assertEqual(before, after)

    def test_repeated_f11_does_not_toggle(self):
        window = Window()
        window.handle_event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_F11, repeat=True))
        self.assertFalse(window.fullscreen)

    def test_screens_and_text_bounds_at_all_sizes(self):
        window = Window()
        renderer = Renderer(window.canvas)
        app = App()
        cases = (("menu", None), ("instructions", None), ("playing", None),
                 ("paused", None), ("result", "victory"), ("result", "defeat"))
        for size in SIZES:
            window.screen = pygame.display.set_mode(size, pygame.RESIZABLE)
            window.handle_event(pygame.event.Event(pygame.VIDEORESIZE, size=size))
            renderer.resize(window.prepare_frame())
            for state, result in cases:
                with self.subTest(size=size, state=state, result=result):
                    app.set_state(state)
                    app.run.result = result
                    app.run.conservation = 18.5 if result != "defeat" else 0
                    renderer.draw(app)
                    for message, rect in renderer.text_rects:
                        self.assertNotIn("↑", message)
                        self.assertNotIn("↓", message)
                        self.assertTrue(pygame.Rect(0, 0, 960, 540).contains(rect), message)
                        if state in ("menu", "instructions"):
                            self.assertTrue(pygame.Rect(140, 90, 680, 380).contains(rect), message)
                    if state in ("playing", "result"):
                        messages = [message for message, _ in renderer.text_rects]
                        expected = f"Sorvete: {format_conservation(app.run.conservation)}"
                        self.assertIn(expected, messages)
                    for message, rect in renderer.physical_text_rects:
                        self.assertTrue(window.canvas.get_rect().contains(rect), message)
                    window.present()
                    viewport = viewport_rect(size)
                    self.assertEqual(window.canvas.get_size(), viewport.size)
                    # Margens fora da área 16:9 conservam a cor de fundo.
                    if viewport.left:
                        self.assertEqual(window.screen.get_at((0, size[1] // 2))[:3], (18, 25, 36))
                    if viewport.top:
                        self.assertEqual(window.screen.get_at((size[0] // 2, 0))[:3], (18, 25, 36))

    def test_display_sizes_do_not_change_simulation(self):
        window = Window()
        outcomes = []
        for size in SIZES:
            window.screen = pygame.display.set_mode(size, pygame.RESIZABLE)
            app = App()
            app.start()
            app.run.objects = []
            app.run.jump()
            renderer = Renderer(window.prepare_frame())
            for _ in range(30):
                app.update(1 / 60)
            renderer.draw(app)
            window.present()
            outcomes.append((app.run.distance, app.run.conservation, app.run.player.y,
                             app.run.player.velocity_y, app.run.player.rect(app.run.distance)))
        self.assertTrue(all(outcome == outcomes[0] for outcome in outcomes))


if __name__ == "__main__":
    unittest.main()
