"""Entidades lógicas. Retângulos do Pygame não exigem uma janela."""

from dataclasses import dataclass

import pygame

from game import settings as S


@dataclass
class Player:
    y: float = S.GROUND_Y - S.PLAYER_HEIGHT
    velocity_y: float = 0.0
    grounded: bool = True

    def jump(self):
        if not self.grounded:
            return False
        self.velocity_y = -S.JUMP_SPEED
        self.grounded = False
        return True

    def update(self, dt):
        if self.grounded:
            return
        self.velocity_y += S.GRAVITY * dt
        self.y += self.velocity_y * dt
        floor = S.GROUND_Y - S.PLAYER_HEIGHT
        if self.y >= floor:
            self.y = float(floor)
            self.velocity_y = 0.0
            self.grounded = True

    def rect(self, distance):
        # Todos os testes de contato usam coordenadas de mundo.
        return pygame.Rect(round(distance + S.PLAYER_SCREEN_X), round(self.y),
                           S.PLAYER_WIDTH, S.PLAYER_HEIGHT)


@dataclass
class WorldObject:
    kind: str
    x: float
    y: float
    width: int
    height: int
    consumed: bool = False

    @property
    def rect(self):
        return pygame.Rect(round(self.x), round(self.y), self.width, self.height)


def build_route():
    """Rota fixa: intervalos menores nos trechos mais rápidos.

    As posições representam a distância até o início do contato, antes
    de acrescentar a posição horizontal do jogador na tela.
    """
    objects = []
    obstacle_distances = (
        1000, 2200, 3400, 4600,
        6400, 7350, 8300, 9250, 10200, 11150,
        12300, 12950, 13600, 14250, 14900, 15550, 16200, 16850, 17500,
    )
    for index, distance in enumerate(obstacle_distances):
        kind = "cone" if index % 2 == 0 else "box"
        width, height = (38, 44) if kind == "cone" else (50, 58)
        objects.append(WorldObject(kind, distance + S.PLAYER_SCREEN_X,
                                   S.GROUND_Y - height, width, height))
    for distance, raised in ((1500, False), (4300, False), (7000, True),
                             (9800, False), (13250, True), (16000, False)):
        y = S.GROUND_Y - (130 if raised else 40)
        objects.append(WorldObject("ice", distance + S.PLAYER_SCREEN_X,
                                   y, 32, 32))
    return sorted(objects, key=lambda obj: obj.x)
