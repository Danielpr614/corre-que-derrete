"""Estados, entrada do teclado e laço principal com passo fixo."""

import argparse

import pygame

from game import settings as S
from game.graphics import Renderer
from game.run import Run
from game.window import Window
from game.audio import Audio


class App:
    def __init__(self, audio=None):
        self.state = "menu"
        self.selection = 0
        self.running = True
        self.run = Run()
        self.accumulator = 0.0
        self.audio = audio if audio is not None else Audio()
        self.audio_return = "menu"

    @property
    def options(self):
        return {
            "menu": ("Iniciar", "Como jogar", "Áudio", "Sair"),
            "paused": ("Retomar", "Menu", "Áudio", "Sair"),
            "result": ("Jogar novamente", "Menu", "Sair"),
        }.get(self.state, ())

    def set_state(self, state):
        self.state = state
        self.selection = 0
        self.accumulator = 0.0

    def start(self):
        # Reconstruir a corrida restaura também objetos e temporizadores.
        self.run = Run()
        self.set_state("playing")

    def activate(self):
        option = self.options[self.selection]
        if option == "Sair":
            self.running = False
        elif option == "Áudio":
            self.audio_return = self.state
            self.set_state("audio")
        elif option == "Como jogar":
            self.set_state("instructions")
        elif option == "Menu":
            self.set_state("menu")
        elif option == "Retomar":
            self.set_state("playing")
        else:
            self.start()

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
            return
        if event.type != pygame.KEYDOWN or getattr(event, "repeat", False):
            return
        key = event.key
        if self.state == "playing":
            if key in (pygame.K_SPACE, pygame.K_UP):
                self.run.jump()
            elif key in (pygame.K_p, pygame.K_ESCAPE):
                self.set_state("paused")
        elif self.state == "audio":
            if key in (pygame.K_RETURN, pygame.K_SPACE):
                self.audio.toggle()
            elif key == pygame.K_LEFT:
                self.audio.adjust_volume(-.05)
            elif key == pygame.K_RIGHT:
                self.audio.adjust_volume(.05)
            elif key == pygame.K_ESCAPE:
                self.set_state(self.audio_return)
        elif self.state == "instructions":
            if key in (pygame.K_ESCAPE, pygame.K_RETURN, pygame.K_m):
                self.set_state("menu")
        elif self.state in ("menu", "paused", "result"):
            if key == pygame.K_UP:
                self.selection = (self.selection - 1) % len(self.options)
            elif key == pygame.K_DOWN:
                self.selection = (self.selection + 1) % len(self.options)
            elif key == pygame.K_RETURN:
                self.activate()
            elif key == pygame.K_m and self.state != "menu":
                self.set_state("menu")
            elif key == pygame.K_p and self.state == "paused":
                self.set_state("playing")
            elif key == pygame.K_ESCAPE:
                if self.state == "menu":
                    self.running = False
                elif self.state == "paused":
                    self.set_state("playing")
                else:
                    self.set_state("menu")

    def update(self, frame_time):
        if self.state != "playing":
            return
        self.accumulator += max(0.0, min(frame_time, S.MAX_FRAME_TIME))
        while self.accumulator + 1e-12 >= S.FIXED_STEP:
            self.accumulator -= S.FIXED_STEP
            self.run.update(S.FIXED_STEP)
            if self.run.result:
                self.set_state("result")
                break


def main():
    parser = argparse.ArgumentParser(description="Corre que Derrete! — protótipo")
    parser.add_argument("--smoke-frames", type=int, metavar="N",
                        help="encerra após N quadros; útil para verificação sem tela")
    args = parser.parse_args()
    if args.smoke_frames is not None and args.smoke_frames <= 0:
        parser.error("--smoke-frames deve ser positivo")
    pygame.display.init()
    pygame.font.init()
    try:
        window = Window()
        pygame.display.set_caption("Corre que Derrete! — Protótipo")
        renderer = Renderer(window.canvas)
        app = App()
        app.audio.initialize()  # Uma vez; trocar telas não reinicia a música.
        clock = pygame.time.Clock()
        frames = 0
        while app.running:
            frame_time = clock.tick(S.TARGET_FPS) / 1000.0
            # Transições descartam o tempo anterior (inclusive após pausa).
            previous_state = app.state
            for event in pygame.event.get():
                if not window.handle_event(event):
                    app.handle_event(event)
            app.update(0.0 if app.state != previous_state else frame_time)
            renderer.resize(window.prepare_frame())
            renderer.draw(app)
            window.present()
            frames += 1
            if args.smoke_frames is not None and frames >= args.smoke_frames:
                break
    finally:
        pygame.quit()
