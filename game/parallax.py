"""Fundos desenhados uma vez; rolagem repetida com fatores de profundidade."""

import pygame

from game import settings as S
from game.palette import CREAM, SKY


def layer_offset(distance, factor, width):
    return (distance * factor) % width


class Parallax:
    def __init__(self):
        self.layers = []
        clouds = pygame.Surface((700, S.HEIGHT), pygame.SRCALPHA)
        for x, y in ((80, 157), (395, 190)):
            pygame.draw.ellipse(clouds, (240, 249, 246), (x, y, 145, 28))
            pygame.draw.circle(clouds, (240, 249, 246), (x + 48, y), 24)
            pygame.draw.circle(clouds, (240, 249, 246), (x + 90, y + 2), 18)
        self.layers.append((clouds, .15))

        skyline = pygame.Surface((960, S.HEIGHT), pygame.SRCALPHA)
        for index, height in enumerate((130, 185, 150, 210, 170, 135)):
            x = index * 160
            pygame.draw.rect(skyline, (133, 183, 193), (x, S.GROUND_Y - height, 136, height))
            for y in range(S.GROUND_Y - height + 20, S.GROUND_Y - 10, 32):
                for column in range(3):
                    pygame.draw.rect(skyline, (179, 210, 210), (x + 15 + column * 36, y, 16, 17))
        self.layers.append((skyline, .35))

        shops = pygame.Surface((800, S.HEIGHT), pygame.SRCALPHA)
        for x, color, height in ((20, (233, 188, 141), 125),
                                 (295, (190, 211, 191), 150),
                                 (580, (223, 174, 161), 120)):
            top = S.GROUND_Y - height
            pygame.draw.rect(shops, color, (x, top, 195, height))
            pygame.draw.rect(shops, (61, 116, 132), (x + 18, top + 55, 158, height - 55))
            pygame.draw.rect(shops, CREAM, (x + 12, top + 26, 170, 29))
            for stripe in range(8):
                if stripe % 2 == 0:
                    pygame.draw.rect(shops, (204, 120, 103), (x + 12 + stripe * 21, top + 26, 21, 29))
            pygame.draw.line(shops, (219, 237, 222), (x + 95, top + 60), (x + 95, S.GROUND_Y), 4)
        self.layers.append((shops, .7))

    def draw(self, surface, distance):
        surface.fill(SKY)
        pygame.draw.circle(surface, (255, 217, 106), (825, 154), 40)
        for tile, factor in self.layers:
            offset = round(layer_offset(distance, factor, tile.get_width()))
            for x in range(-offset, S.WIDTH, tile.get_width()):
                surface.blit(tile, (x, 0))
        pygame.draw.rect(surface, (72, 81, 95), (0, S.GROUND_Y, S.WIDTH, 110))
        pygame.draw.rect(surface, (241, 197, 130), (0, S.GROUND_Y, S.WIDTH, 12))
        for x in range(-round(distance % 110), S.WIDTH, 110):
            pygame.draw.rect(surface, CREAM, (x, 476, 62, 5))
