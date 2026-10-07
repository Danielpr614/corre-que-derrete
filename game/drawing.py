"""Primitivas em coordenadas lógicas, rasterizadas na resolução de destino."""

import pygame
import pygame.gfxdraw


class Draw:
    def __init__(self, surface, scale=1.0):
        self.surface = surface
        self.scale = scale

    def point(self, point):
        return tuple(round(value * self.scale) for value in point)

    def rect_coords(self, rect):
        return pygame.Rect(*(round(value * self.scale) for value in rect))

    def width(self, value):
        return max(1, round(value * self.scale)) if value else 0

    def rect(self, color, rect, width=0, border_radius=0):
        return pygame.draw.rect(self.surface, color, self.rect_coords(rect),
                                self.width(width), border_radius=round(border_radius * self.scale))

    def circle(self, color, center, radius, width=0, **kwargs):
        center, radius = self.point(center), max(1, round(radius * self.scale))
        if not width and not kwargs and not self.surface.get_flags() & pygame.SRCALPHA:
            pygame.gfxdraw.filled_circle(self.surface, *center, radius, color)
            pygame.gfxdraw.aacircle(self.surface, *center, radius, color)
        else:
            pygame.draw.circle(self.surface, color, center, radius, self.width(width), **kwargs)

    def ellipse(self, color, rect, width=0):
        pygame.draw.ellipse(self.surface, color, self.rect_coords(rect), self.width(width))

    def line(self, color, start, end, width=1):
        pygame.draw.line(self.surface, color, self.point(start), self.point(end), self.width(width))

    def lines(self, color, closed, points, width=1):
        pygame.draw.lines(self.surface, color, closed, [self.point(p) for p in points], self.width(width))

    def polygon(self, color, points, width=0):
        points = [self.point(point) for point in points]
        pygame.draw.polygon(self.surface, color, points, self.width(width))
        if not width and not self.surface.get_flags() & pygame.SRCALPHA:
            pygame.gfxdraw.aapolygon(self.surface, points, color)

    def arc(self, color, rect, start, end, width=1):
        pygame.draw.arc(self.surface, color, self.rect_coords(rect), start, end, self.width(width))
