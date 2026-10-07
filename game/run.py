"""Regras da corrida, independentes da renderização e do teclado."""

from game import settings as S
from game.entities import Player, build_route


class Run:
    def __init__(self):
        self.player = Player()
        self.objects = build_route()
        self.distance = 0.0
        self.conservation = 100.0
        self.elapsed = 0.0
        self.invulnerable = 0.0
        self.ices = 0
        self.hits = 0
        self.result = None
        self.notice = "Vamos entregar esse sorvete!"
        self.notice_time = 2.0

    @property
    def stage(self):
        return min(2, int(self.distance // S.STAGE_LENGTH))

    @property
    def speed(self):
        return S.STAGE_SPEEDS[self.stage]

    @property
    def score(self):
        return int(self.distance / S.WORLD_UNITS_PER_METER) + self.ices * S.ICE_SCORE

    def jump(self):
        return self.result is None and self.player.jump()

    def update(self, dt):
        if self.result is not None or dt <= 0:
            return
        # O controlador chama esta função em passos de 1/60 s.
        self.elapsed += dt
        self.invulnerable = max(0.0, self.invulnerable - dt)
        self.notice_time = max(0.0, self.notice_time - dt)
        self.distance = min(S.ROUTE_LENGTH, self.distance + self.speed * dt)
        self.player.update(dt)
        self.conservation -= S.MELT_RATE * dt
        player_rect = self.player.rect(self.distance)

        # Ordem deliberada: impactos, coletas, limite, resultado.
        for obj in self.objects:
            if obj.kind == "ice" or obj.consumed:
                continue
            if player_rect.colliderect(obj.rect):
                # Cada obstáculo causa no máximo um impacto por passagem.
                obj.consumed = True
                if self.invulnerable <= 0:
                    self.conservation -= S.IMPACT_DAMAGE
                    self.invulnerable = S.INVULNERABILITY
                    self.hits += 1
                    self.notice = "Impacto! -20 de conservação"
                    self.notice_time = 1.2

        for obj in self.objects:
            if obj.kind != "ice" or obj.consumed:
                continue
            if player_rect.colliderect(obj.rect):
                obj.consumed = True
                previous = max(0.0, self.conservation)
                self.conservation = min(100.0, self.conservation + S.ICE_GAIN)
                gained = max(0.0, self.conservation - previous)
                self.ices += 1
                self.notice = f"Gelo! +{gained:.0f} conservação / +100 pontos"
                self.notice_time = 1.2

        self.conservation = max(0.0, min(100.0, self.conservation))
        if self.conservation <= 0:
            self.result = "defeat"
        elif self.distance >= S.ROUTE_LENGTH:
            self.result = "victory"
