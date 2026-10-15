# Corre que Derrete!

Um entregador precisa chegar ao cliente antes que o sorvete derreta. Ele corre sozinho, e o jogador controla os saltos para desviar de cones e caixas e coletar gelo pelo caminho.

Escolhemos uma corrida lateral com partidas curtas e controles simples. A conservação do sorvete reúne os efeitos do calor e dos impactos em uma única barra. O projeto aplica conceitos de Computação Gráfica usando Python e Pygame.

**Equipe:** Daniel Pena, John Lucas e Lucas Oliveira.  
**Disciplina:** Computação Gráfica, professor Pedro Cândido.  
**Turma:** 7º período de Engenharia da Computação.  
**Entrega:** 16/10/2026.

## Como executar

É necessário ter Python instalado. O jogo usa `pygame==2.6.1`, listado no `requirements.txt`. Foi executado com Python 3.12 na verificação automatizada e Python 3.13.7 nos testes de Daniel no Windows. O VS Code é opcional.

Baixe o ZIP da branch `main` no GitHub e extraia. Abra o terminal na pasta que contém `main.py` e `requirements.txt`. No Windows, execute um comando por vez:

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe main.py
```

Se usar Python 3.12, troque o primeiro comando por `py -3.12 -m venv .venv`. Se o computador não tiver o comando `py`, confira `python --version` e use `python -m venv .venv`. A instalação do Pygame precisa de internet. Depois da instalação, o último comando abre o jogo novamente.

Em Linux:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python main.py
```

Mantenha `game/` e `assets/` junto de `main.py`. Esta versão executa com Python, sem um `.exe` independente. Para clonar, use `git clone https://github.com/Danielpr614/corre-que-derrete.git`.

## Regras

A rota tem 1.800 metros, divididos em três trechos. A velocidade aumenta e os obstáculos ficam mais próximos no fim. O chão é contínuo, e não há salto duplo.

| Elemento | Regra |
| --- | --- |
| Conservação | Começa em 100% e perde 2 pontos percentuais por segundo ativo |
| Cone ou caixa | O impacto tira 20 pontos percentuais e dá 0,8 s de proteção |
| Gelo | Recupera até 15 pontos percentuais, limitado a 100%, e soma 100 pontos |
| Pontuação | Metros inteiros percorridos + 100 por gelo |
| Vitória | Chegar ao destino com conservação acima de zero |
| Derrota | Zerar a conservação |

Um impacto com 80% deixa 60%. A pausa congela a corrida, e reiniciar restaura os objetos, os efeitos e os dados da partida. A pontuação não fica salva entre partidas.

## Controles

| Tecla | Ação |
| --- | --- |
| Espaço ou seta para cima | Saltar |
| P ou Esc na corrida | Pausar ou retomar |
| Setas para cima/baixo e Enter | Selecionar e confirmar opções |
| M na pausa ou no resultado | Voltar ao menu |
| Enter ou Esc nas instruções | Voltar ao menu |
| F11 | Alternar tela cheia e janela |
| Opção Sair, Esc no menu ou fechar a janela | Encerrar |

Em **Áudio**, no menu ou na pausa, Enter/Espaço liga ou desliga a música, esquerda/direita ajusta o volume e Esc volta. As preferências ficam em `.local/audio.json`, fora do Git. Sem dispositivo de áudio, o jogo continua sem música.

## Organização do projeto

| Pasta ou arquivo | Conteúdo |
| --- | --- |
| `main.py` | Entrada do programa |
| `game/app.py` | Comandos, estados e loop |
| `game/run.py` e `entities.py` | Regras, movimento, objetos e colisões |
| `game/graphics.py`, `window.py` e `drawing.py` | Cena, interface, janela e escala |
| `game/parallax.py`, `animation.py` e `particles.py` | Técnicas gráficas |
| `game/audio.py` | Música e configurações |
| `game/settings.py` e `palette.py` | Constantes e cores |
| `assets/` | Música e créditos do recurso |
| `tests/` | Testes automatizados |
| `docs/` | Concepção, evolução, técnicas, autoria e verificações |
| `presentation/` | Apresentação, guia e imagens selecionadas |

O loop lê os comandos, atualiza a partida e desenha a tela. A simulação usa passos de 1/60 s. As colisões comparam retângulos por `pygame.Rect.colliderect`.

As técnicas principais são **parallax**, com camadas em velocidades diferentes; **animação por quadros**, com seis poses de corrida e duas de salto; e **partículas**, que representam cristais, faíscas e gotas. A janela pode ser ampliada sem mudar a física. A explicação está no [manual técnico](docs/13-organizacao-e-tecnicas.md).

## Testes e limites

Para executar os testes no Windows:

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

As verificações de regras, telas, gráficos e áudio estão descritas no [relatório de testes e requisitos](docs/12-conferencia-do-enunciado.md). Daniel também testou o jogo no Windows e avaliou o visual e a música.

A meta de desenho é 60 FPS, sem medição registrada na máquina da apresentação. Redimensionar pode causar uma breve pausa. As colisões usam retângulos aproximados. Não há ranking nem salvamento de partida. Falhas de áudio ou de gravação das preferências não impedem jogar.

## Autoria e créditos

Daniel Pena, John Lucas e Lucas Oliveira participaram das escolhas de tema, corrida lateral, obstáculos e itens, conforme relato da equipe. Daniel realizou os testes no Windows e encaminhou os problemas encontrados nas revisões. A [divisão de contribuições](docs/16-equipe-e-entrega.md) detalha essas atividades.

Usamos **ChatGPT/Codex, da OpenAI**, para apoiar a implementação do código, os desenhos feitos no Pygame, os testes e a documentação. O [registro de uso de IA](docs/06-fontes-e-ia.md) identifica as partes afetadas e como os resultados foram verificados.

- **Python 3:** Python Software Foundation, https://www.python.org/. Licença PSF: https://docs.python.org/3/license.html.
- **Pygame 2.6.1:** comunidade Pygame, https://www.pygame.org/. Biblioteca distribuída sob LGPL. A fonte padrão acompanha o pacote; seus avisos constam do [registro de fontes](docs/06-fontes-e-ia.md).
- **Música:** House In a Forest Loop, de HorrorPen, [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/). Origem e atribuição completas em [créditos musicais](assets/audio/CREDITOS.md).
- **Arte:** personagens, cenário e objetos desenhados por primitivas no código, com apoio da ferramenta.

Não reutilizamos código dos três jogos indicados pelo professor. A lista dessas referências e as fontes efetivamente usadas estão no documento 06. A licença da música permanece própria do recurso; não foi escolhida uma licença geral para o código deste projeto.

## Evolução e apresentação

O [diário](docs/05-diario.md) e o [histórico de evidências](docs/14-evidencias-e-evolucao.md) registram concepção, protótipo e revisões. A [conferência do enunciado](docs/12-conferencia-do-enunciado.md) relaciona requisitos e evidências. A [apresentação](presentation/README.md) fica em `presentation/`, com um guia para o ensaio.
