"""Composição da cena e interface; técnicas visuais em módulos separados."""

import math

import pygame

from game import settings as S
from game.drawing import Draw
from game.animation import CourierAnimation, draw_customer
from game.parallax import Parallax
from game.palette import BLUE, CREAM, ICE, INK, ORANGE, SKY


def format_conservation(value):
    """Uma casa decimal, vírgula e a mesma apresentação em todas as telas."""
    return f"{value:.1f}".replace(".", ",") + "%"


class Renderer:
    def __init__(self, screen):
        self.text_rects = []
        self.physical_text_rects = []
        self.screen = None
        self.resize(screen)

    def resize(self, screen):
        if self.screen is not None and self.screen.get_size() == screen.get_size():
            self.screen = screen
            self.d = Draw(screen, self.scale)
            return
        self.screen = screen
        self.scale = screen.get_width() / S.WIDTH
        self.d = Draw(screen, self.scale)
        self.background = Parallax(self.scale)
        self.courier = CourierAnimation(self.scale)
        self.effect_layer = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
        # Fonte rasterizada no tamanho final: nunca ampliar texto de 960 × 540.
        self.font = pygame.font.Font(None, max(1, round(27 * self.scale)))
        self.small = pygame.font.Font(None, max(1, round(23 * self.scale)))
        self.title_font = pygame.font.Font(None, max(1, round(64 * self.scale)))
        self.heading = pygame.font.Font(None, max(1, round(40 * self.scale)))

    def text(self, message, position, color=INK, font=None, center=False):
        surface = (font or self.font).render(message, True, color)
        rect = surface.get_rect()
        if center:
            rect.center = self.d.point(position)
        else:
            rect.topleft = self.d.point(position)
        self.screen.blit(surface, rect)
        self.physical_text_rects.append((message, rect.copy()))
        logical = pygame.Rect(*(round(value / self.scale) for value in rect))
        self.text_rects.append((message, logical))

    def panel(self, rect):
        self.d.rect((52, 77, 91), rect.move(0, 4), border_radius=18)
        self.d.rect(CREAM, rect, border_radius=18)
        self.d.rect(INK, rect, width=2, border_radius=18)

    def world(self, run):
        self.background.draw(self.screen, run.distance)
        self.destination(run)

        for obj in run.objects:
            if obj.kind == "ice" and obj.consumed:
                continue
            rect = obj.rect.move(-round(run.distance), 0)
            if rect.right < 0 or rect.left > S.WIDTH:
                continue
            self.d.ellipse((46, 64, 75), (rect.x - 4, S.GROUND_Y - 3, rect.width + 8, 7))
            if obj.kind == "cone":
                self.d.polygon(INK, [rect.midtop, rect.bottomleft, rect.bottomright])
                self.d.polygon(ORANGE,
                                    [rect.midtop, rect.bottomleft, rect.bottomright])
                self.d.polygon((204, 80, 35), [rect.midtop, rect.bottomright, (rect.centerx, rect.bottom)])
                self.d.polygon(CREAM, [(rect.centerx - 9, rect.bottom - 21),
                                      (rect.centerx + 9, rect.bottom - 21),
                                      (rect.centerx + 12, rect.bottom - 15),
                                      (rect.centerx - 12, rect.bottom - 15)])
                self.d.line((255, 180, 100), (rect.centerx - 2, rect.y + 10),
                            (rect.x + 6, rect.bottom - 7), 2)
                self.d.rect(INK, (rect.x - 4, rect.bottom - 4,
                                                  rect.width + 8, 5))
            elif obj.kind == "box":
                self.d.rect((169, 110, 63), rect, border_radius=3)
                self.d.rect(INK, rect, 2, border_radius=3)
                self.d.line((229, 182, 125), rect.midtop, rect.midbottom, 6)
                self.d.rect((196, 141, 89), (rect.x + 3, rect.y + 3, rect.width - 6, 8))
                self.d.line((113, 72, 50), (rect.right - 5, rect.y + 12), (rect.right - 5, rect.bottom - 4), 2)
                self.d.rect(CREAM, (rect.x + 7, rect.y + 24, 14, 12), border_radius=2)
                self.d.line(INK, (rect.x + 10, rect.y + 28), (rect.x + 18, rect.y + 28), 1)
            else:
                self.d.rect((165, 246, 255), rect, border_radius=5)
                self.d.rect(BLUE, rect, 2, border_radius=5)
                self.d.polygon((97, 207, 235), [(rect.right - 9, rect.y + 2),
                                               (rect.right - 2, rect.y + 2),
                                               (rect.right - 2, rect.bottom - 2),
                                               (rect.right - 9, rect.bottom - 2)])
                self.d.line(CREAM, (rect.x + 5, rect.y + 5), (rect.x + 20, rect.y + 5), 2)
                self.d.line((255, 255, 255),
                                 (rect.x + 6, rect.y + 20), (rect.x + 20, rect.y + 6), 3)

        if run.invulnerable <= 0 or int(run.elapsed * 12) % 2 == 0:
            self.courier.draw(self.screen, run.player, run.elapsed, S.PLAYER_SCREEN_X)
        self.effect_layer.fill((0, 0, 0, 0))
        run.effects.draw(self.effect_layer, run.distance, self.scale)
        self.screen.blit(self.effect_layer, (0, 0))
        if run.effects.flash_time > 0:
            color = ORANGE if run.effects.flash_kind == "impact" else ICE
            self.d.rect(color, (5, 5, S.WIDTH - 10, S.HEIGHT - 10),
                             width=5, border_radius=12)

    def destination(self, run):
        x = round(S.ROUTE_LENGTH + S.PLAYER_SCREEN_X - run.distance)
        if x > S.WIDTH or x + 200 < 0:
            return
        self.d.rect((236, 200, 158), (x + 25, 285, 145, 145), border_radius=6)
        self.d.rect((210, 157, 111), (x + 25, 285, 145, 8), border_radius=3)
        self.d.rect(BLUE, (x + 112, 333, 36, 97), border_radius=4)
        self.d.rect((66, 137, 158), (x + 118, 340, 24, 45), border_radius=3)
        self.d.circle(CREAM, (x + 140, 397), 2)
        self.d.rect((206, 168, 127), (x + 30, 422, 132, 8))
        self.d.rect(CREAM, (x + 33, 295, 125, 28), border_radius=4)
        if 0 <= x + 33 and x + 158 <= S.WIDTH:
            self.text("CLIENTE", (x + 95, 309), center=True, font=self.small)
        self.d.line(ORANGE, (x, 364), (x, S.GROUND_Y), 4)
        self.d.polygon(ORANGE, [(x, 365), (x + 25, 376), (x, 387)])
        draw_customer(self.screen, x + 63, S.GROUND_Y, run.result == "victory", self.scale)

    def delivery(self):
        # Ilustração dentro do resultado: não acrescenta estado ou regra.
        self.screen.blit(self.courier.delivery, self.d.point((145, 292)))
        draw_customer(self.screen, 245, 380, delivered=True, scale=self.scale)
        self.text("Sorvete entregue!", (220, 397), center=True, font=self.small)

    def hud(self, run):
        self.panel(pygame.Rect(18, 15, 924, 84))
        self.text(f"Sorvete: {format_conservation(run.conservation)}", (34, 27))
        self.d.rect((220, 222, 222), (34, 61, 190, 17), border_radius=6)
        color = (64, 156, 121) if run.conservation > 25 else ORANGE
        if run.conservation > 0:
            self.d.rect(color,
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
            self.d.rect((strength, 73, 43), (29, 56, 200, 27),
                             width=3, border_radius=7)
        if run.notice_time > 0:
            self.panel(pygame.Rect(155, 110, 650, 38))
            if run.effects.flash_time > 0:
                color = ORANGE if run.effects.flash_kind == "impact" else ICE
                self.d.rect(color, (155, 110, 650, 38), 3, border_radius=18)
            self.text(run.notice, (480, 129), center=True, font=self.small)
        elif run.conservation < 25:
            self.panel(pygame.Rect(155, 110, 650, 38))
            self.text("Conservação baixa! O sorvete está derretendo. Colete gelo.",
                      (480, 129), center=True, font=self.small)
        self.text("Espaço ou seta para cima: saltar", (24, 501), CREAM, self.small)
        self.text("P ou Esc: pausar | F11: tela cheia", (610, 501), CREAM, self.small)

    def options(self, app, top):
        spacing, height = (42, 36) if len(app.options) == 4 else (50, 42)
        for index, option in enumerate(app.options):
            rect = pygame.Rect(300, top + index * spacing, 360, height)
            selected = index == app.selection
            self.d.rect(BLUE if selected else (232, 226, 206),
                             rect, border_radius=10)
            self.text(option, rect.center, CREAM if selected else INK, center=True)
        self.text("Setas para cima/baixo: selecionar | Enter: confirmar", (480, top + spacing * len(app.options) + 16),
                  center=True, font=self.small)

    def draw(self, app):
        self.text_rects.clear()
        self.physical_text_rects.clear()
        over_run = app.state in ("playing", "paused", "result") or (
            app.state == "audio" and app.audio_return == "paused")
        if over_run:
            self.world(app.run)
            self.hud(app.run)
        else:
            self.background.draw(self.screen, 0)
        if app.state == "playing":
            return
        if over_run:
            shade = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
            shade.fill((20, 30, 45, 155))
            self.screen.blit(shade, (0, 0))
        self.panel(pygame.Rect(120, 70, 720, 410))
        if app.state == "menu":
            self.text("CORRE QUE DERRETE!", (480, 127), font=self.title_font, center=True)
            self.text("Entregue o sorvete antes que ele derreta!",
                      (480, 185), center=True)
            self.text("Corrida de sorvete • Python + Pygame", (480, 221),
                      font=self.small, center=True)
            self.options(app, 250)
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
        elif app.state == "audio":
            self.text("ÁUDIO", (480, 120), font=self.heading, center=True)
            status = "Ligada" if app.audio.enabled else "Desligada"
            self.text(f"Música: {status}", (480, 177), center=True)
            self.text(f"Volume: {round(app.audio.volume * 100)}%", (480, 220), center=True)
            self.d.rect((216, 222, 219), (300, 250, 360, 16), border_radius=7)
            if app.audio.volume > 0:
                self.d.rect(BLUE, (300, 250, round(360 * app.audio.volume), 16), border_radius=7)
            self.text("Enter ou Espaço: ligar/desligar a música", (480, 303), center=True)
            self.text("Setas esquerda/direita: ajustar o volume", (480, 337), center=True)
            if not app.audio.available:
                self.text("Som indisponível; o jogo continua sem música.", (480, 372), center=True, font=self.small)
            elif app.audio.save_warning:
                self.text("Não foi possível salvar a preferência nesta pasta.", (480, 372), center=True, font=self.small)
            self.text("House In a Forest Loop - HorrorPen | CC BY 3.0", (480, 410), center=True, font=self.small)
            back = "pausa" if app.audio_return == "paused" else "menu"
            self.text(f"Esc: voltar à {back}" if back == "pausa" else "Esc: voltar ao menu",
                      (480, 451), center=True)
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
