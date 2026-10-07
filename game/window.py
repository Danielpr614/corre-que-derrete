"""Janela e superfície nativa; 960 × 540 é só a referência de coordenadas."""

import pygame

from game import settings as S


def viewport_rect(size):
    """Maior área 16:9 que cabe na janela, centralizada e sem recorte."""
    width, height = size
    # Múltiplos inteiros de 16 e 9 preservam exatamente a proporção.
    unit = max(0, min(width // 16, height // 9))
    viewport = pygame.Rect(0, 0, 16 * unit, 9 * unit)
    viewport.center = (width // 2, height // 2)
    return viewport


class Window:
    def __init__(self):
        self.windowed_size = (S.WIDTH, S.HEIGHT)
        self.fullscreen = False
        self.screen = pygame.display.set_mode(self.windowed_size, pygame.RESIZABLE)
        self.canvas = None
        self.prepare_frame()

    def toggle_fullscreen(self):
        if not self.fullscreen:
            self.windowed_size = self.screen.get_size()
            screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        else:
            screen = pygame.display.set_mode(self.windowed_size, pygame.RESIZABLE)
            # Alguns backends SDL mantêm o tamanho do desktop na primeira
            # saída de tela cheia. Reaplicar só se o tamanho não foi restaurado.
            if screen.get_size() != self.windowed_size:
                screen = pygame.display.set_mode(self.windowed_size, pygame.RESIZABLE)
        self.screen = screen
        self.fullscreen = not self.fullscreen
        self.prepare_frame()

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
            if not getattr(event, "repeat", False):
                self.toggle_fullscreen()
            return True
        if event.type in (pygame.VIDEORESIZE, pygame.WINDOWSIZECHANGED):
            # Pygame 2 redimensiona automaticamente a superfície da janela.
            # Não recriar o modo aqui: isso pode interferir na maximização.
            self.screen = pygame.display.get_surface()
            if not self.fullscreen:
                self.windowed_size = self.screen.get_size()
            return True
        return False

    def prepare_frame(self):
        viewport = viewport_rect(self.screen.get_size())
        size = viewport.size if viewport.width and viewport.height else (16, 9)
        if self.canvas is None or self.canvas.get_size() != size:
            self.canvas = pygame.Surface(size).convert()
        return self.canvas

    def present(self):
        self.screen.fill((18, 25, 36))
        viewport = viewport_rect(self.screen.get_size())
        if viewport.width and viewport.height:
            # Imagem já rasterizada no tamanho final: cópia sem ampliação.
            self.screen.blit(self.canvas, viewport)
        pygame.display.flip()
