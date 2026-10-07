"""Fundos desenhados uma vez; rolagem repetida com fatores de profundidade."""

import pygame

from game import settings as S
from game.drawing import Draw
from game.palette import CREAM, SKY


def layer_offset(distance, factor, width):
    return (distance * factor) % width


class Parallax:
    def __init__(self, scale=1.0):
        self.scale = scale
        self.layers = []
        self.sky = pygame.Surface((round(S.WIDTH * scale), round(S.HEIGHT * scale)))
        height = self.sky.get_height()
        for y in range(height):
            t = y / max(1, height - 1)
            color = tuple(round(a + (b - a) * t) for a, b in zip((127, 204, 236), (218, 241, 230)))
            pygame.draw.line(self.sky, color, (0, y), (self.sky.get_width(), y))
        clouds = pygame.Surface((round(1400 * scale), round(S.HEIGHT * scale * 2)), pygame.SRCALPHA)
        d = Draw(clouds, scale * 2)
        for x, y in ((80, 157), (395, 190)):
            d.ellipse((240, 249, 246), (x, y, 145, 28))
            d.circle((240, 249, 246), (x + 48, y), 24)
            d.circle((240, 249, 246), (x + 90, y + 2), 18)
        clouds = pygame.transform.smoothscale(clouds, (round(700 * scale), round(S.HEIGHT * scale)))
        self.layers.append((clouds, .15))

        skyline = pygame.Surface((round(960 * scale), round(S.HEIGHT * scale)), pygame.SRCALPHA)
        d = Draw(skyline, scale)
        for index, height in enumerate((130, 185, 150, 210, 170, 135)):
            x = index * 160
            d.rect((133, 183, 193), (x, S.GROUND_Y - height, 136, height))
            for y in range(S.GROUND_Y - height + 20, S.GROUND_Y - 10, 32):
                for column in range(3):
                    d.rect((179, 210, 210), (x + 15 + column * 36, y, 16, 17))
            d.line((115, 167, 181), (x, S.GROUND_Y - height), (x + 136, S.GROUND_Y - height), 3)
            d.rect((115, 167, 181), (x + 20, S.GROUND_Y - height - 6, 35, 6))
        self.layers.append((skyline, .35))

        shops = pygame.Surface((round(800 * scale), round(S.HEIGHT * scale)), pygame.SRCALPHA)
        d = Draw(shops, scale)
        for x, color, height in ((20, (233, 188, 141), 125),
                                 (295, (190, 211, 191), 150),
                                 (580, (223, 174, 161), 120)):
            top = S.GROUND_Y - height
            d.rect(color, (x, top, 195, height))
            d.rect((61, 116, 132), (x + 18, top + 55, 158, height - 55))
            d.rect(CREAM, (x + 12, top + 26, 170, 29))
            for stripe in range(8):
                if stripe % 2 == 0:
                    d.rect((204, 120, 103), (x + 12 + stripe * 21, top + 26, 21, 29))
            d.line((219, 237, 222), (x + 95, top + 60), (x + 95, S.GROUND_Y), 4)
            d.line((255, 232, 197), (x, top + 3), (x + 195, top + 3), 3)
            d.rect((232, 216, 175), (x + 65, top + 70, 32, 12), border_radius=2)
            d.line((199, 232, 231), (x + 23, top + 64), (x + 54, top + 95), 2)
            d.rect((162, 109, 74), (x + 165, S.GROUND_Y - 20, 24, 20), border_radius=3)
            d.circle((98, 160, 112), (x + 176, S.GROUND_Y - 25), 15)
        self.layers.append((shops, .7))

    def draw(self, surface, distance):
        d = Draw(surface, self.scale)
        surface.blit(self.sky, (0, 0))
        d.circle((255, 234, 167), (825, 154), 45)
        d.circle((255, 217, 106), (825, 154), 38)
        for tile, factor in self.layers:
            offset = round(layer_offset(distance * self.scale, factor, tile.get_width()))
            for x in range(-offset, surface.get_width(), tile.get_width()):
                surface.blit(tile, (x, 0))
        d.rect((72, 81, 95), (0, S.GROUND_Y, S.WIDTH, 110))
        d.rect((241, 197, 130), (0, S.GROUND_Y, S.WIDTH, 12))
        d.line((255, 222, 173), (0, S.GROUND_Y + 1), (S.WIDTH, S.GROUND_Y + 1), 2)
        for x in range(-round(distance % 110), S.WIDTH, 110):
            d.rect(CREAM, (x, 476, 62, 5), border_radius=2)
        for x in range(-round(distance % 80), S.WIDTH, 80):
            d.line((180, 147, 112), (x, S.GROUND_Y + 3), (x, S.GROUND_Y + 11), 1)
