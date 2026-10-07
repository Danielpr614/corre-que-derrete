"""Composição da cena e interface; técnicas visuais em módulos separados."""

import math

import pygame

from game import settings as S
from game.animation import CourierAnimation, draw_customer
from game.parallax import Parallax
from game.palette import BLUE, CREAM, ICE, INK, ORANGE, SKY


def format_conservation(value):
    """Uma casa decimal, vírgula e a mesma apresentação em todas as telas."""
    return f"{value:.1f}".replace(".", ",") + "%"


class Renderer:
    def __init__(self, screen):
        self.screen = screen
        self.text_rects = []
        self.background = Parallax()
        self.courier = CourierAnimation()
        self.effect_layer = pygame.Surface((S.WIDTH, S.HEIGHT), pygame.SRCALPHA)
        self.font = pygame.font.Font(None, 27)
        self.small = pygame.font.Font(None, 23)
        self.title_font = pygame.font.Font(None, 64)
        self.heading = pygame.font.Font(None, 40)

    def text(self, message, position, color=INK, font=None, center=False):
        surface = (font or self.font).render(message, True, color)
        rect = surface.get_rect()
        if center:
            rect.center = position
        else:
            rect.topleft = position
        self.screen.blit(surface, rect)
        self.text_rects.append((message, rect.copy()))

    def panel(self, rect):
        pygame.draw.rect(self.screen, CREAM, rect, border_radius=18)
        pygame.draw.rect(self.screen, INK, rect, width=2, border_radius=18)

    def world(self, run):
        self.background.draw(self.screen, run.distance)
        self.destination(run)

        for obj in run.objects:
            if obj.kind == "ice" and obj.consumed:
                continue
            rect = obj.rect.move(-round(run.distance), 0)
            if rect.right < 0 or rect.left > S.WIDTH:
                continue
            if obj.kind == "cone":
                pygame.draw.polygon(self.screen, ORANGE,
                                    [rect.midtop, rect.bottomleft, rect.bottomright])
                pygame.draw.line(self.screen, CREAM,
                                 (rect.left + 10, rect.bottom - 16),
                                 (rect.right - 10, rect.bottom - 16), 5)
                pygame.draw.rect(self.screen, INK, (rect.x - 4, rect.bottom - 4,
                                                  rect.width + 8, 5))
            elif obj.kind == "box":
                pygame.draw.rect(self.screen, (169, 110, 63), rect, border_radius=3)
                pygame.draw.rect(self.screen, INK, rect, 2, border_radius=3)
                pygame.draw.line(self.screen, (229, 182, 125), rect.midtop, rect.midbottom, 6)
            else:
                pygame.draw.rect(self.screen, (165, 246, 255), rect, border_radius=5)
                pygame.draw.rect(self.screen, BLUE, rect, 2, border_radius=5)
                pygame.draw.line(self.screen, (255, 255, 255),
                                 (rect.x + 6, rect.y + 20), (rect.x + 20, rect.y + 6), 3)

        if run.invulnerable <= 0 or int(run.elapsed * 12) % 2 == 0:
            self.courier.draw(self.screen, run.player, run.elapsed, S.PLAYER_SCREEN_X)
        self.effect_layer.fill((0, 0, 0, 0))
        run.effects.draw(self.effect_layer, run.distance)
        self.screen.blit(self.effect_layer, (0, 0))
        if run.effects.flash_time > 0:
            color = ORANGE if run.effects.flash_kind == "impact" else ICE
            pygame.draw.rect(self.screen, color, (5, 5, S.WIDTH - 10, S.HEIGHT - 10),
                             width=5, border_radius=12)

    def destination(self, run):
        x = round(S.ROUTE_LENGTH + S.PLAYER_SCREEN_X - run.distance)
        if x > S.WIDTH or x + 200 < 0:
            return
        pygame.draw.rect(self.screen, (236, 200, 158), (x + 25, 285, 145, 145), border_radius=6)
        pygame.draw.rect(self.screen, BLUE, (x + 112, 333, 36, 97), border_radius=4)
        pygame.draw.rect(self.screen, CREAM, (x + 33, 295, 125, 28), border_radius=4)
        if 0 <= x + 33 and x + 158 <= S.WIDTH:
            self.text("CLIENTE", (x + 95, 309), center=True, font=self.small)
        pygame.draw.line(self.screen, ORANGE, (x, 364), (x, S.GROUND_Y), 4)
        pygame.draw.polygon(self.screen, ORANGE, [(x, 365), (x + 25, 376), (x, 387)])
        draw_customer(self.screen, x + 63, S.GROUND_Y, run.result == "victory")

    def delivery(self):
        # Ilustração dentro do resultado: não acrescenta estado ou regra.
        self.screen.blit(self.courier.delivery, (145, 292))
        draw_customer(self.screen, 245, 380, delivered=True)
        self.text("Sorvete entregue!", (220, 397), center=True, font=self.small)

    def hud(self, run):
        self.panel(pygame.Rect(18, 15, 924, 84))
        self.text(f"Sorvete: {format_conservation(run.conservation)}", (34, 27))
        pygame.draw.rect(self.screen, (220, 222, 222), (34, 61, 190, 17), border_radius=6)
        color = (64, 156, 121) if run.conservation > 25 else ORANGE
        if run.conservation > 0:
            pygame.draw.rect(self.screen, color,
                             (34, 61, round(190 * run.conservation / 100), 17), border_radius=6)
        meters = int(run.distance / S.WORLD_UNITS_PER_METER)
        total = int(S.ROUTE_LENGTH / S.WORLD_UNITS_PER_METER)
        self.text(f"Distância: {meters} / {total} m", (260, 27))
        self.text(f"Trecho {run.stage + 1}/3 • {int(run.distance / S.ROUTE_LENGTH * 100)}% da rota",
                  (260, 62), font=self.small)
        self.text(f"Pontos: {run.score}", (660, 27))
        self.text(f"Gelos: {run.ices}  •  Impactos: {run.hits}", (660, 62), font=self.small)
        if run.conservation < 25:
            strength = 140 + round(80 * math.sin(run.elapsed * 4))
            pygame.draw.rect(self.screen, (strength, 73, 43), (29, 56, 200, 27),
                             width=3, border_radius=7)
        if run.notice_time > 0:
            self.panel(pygame.Rect(155, 110, 650, 38))
            if run.effects.flash_time > 0:
                color = ORANGE if run.effects.flash_kind == "impact" else ICE
                pygame.draw.rect(self.screen, color, (155, 110, 650, 38), 3, border_radius=18)
            self.text(run.notice, (480, 129), center=True, font=self.small)
        elif run.conservation < 25:
            self.panel(pygame.Rect(155, 110, 650, 38))
            self.text("Conservação baixa! O sorvete está derretendo. Colete gelo.",
                      (480, 129), center=True, font=self.small)
        self.text("Espaço ou seta para cima: saltar", (24, 501), CREAM, self.small)
        self.text("P ou Esc: pausar | F11: tela cheia", (610, 501), CREAM, self.small)

    def options(self, app, top):
        for index, option in enumerate(app.options):
            rect = pygame.Rect(300, top + index * 50, 360, 42)
            selected = index == app.selection
            pygame.draw.rect(self.screen, BLUE if selected else (232, 226, 206),
                             rect, border_radius=10)
            self.text(option, rect.center, CREAM if selected else INK, center=True)
        self.text("Setas para cima/baixo: selecionar | Enter: confirmar", (480, top + 166),
                  center=True, font=self.small)

    def draw(self, app):
        self.text_rects.clear()
        if app.state in ("playing", "paused", "result"):
            self.world(app.run)
            self.hud(app.run)
        else:
            self.screen.fill(SKY)
        if app.state == "playing":
            return
        if app.state in ("paused", "result"):
            shade = pygame.Surface((S.WIDTH, S.HEIGHT), pygame.SRCALPHA)
            shade.fill((20, 30, 45, 155))
            self.screen.blit(shade, (0, 0))
        self.panel(pygame.Rect(120, 70, 720, 410))
        if app.state == "menu":
            self.text("CORRE QUE DERRETE!", (480, 127), font=self.title_font, center=True)
            self.text("Entregue o sorvete antes que ele derreta!",
                      (480, 185), center=True)
            self.text("Corrida de sorvete • Python + Pygame", (480, 221),
                      font=self.small, center=True)
            self.options(app, 265)
            self.text("Esc: sair | F11: tela cheia", (480, 459), font=self.small, center=True)
        elif app.state == "instructions":
            self.text("COMO JOGAR", (480, 117), font=self.heading, center=True)
            lines = [
                "A corrida é automática. Chegue ao cliente antes que o sorvete derreta!",
                "Espaço ou seta para cima: saltar. Não há salto duplo.",
                "Cones e caixas: perda de 20 pontos percentuais por impacto.",
                "Gelo: recupera 15 pontos percentuais, até 100%, e vale 100 pontos.",
                "Calor: perda de 2 pontos percentuais por segundo de corrida.",
                "Exemplo: impacto com 80% deixa 60%; gelo com 60% deixa 75%.",
                "Pontuação: 1 ponto por metro inteiro + 100 por gelo coletado.",
                "Três trechos: velocidade e frequência de obstáculos aumentam.",
                "P ou Esc: pausar/retomar. F11: alternar tela cheia.",
            ]
            for index, line in enumerate(lines):
                self.text(line, (153, 160 + index * 29), font=self.small)
            self.text("Enter / Esc: voltar ao menu", (480, 451),
                      font=self.font, center=True)
        elif app.state == "paused":
            self.text("PAUSADO", (480, 133), font=self.heading, center=True)
            self.text("A corrida e o derretimento estão congelados.", (480, 190), center=True)
            self.options(app, 242)
            self.text("P ou Esc: retomar | M: menu | F11: tela cheia", (480, 449),
                      font=self.small, center=True)
        else:
            victory = app.run.result == "victory"
            title = "ENTREGA CONCLUÍDA!" if victory else "O SORVETE DERRETEU!"
            self.text(title, (480, 128), font=self.heading, center=True)
            if victory:
                self.delivery()
            self.text(f"Distância: {int(app.run.distance / S.WORLD_UNITS_PER_METER)} m | Pontos: {app.run.score}",
                      (480, 183), center=True)
            self.text(f"Sorvete: {format_conservation(app.run.conservation)}",
                      (480, 216), center=True)
            self.options(app, 265)
            self.text("M ou Esc: menu | F11: tela cheia", (480, 459), font=self.small, center=True)
