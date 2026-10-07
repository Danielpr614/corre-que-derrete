"""Efeitos cosméticos em coordenadas de mundo, com limite e tempo de vida."""

from dataclasses import dataclass
import random

import pygame

from game.palette import ICE, ORANGE, PINK


@dataclass
class Particle:
    kind: str
    x: float
    y: float
    vx: float
    vy: float
    lifetime: float
    remaining: float


class Effects:
    LIMIT = 100
    MELT_INTERVAL = .12

    def __init__(self):
        self.particles = []
        self.random = random.Random(7)  # Isolado de qualquer regra de jogo.
        self.melt_timer = 0.0
        self.flash_kind = None
        self.flash_time = 0.0

    def emit(self, kind, x, y, count):
        for _ in range(min(count, self.LIMIT - len(self.particles))):
            lifetime = self.random.uniform(.4, .9)
            vx = self.random.uniform(-90, 90)
            vy = self.random.uniform(-150, -45)
            if kind == "melt":
                vx, vy = self.random.uniform(-15, 15), self.random.uniform(15, 45)
            self.particles.append(Particle(kind, x, y, vx, vy, lifetime, lifetime))

    def burst(self, kind, x, y):
        self.emit(kind, x, y, 16 if kind == "ice" else 12)
        # Impacto tem prioridade se coleta e dano ocorrerem no mesmo passo.
        if kind == "impact" or self.flash_kind != "impact" or self.flash_time <= 0:
            self.flash_kind = kind
            self.flash_time = .35

    def update(self, dt, low, x, y):
        self.flash_time = max(0.0, self.flash_time - dt)
        alive = []
        for particle in self.particles:
            particle.remaining -= dt
            if particle.remaining > 0:
                particle.x += particle.vx * dt
                particle.vy += 190 * dt
                particle.y += particle.vy * dt
                alive.append(particle)
        self.particles = alive
        if low:
            self.melt_timer += dt
            while self.melt_timer >= self.MELT_INTERVAL:
                self.melt_timer -= self.MELT_INTERVAL
                self.emit("melt", x, y, 2)
        else:
            self.melt_timer = 0.0

    def draw(self, layer, camera):
        for particle in self.particles:
            x, y = round(particle.x - camera), round(particle.y)
            alpha = round(255 * particle.remaining / particle.lifetime)
            if particle.kind == "ice":
                pygame.draw.polygon(layer, (*ICE, alpha),
                                    [(x, y - 4), (x + 4, y), (x, y + 4), (x - 4, y)])
            elif particle.kind == "impact":
                pygame.draw.line(layer, (*ORANGE, alpha), (x - 3, y - 3), (x + 3, y + 3), 3)
                pygame.draw.line(layer, (*ORANGE, alpha), (x - 3, y + 3), (x + 3, y - 3), 3)
            else:
                pygame.draw.ellipse(layer, (*PINK, alpha), (x - 2, y - 3, 5, 8))
