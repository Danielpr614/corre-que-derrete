"""Música única em loop, preferências locais e falha de áudio não fatal."""

import json
import math
from pathlib import Path

import pygame


PROJECT_ROOT = Path(__file__).resolve().parent.parent
MUSIC_PATH = PROJECT_ROOT / "assets" / "audio" / "house_in_a_forest_loop.ogg"
PREFERENCES_PATH = PROJECT_ROOT / ".local" / "audio.json"


class Audio:
    def __init__(self, preference_path=None, music_path=None, mixer=None):
        self.preference_path = Path(preference_path) if preference_path else PREFERENCES_PATH
        self.music_path = Path(music_path) if music_path else MUSIC_PATH
        self.mixer = mixer if mixer is not None else pygame.mixer
        self.enabled = True
        self.volume = .15
        self.available = False
        self.error = ""
        self.save_warning = False
        self.load_preferences()

    def load_preferences(self):
        try:
            data = json.loads(self.preference_path.read_text(encoding="utf-8"))
            if not isinstance(data, dict):
                return
            if isinstance(data.get("enabled"), bool):
                self.enabled = data["enabled"]
            volume = data.get("volume")
            if isinstance(volume, (int, float)) and not isinstance(volume, bool) and math.isfinite(volume):
                self.volume = max(0.0, min(1.0, float(volume)))
        except (OSError, ValueError):
            # Arquivo ausente, inválido ou sem acesso: usar padrões seguros.
            pass

    def save_preferences(self):
        temporary = self.preference_path.with_suffix(".tmp")
        try:
            self.preference_path.parent.mkdir(parents=True, exist_ok=True)
            temporary.write_text(json.dumps({"enabled": self.enabled, "volume": self.volume},
                                            indent=2) + "\n", encoding="utf-8")
            temporary.replace(self.preference_path)
            self.save_warning = False
        except OSError:
            self.save_warning = True

    def initialize(self):
        if self.available:
            return
        try:
            self.mixer.init()
            self.mixer.music.load(str(self.music_path))
            self.mixer.music.set_volume(self.volume if self.enabled else 0)
            self.mixer.music.play(loops=-1)
            if not self.enabled:
                self.mixer.music.pause()
            self.available = True
        except (pygame.error, OSError) as error:
            self.error = str(error)
            self.available = False

    def apply(self):
        if self.available:
            try:
                self.mixer.music.set_volume(self.volume)
                if self.enabled:
                    self.mixer.music.unpause()
                else:
                    self.mixer.music.pause()
            except pygame.error as error:
                self.error = str(error)
                self.available = False
        self.save_preferences()

    def toggle(self):
        self.enabled = not self.enabled
        self.apply()

    def adjust_volume(self, delta):
        value = round(max(0.0, min(1.0, self.volume + delta)), 2)
        if value != self.volume:
            self.volume = value
            self.apply()
