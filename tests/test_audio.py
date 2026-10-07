"""Controles, persistência e falhas de áudio; SDL dummy não valida audição."""

import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")
os.environ.setdefault("PYGAME_HIDE_SUPPORT_PROMPT", "1")

import pygame

from game.audio import Audio, MUSIC_PATH
from game.app import App
from game.graphics import Renderer
from game.window import Window


def press(app, key):
    app.handle_event(pygame.event.Event(pygame.KEYDOWN, key=key))


class AudioTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.preference_path = Path(self.temporary.name) / "prefs" / "audio.json"
        self.mixer = MagicMock()
        self.audio = Audio(self.preference_path, mixer=self.mixer)

    def tearDown(self):
        pygame.quit()
        self.temporary.cleanup()

    def test_music_loops_once_and_is_not_restarted_by_screens_or_restart(self):
        self.audio.initialize()
        app = App(self.audio)
        for state in ("instructions", "menu", "playing", "paused", "audio", "result"):
            app.set_state(state)
        app.start()
        self.audio.initialize()
        self.mixer.music.play.assert_called_once_with(loops=-1)
        self.mixer.music.load.assert_called_once_with(str(MUSIC_PATH))
        self.mixer.music.set_volume.assert_called_once_with(.15)

    def test_toggle_uses_pause_and_unpause_not_play(self):
        self.audio.initialize()
        self.audio.toggle()
        self.assertFalse(self.audio.enabled)
        self.mixer.music.pause.assert_called_once()
        self.audio.toggle()
        self.assertTrue(self.audio.enabled)
        self.mixer.music.unpause.assert_called_once()
        self.mixer.music.play.assert_called_once()

    def test_preferences_survive_new_controller_and_volume_limits(self):
        self.audio.toggle()
        self.audio.adjust_volume(.25)
        loaded = Audio(self.preference_path, mixer=self.mixer)
        self.assertFalse(loaded.enabled)
        self.assertAlmostEqual(loaded.volume, .4)
        loaded.adjust_volume(10)
        self.assertEqual(loaded.volume, 1)
        loaded.adjust_volume(-10)
        self.assertEqual(loaded.volume, 0)

    def test_invalid_preferences_use_safe_defaults(self):
        self.preference_path.parent.mkdir()
        for data in ("not json", "[]", '{"enabled": 42, "volume": "LOUD"}', '{"volume": NaN}'):
            self.preference_path.write_text(data)
            audio = Audio(self.preference_path, mixer=self.mixer)
            self.assertTrue(audio.enabled)
            self.assertEqual(audio.volume, .15)

    def test_save_failure_does_not_stop_controls(self):
        blocker = Path(self.temporary.name) / "not_a_directory"
        blocker.write_text("x")
        audio = Audio(blocker / "audio.json", mixer=self.mixer)
        audio.toggle()
        self.assertTrue(audio.save_warning)
        self.assertFalse(audio.enabled)

    def test_mixer_or_music_failure_is_nonfatal(self):
        for method in (self.mixer.init, self.mixer.music.load):
            with self.subTest(method=method):
                self.mixer.reset_mock(side_effect=True)
                method.side_effect = pygame.error("falha simulada")
                audio = Audio(self.preference_path, mixer=self.mixer)
                audio.initialize()
                self.assertFalse(audio.available)
                app = App(audio)
                app.start()
                app.update(.1)
                self.assertGreater(app.run.distance, 0)
                audio.toggle()
                self.assertTrue(self.preference_path.exists())

    def test_audio_controls_and_return_to_paused_run(self):
        app = App(self.audio)
        app.start()
        app.run.jump()
        app.update(.1)
        press(app, pygame.K_p)
        app.selection = app.options.index("Áudio")
        press(app, pygame.K_RETURN)
        self.assertEqual(app.state, "audio")
        before = (app.run.distance, app.run.conservation, app.run.player.y,
                  app.run.elapsed, app.run.player.velocity_y)
        press(app, pygame.K_RETURN)
        self.assertFalse(app.audio.enabled)
        press(app, pygame.K_RIGHT)
        self.assertEqual(app.audio.volume, .2)
        press(app, pygame.K_LEFT)
        self.assertEqual(app.audio.volume, .15)
        press(app, pygame.K_SPACE)
        self.assertTrue(app.audio.enabled)
        for _ in range(30):
            app.update(1)
        self.assertEqual(before, (app.run.distance, app.run.conservation, app.run.player.y,
                                  app.run.elapsed, app.run.player.velocity_y))
        press(app, pygame.K_ESCAPE)
        self.assertEqual(app.state, "paused")
        app.update(1)
        self.assertEqual(app.run.elapsed, before[3])
        press(app, pygame.K_p)
        self.assertEqual(app.state, "playing")

    def test_menu_audio_returns_to_menu(self):
        app = App(self.audio)
        app.selection = app.options.index("Áudio")
        press(app, pygame.K_RETURN)
        self.assertEqual(app.state, "audio")
        press(app, pygame.K_ESCAPE)
        self.assertEqual(app.state, "menu")

    def test_mute_saved_preference_starts_without_audible_volume(self):
        self.audio.toggle()
        self.audio.initialize()
        self.mixer.music.set_volume.assert_called_once_with(0)
        self.mixer.music.pause.assert_called_once()

    def test_real_packaged_ogg_loads_and_plays_with_dummy_driver(self):
        audio = Audio(self.preference_path)
        audio.initialize()
        self.assertTrue(audio.available, audio.error)
        self.assertTrue(pygame.mixer.music.get_busy())
        self.assertLessEqual(pygame.mixer.music.get_volume(), .15)
        audio.toggle()
        self.assertFalse(pygame.mixer.music.get_busy())
        audio.toggle()
        self.assertTrue(pygame.mixer.music.get_busy())

    def test_audio_and_four_button_menus_fit_native_sizes(self):
        pygame.display.init()
        pygame.font.init()
        window = Window()
        app = App(self.audio)
        renderer = Renderer(window.canvas)
        for size in ((960, 540), (1920, 1080), (800, 600), (600, 900)):
            window.screen = pygame.display.set_mode(size, pygame.RESIZABLE)
            renderer.resize(window.prepare_frame())
            for state in ("menu", "paused", "audio"):
                for origin in ("menu", "paused"):
                    app.set_state(state)
                    app.audio_return = origin
                    renderer.draw(app)
                    for message, rect in renderer.physical_text_rects:
                        self.assertTrue(window.canvas.get_rect().contains(rect), message)
                    window.present()


if __name__ == "__main__":
    unittest.main()
