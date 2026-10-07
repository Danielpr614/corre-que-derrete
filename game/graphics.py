"""Desenhos provisórios próprios: formas e fonte padrão do Pygame.

Sem arquivos de recursos externos nem dependência do diretório de execução.
Parallax, animação por quadros e partículas ficam para o próximo marco.
"""

import math

import pygame

from game import settings as S


INK = (32, 45, 66)
CREAM = (255, 248, 230)
SKY = (157, 217, 245)
BLUE = (37, 89, 129)
ORANGE = (246, 115, 51)


class Renderer:
    def __init__(self, screen):
        self.screen = screen
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

    def panel(self, rect):
        pygame.draw.rect(self.screen, CREAM, rect, border_radius=18)
        pygame.draw.rect(self.screen, INK, rect, width=2, border_radius=18)

    def world(self, run):
        self.screen.fill(SKY)
        pygame.draw.circle(self.screen, (255, 217, 106), (825, 108), 44)
        # Cenário simples de uma camada, repetido e rolado com a câmera.
        offset = int(run.distance) % 240
        for x in range(-240, S.WIDTH + 240, 240):
            left = x - offset
            pygame.draw.rect(self.screen, (112, 161, 175), (left, 200, 160, 230))
            for row in range(3):
                for column in range(3):
                    pygame.draw.rect(self.screen, (223, 239, 224),
                                     (left + 20 + column * 45, 225 + row * 58, 24, 28))
        pygame.draw.rect(self.screen, (72, 81, 95), (0, S.GROUND_Y, S.WIDTH, 110))
        pygame.draw.rect(self.screen, (241, 197, 130), (0, S.GROUND_Y, S.WIDTH, 12))
        road_offset = int(run.distance) % 110
        for x in range(-110, S.WIDTH + 110, 110):
            pygame.draw.rect(self.screen, CREAM, (x - road_offset, 476, 62, 5))

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

        destination = round(S.ROUTE_LENGTH + S.PLAYER_SCREEN_X - run.distance)
        if destination < S.WIDTH:
            pygame.draw.line(self.screen, INK, (destination, 260),
                             (destination, S.GROUND_Y), 4)
            pygame.draw.rect(self.screen, ORANGE, (destination, 265, 130, 38))
            self.text("DESTINO", (destination + 8, 275), font=self.small)

        if run.invulnerable <= 0 or int(run.elapsed * 12) % 2 == 0:
            rect = run.player.rect(run.distance).move(-round(run.distance), 0)
            # Um único desenho do entregador; não é animação por quadros.
            pygame.draw.circle(self.screen, (245, 193, 145), (rect.centerx, rect.y + 12), 12)
            pygame.draw.rect(self.screen, BLUE, (rect.x + 3, rect.y + 23, 34, 26),
                             border_radius=6)
            pygame.draw.line(self.screen, INK, (rect.x + 12, rect.y + 48),
                             (rect.x + 9, rect.bottom), 8)
            pygame.draw.line(self.screen, INK, (rect.x + 30, rect.y + 48),
                             (rect.x + 33, rect.bottom), 8)
            pygame.draw.rect(self.screen, ORANGE, (rect.x - 9, rect.y + 25, 18, 25),
                             border_radius=4)
            pygame.draw.polygon(self.screen, (221, 158, 88),
                                [(rect.right + 2, rect.y + 23),
                                 (rect.right + 16, rect.y + 23),
                                 (rect.right + 9, rect.y + 41)])
            pygame.draw.circle(self.screen, (255, 228, 237),
                               (rect.right + 9, rect.y + 19), 10)

    def hud(self, run):
        self.panel(pygame.Rect(18, 15, 924, 84))
        percent = math.ceil(run.conservation)
        self.text(f"Sorvete: {percent}%", (34, 27))
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
        if run.notice_time > 0:
            self.panel(pygame.Rect(200, 110, 560, 38))
            self.text(run.notice, (480, 129), center=True, font=self.small)
        elif run.conservation < 25:
            self.text("O sorvete está derretendo! Colete gelo.", (480, 127), center=True)
        self.text("Espaço / ↑: saltar    P / Esc: pausa", (24, 508), CREAM, self.small)

    def options(self, app, top):
        for index, option in enumerate(app.options):
            rect = pygame.Rect(300, top + index * 50, 360, 42)
            selected = index == app.selection
            pygame.draw.rect(self.screen, BLUE if selected else (232, 226, 206),
                             rect, border_radius=10)
            self.text(option, rect.center, CREAM if selected else INK, center=True)
        self.text("↑ / ↓: escolher     Enter: confirmar", (480, top + 166),
                  center=True, font=self.small)

    def draw(self, app):
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
            self.text("Entregue o sorvete antes que a conservação zere.",
                      (480, 185), center=True)
            self.text("Protótipo • Python + Pygame", (480, 221),
                      font=self.small, center=True)
            self.options(app, 265)
            self.text("Esc: sair", (480, 459), font=self.small, center=True)
        elif app.state == "instructions":
            self.text("COMO JOGAR", (480, 117), font=self.heading, center=True)
            lines = [
                "O entregador corre sozinho. Chegue ao cliente com sorvete!",
                "Espaço ou ↑: saltar. Não há salto duplo.",
                "Cones e caixas: -20% de conservação ao bater.",
                "Gelo azul: +15%, até 100%, e +100 pontos.",
                "O calor consome 2% por segundo de corrida.",
                "Três trechos: a velocidade e o desafio aumentam.",
                "P ou Esc: pausa. Pontos: metros percorridos + gelos.",
            ]
            for index, line in enumerate(lines):
                self.text(line, (153, 167 + index * 34), font=self.font)
            self.text("Enter / Esc: voltar ao menu", (480, 451),
                      font=self.font, center=True)
        elif app.state == "paused":
            self.text("PAUSADO", (480, 133), font=self.heading, center=True)
            self.text("A corrida e o derretimento estão congelados.", (480, 190), center=True)
            self.options(app, 242)
            self.text("P / Esc: retomar    M: menu", (480, 449),
                      font=self.small, center=True)
        else:
            victory = app.run.result == "victory"
            title = "ENTREGA CONCLUÍDA!" if victory else "O SORVETE DERRETEU!"
            self.text(title, (480, 128), font=self.heading, center=True)
            self.text(f"Distância: {app.run.distance / 10:.0f} m • Pontos: {app.run.score}",
                      (480, 183), center=True)
            self.text(f"Conservação restante: {app.run.conservation:.1f}%",
                      (480, 216), center=True)
            self.options(app, 265)
            self.text("M / Esc: menu", (480, 459), font=self.small, center=True)
