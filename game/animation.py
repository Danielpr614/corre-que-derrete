"""Quadros próprios gerados com primitivas, sem mover a hitbox do personagem."""

import pygame

from game.palette import BLUE, CREAM, ICE, INK, ORANGE, PINK


class CourierAnimation:
    FPS = 10

    def __init__(self):
        self.running = [self.make_frame(pose) for pose in range(6)]
        self.jumping = [self.make_frame(6), self.make_frame(7)]
        self.delivery = self.make_frame(8)

    @staticmethod
    def make_frame(pose):
        frame = pygame.Surface((82, 88), pygame.SRCALPHA)
        # Cabeça, capacete, mochila térmica e uniforme usam a mesma paleta.
        bob = 1 if pose in (1, 4) else 0
        pygame.draw.rect(frame, ORANGE, (5, 36 + bob, 21, 29), border_radius=5)
        pygame.draw.line(frame, CREAM, (9, 44 + bob), (23, 44 + bob), 3)
        pygame.draw.circle(frame, (246, 197, 154), (38, 24 + bob), 12)
        pygame.draw.circle(frame, BLUE, (38, 19 + bob), 13, draw_top_left=True, draw_top_right=True)
        pygame.draw.line(frame, INK, (38, 16 + bob), (53, 16 + bob), 4)
        pygame.draw.circle(frame, INK, (44, 24 + bob), 2)
        pygame.draw.rect(frame, BLUE, (24, 37 + bob, 29, 25), border_radius=7)
        pygame.draw.line(frame, CREAM, (31, 44 + bob), (43, 44 + bob), 3)
        pygame.draw.line(frame, (246, 197, 154), (48, 43 + bob), (66, 40 + bob), 6)
        if pose < 6:
            leg_poses = ((-10, 12), (-5, 7), (0, 0), (12, -10), (7, -5), (0, 2))
            front, back = leg_poses[pose]
            pygame.draw.line(frame, INK, (32, 60), (31 + back, 78), 7)
            pygame.draw.line(frame, BLUE, (45, 60), (45 + front, 78), 7)
            pygame.draw.line(frame, INK, (29 + back, 79), (38 + back, 79), 5)
            pygame.draw.line(frame, INK, (43 + front, 79), (54 + front, 79), 5)
        else:
            # Subida: joelhos recolhidos; descida: pernas estendidas.
            knee_y, foot_y = (64, 68) if pose == 6 else (69, 79)
            pygame.draw.lines(frame, INK, False, [(32, 60), (22, knee_y), (34, foot_y)], 7)
            pygame.draw.lines(frame, BLUE, False, [(45, 60), (56, knee_y), (49, foot_y)], 7)
        if pose == 8:
            return frame
        pygame.draw.polygon(frame, (221, 158, 88), [(64, 37 + bob), (78, 37 + bob), (71, 55 + bob)])
        pygame.draw.circle(frame, PINK, (71, 32 + bob), 10)
        pygame.draw.circle(frame, CREAM, (68, 29 + bob), 3)
        return frame

    def frame_index(self, player, elapsed):
        if player.grounded:
            return "running", int(elapsed * self.FPS) % len(self.running)
        return "jumping", 0 if player.velocity_y < 0 else 1

    def frame(self, player, elapsed):
        state, index = self.frame_index(player, elapsed)
        return (self.running if state == "running" else self.jumping)[index]

    def draw(self, surface, player, elapsed, screen_x):
        surface.blit(self.frame(player, elapsed), (screen_x - 16, round(player.y) - 12))


def draw_customer(surface, x, feet_y, delivered=False):
    """Cliente decorativo: espera na calçada e recebe o sorvete na vitória."""
    top = feet_y - 70
    pygame.draw.circle(surface, (128, 80, 58), (x + 20, top + 13), 12)
    pygame.draw.rect(surface, (85, 145, 118), (x + 6, top + 28, 28, 24), border_radius=7)
    pygame.draw.line(surface, INK, (x + 12, top + 50), (x + 10, feet_y), 6)
    pygame.draw.line(surface, INK, (x + 29, top + 50), (x + 32, feet_y), 6)
    pygame.draw.line(surface, (128, 80, 58), (x + 8, top + 32), (x - 8, top + 29), 5)
    pygame.draw.circle(surface, CREAM, (x + 23, top + 10), 2)
    pygame.draw.arc(surface, CREAM, (x + 15, top + 12, 11, 9), 3.2, 6.1, 2)
    if delivered:
        pygame.draw.polygon(surface, ORANGE, [(x - 16, top + 24), (x - 2, top + 24), (x - 9, top + 40)])
        pygame.draw.circle(surface, PINK, (x - 9, top + 20), 9)
        pygame.draw.circle(surface, ICE, (x + 30, top - 17), 12)
        pygame.draw.lines(surface, INK, False,
                          [(x + 24, top - 17), (x + 29, top - 12), (x + 37, top - 22)], 3)
