"""Quadros próprios gerados com primitivas, sem mover a hitbox do personagem."""

import pygame

from game.drawing import Draw
from game.palette import BLUE, CREAM, ICE, INK, ORANGE, PINK


class CourierAnimation:
    FPS = 10

    def __init__(self, scale=1.0):
        self.scale = scale
        self.running = [self.make_frame(pose, scale) for pose in range(6)]
        self.jumping = [self.make_frame(6, scale), self.make_frame(7, scale)]
        self.delivery = self.make_frame(8, scale)

    @staticmethod
    def make_frame(pose, scale=1.0):
        # Suavização de bordas por redução de uma fonte mais detalhada,
        # gerada a 2× a resolução de destino, nunca por ampliação do quadro.
        frame = pygame.Surface((round(164 * scale), round(176 * scale)), pygame.SRCALPHA)
        d = Draw(frame, scale * 2)
        # Cabeça, capacete, mochila térmica e uniforme usam a mesma paleta.
        bob = 1 if pose in (1, 4) else 0
        d.rect(ORANGE, (5, 36 + bob, 21, 29), border_radius=5)
        d.line(CREAM, (9, 44 + bob), (23, 44 + bob), 3)
        d.circle((246, 197, 154), (38, 24 + bob), 12)
        d.circle(BLUE, (38, 19 + bob), 13, draw_top_left=True, draw_top_right=True)
        d.line(INK, (38, 16 + bob), (53, 16 + bob), 4)
        d.circle(INK, (44, 24 + bob), 2)
        d.rect(BLUE, (24, 37 + bob, 29, 25), border_radius=7)
        d.line(CREAM, (31, 44 + bob), (43, 44 + bob), 3)
        d.line((246, 197, 154), (48, 43 + bob), (66, 40 + bob), 6)
        if pose < 6:
            leg_poses = ((-10, 12), (-5, 7), (0, 0), (12, -10), (7, -5), (0, 2))
            front, back = leg_poses[pose]
            d.line(INK, (32, 60), (31 + back, 78), 7)
            d.line(BLUE, (45, 60), (45 + front, 78), 7)
            d.line(INK, (29 + back, 79), (38 + back, 79), 5)
            d.line(INK, (43 + front, 79), (54 + front, 79), 5)
        else:
            # Subida: joelhos recolhidos; descida: pernas estendidas.
            knee_y, foot_y = (64, 68) if pose == 6 else (69, 79)
            d.lines(INK, False, [(32, 60), (22, knee_y), (34, foot_y)], 7)
            d.lines(BLUE, False, [(45, 60), (56, knee_y), (49, foot_y)], 7)
        # Detalhes desenhados na resolução atual, sem ampliar o quadro antigo.
        d.line((19, 60, 88), (27, 52 + bob), (49, 52 + bob), 2)
        d.line(CREAM, (8, 39 + bob), (22, 39 + bob), 1)
        d.line((191, 77, 32), (8, 60 + bob), (22, 60 + bob), 2)
        d.line(CREAM, (15, 47 + bob), (15, 55 + bob), 1)
        d.line(CREAM, (11, 51 + bob), (19, 51 + bob), 1)
        d.line((88, 157, 185), (30, 10 + bob), (43, 10 + bob), 2)
        d.line((18, 47, 73), (25, 23 + bob), (31, 32 + bob), 1)
        d.circle((231, 156, 131), (47, 29 + bob), 2)
        if pose == 8:
            return pygame.transform.smoothscale(frame, (round(82 * scale), round(88 * scale)))
        d.polygon((221, 158, 88), [(64, 37 + bob), (78, 37 + bob), (71, 55 + bob)])
        d.circle(PINK, (71, 32 + bob), 10)
        d.circle(CREAM, (68, 29 + bob), 3)
        d.arc((223, 138, 165), (62, 27 + bob, 16, 13), 3.2, 6, 1)
        d.line((182, 119, 63), (68, 42 + bob), (74, 42 + bob), 1)
        return pygame.transform.smoothscale(frame, (round(82 * scale), round(88 * scale)))

    def frame_index(self, player, elapsed):
        if player.grounded:
            return "running", int(elapsed * self.FPS) % len(self.running)
        return "jumping", 0 if player.velocity_y < 0 else 1

    def frame(self, player, elapsed):
        state, index = self.frame_index(player, elapsed)
        return (self.running if state == "running" else self.jumping)[index]

    def draw(self, surface, player, elapsed, screen_x):
        surface.blit(self.frame(player, elapsed), (round((screen_x - 16) * self.scale), round((player.y - 12) * self.scale)))


def draw_customer(surface, x, feet_y, delivered=False, scale=1.0):
    """Cliente decorativo: espera na calçada e recebe o sorvete na vitória."""
    d = Draw(surface, scale)
    top = feet_y - 70
    d.circle((128, 80, 58), (x + 20, top + 13), 12)
    d.rect((85, 145, 118), (x + 6, top + 28, 28, 24), border_radius=7)
    d.line(INK, (x + 12, top + 50), (x + 10, feet_y), 6)
    d.line(INK, (x + 29, top + 50), (x + 32, feet_y), 6)
    d.line((128, 80, 58), (x + 8, top + 32), (x - 8, top + 29), 5)
    # Rosto frontal: olhos simétricos, alinhados e sorriso central.
    for eye_x in (x + 15, x + 25):
        d.circle(CREAM, (eye_x, top + 11), 2)
        d.circle((32, 25, 30), (eye_x, top + 11), 1)
    d.lines(CREAM, False, [(x + 15, top + 17), (x + 17, top + 19),
                          (x + 20, top + 20), (x + 23, top + 19),
                          (x + 25, top + 17)], 1)
    d.arc((55, 37, 36), (x + 8, top + 1, 24, 19), 0, 3.2, 4)
    d.line((169, 208, 175), (x + 11, top + 32), (x + 29, top + 32), 2)
    d.line((41, 88, 69), (x + 10, top + 49), (x + 30, top + 49), 2)
    d.line(CREAM, (x + 6, feet_y - 1), (x + 14, feet_y - 1), 2)
    d.line(CREAM, (x + 29, feet_y - 1), (x + 37, feet_y - 1), 2)
    if delivered:
        d.polygon(ORANGE, [(x - 16, top + 24), (x - 2, top + 24), (x - 9, top + 40)])
        d.circle(PINK, (x - 9, top + 20), 9)
        d.circle(ICE, (x + 30, top - 17), 12)
        d.lines(INK, False,
                          [(x + 24, top - 17), (x + 29, top - 12), (x + 37, top - 22)], 3)
