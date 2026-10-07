"""Janela física separada da superfície lógica de 960 × 540 do jogo."""

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
        self.canvas = pygame.Surface((S.WIDTH, S.HEIGHT)).convert()
        self.scaled = None

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
        self.scaled = None

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

    def present(self):
        self.screen.fill((18, 25, 36))
        viewport = viewport_rect(self.screen.get_size())
        if viewport.width and viewport.height:
            if self.scaled is None or self.scaled.get_size() != viewport.size:
                self.scaled = pygame.Surface(viewport.size).convert()
            pygame.transform.smoothscale(self.canvas, viewport.size, self.scaled)
            self.screen.blit(self.scaled, viewport)
        pygame.display.flip()
