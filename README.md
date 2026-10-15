# Corre que Derrete!

Uma corrida contra o calor: o entregador avança sozinho, e o jogador precisa saltar os obstáculos e coletar gelo para chegar ao cliente antes que o sorvete derreta. O jogo foi desenvolvido em Python e Pygame para a disciplina de Computação Gráfica, do professor Pedro Cândido.

## Equipe

- Daniel Pena
- John Lucas
- Lucas Oliveira

**Turma:** 7º período de Engenharia da Computação. **Entrega:** 16/10/2026. A data da apresentação ainda não foi informada. A divisão das contribuições e as pendências estão no [registro da equipe e da entrega](docs/16-equipe-e-entrega.md).

## Instalação e execução

É necessário ter Python instalado. A dependência é `pygame==2.6.1`, indicada em `requirements.txt`. Há registros de execução com Python 3.12 na nuvem e Python 3.13.7 no Windows. O VS Code é opcional. Esta distribuição roda com Python; não é um executável `.exe` independente.

Baixe o ZIP da branch `main` no GitHub, extraia e abra a pasta que contém `main.py` e `requirements.txt`. No terminal dessa pasta, execute um comando por vez:

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe main.py
```

Se usar Python 3.12, troque apenas o primeiro comando por `py -3.12 -m venv .venv`. Se não houver o comando `py`, use `python -m venv .venv` depois de conferir a versão com `python --version`. A instalação de dependências precisa de internet. Os comandos não exigem ativar o ambiente virtual nem mudar a política de execução do PowerShell.

Para abrir novamente, basta usar `.\.venv\Scripts\python.exe main.py`. Mantenha as pastas `game` e `assets` junto de `main.py`. Ao usar o VS Code, abra essa mesma pasta e selecione o interpretador `.venv\Scripts\python.exe`.

Em Linux, use:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python main.py
```

Quem utiliza Git pode clonar o projeto com `git clone https://github.com/Danielpr614/corre-que-derrete.git`. A branch `work` mantém a linha de desenvolvimento; a branch `main` deve receber a versão conferida para a entrega. Confira a branch ao baixar um ZIP.

## Como jogar

A rota tem 1.800 metros e três trechos. A velocidade aumenta e os obstáculos ficam mais próximos no decorrer da corrida. Há cones, caixas e seis gelos, dois deles no alto. O chão é contínuo e não há salto duplo.

| Regra | Efeito |
| --- | --- |
| Início | Conservação em 100% |
| Calor | Perda de 2 pontos percentuais por segundo ativo |
| Impacto | Perda de 20 pontos percentuais, uma vez por obstáculo, com 0,8 s de proteção |
| Gelo | Recupera até 15 pontos percentuais, limitado a 100%, e soma 100 pontos |
| Pontuação | Metros inteiros percorridos + 100 por gelo |
| Vitória | Alcançar o cliente com conservação acima de zero |
| Derrota | Zerar a conservação |

Por exemplo, um impacto com 80% deixa 60%. Os valores de conservação aparecem com uma casa decimal e vírgula. Uma partida concluída dura aproximadamente um minuto, sem contar pausas. A pontuação não é salva entre partidas.

| Controle | Ação |
| --- | --- |
| Espaço ou seta para cima | Saltar quando estiver no chão |
| P ou Esc na corrida | Pausar ou retomar |
| Setas para cima/baixo e Enter | Selecionar e confirmar opções |
| M na pausa ou no resultado | Voltar ao menu |
| Enter/Esc nas instruções | Voltar ao menu |
| F11 | Alternar entre janela e tela cheia |
| Arrastar bordas ou maximizar | Ajustar o tamanho da janela |
| Esc no menu, opção Sair ou fechar a janela | Encerrar |

O resultado permite jogar novamente, voltar ao menu ou sair. Reiniciar restaura conservação, rota, objetos e efeitos. Na pausa, os dados da corrida ficam congelados.

## Música e configurações

A opção **Áudio**, no menu inicial e na pausa, permite ligar/desligar a música com Enter ou Espaço e ajustar o volume com esquerda/direita. Esc retorna à tela anterior. A música começa a 15%, repete continuamente e não reinicia quando o jogo troca de tela.

As preferências ficam em `.local/audio.json`, fora do Git. Se não for possível salvar, os controles continuam funcionando durante a execução. Se o dispositivo de áudio ou a faixa não puder ser inicializado, o jogo continua sem música e informa a situação. A faixa e os créditos acompanham o projeto em `assets/audio`.

## Organização e Computação Gráfica

| Arquivo | Função principal |
| --- | --- |
| `main.py` | Entrada do programa |
| `game/app.py` | Eventos, estados e loop |
| `game/run.py` | Regras, conservação, pontuação e resultado |
| `game/entities.py` | Salto, objetos, rota e caixas de colisão |
| `game/graphics.py` | Composição da cena, menus e HUD |
| `game/window.py` e `drawing.py` | Janela, tela cheia e escala do desenho |
| `game/parallax.py` | Rolagem das camadas do cenário |
| `game/animation.py` | Quadros do entregador e desenho do cliente |
| `game/particles.py` | Cristais, faíscas e gotas |
| `game/audio.py` | Música e preferências |
| `game/settings.py` e `palette.py` | Constantes e cores |
| `tests/`, `docs/` e `assets/` | Testes, documentação e recursos |

O loop lê os comandos, atualiza a simulação e desenha a tela. A simulação usa passos de 1/60 s. As colisões usam retângulos AABB com `pygame.Rect.colliderect`. A câmera desloca os objetos do mundo para a tela, enquanto o HUD permanece fixo.

As três técnicas gráficas principais são:

- **Parallax:** nuvens, prédios e fachadas se deslocam com fatores 0,15, 0,35 e 0,70 para criar profundidade.
- **Animação por quadros:** seis poses de corrida, alternadas dez vezes por segundo, e duas poses de salto.
- **Partículas:** cristais na coleta, faíscas no impacto e gotas quando a conservação está baixa. Cada partícula tem tempo de vida e há um limite de 100 ativas.

O desenho usa a resolução da área visível em proporção 16:9. Fontes e recursos são gerados nesse tamanho, evitando ampliar uma imagem pequena já pronta. A referência lógica continua em 960 × 540, de modo que F11 e o tamanho da janela não alteram a física. Veja a explicação das funções no [manual técnico](docs/13-organizacao-e-tecnicas.md).

## Testes e limitações

Execute os testes no Windows com:

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

A revisão de 15/10/2026 instalou as dependências em um ambiente virtual novo e executou os 59 testes com vídeo/áudio simulados. O registro completo está na [conferência do enunciado](docs/12-conferencia-do-enunciado.md). Daniel também jogou no Windows e aprovou o visual e o áudio nas revisões anteriores.

A meta é 60 FPS, sem medição registrada no computador da avaliação. Uma mudança de tamanho pode causar uma breve pausa para regenerar os desenhos. Janelas pequenas reduzem a legibilidade. As colisões aproximam as formas por retângulos. O jogo não tem ranking nem salvamento de partida, e precisa de Python para rodar. Os testes automatizados não substituem a demonstração e o ensaio no computador escolhido.

## Créditos e apoio de IA

| Recurso / ferramenta | Autoria, fonte e licença | Uso no projeto |
| --- | --- | --- |
| Tema e decisões solicitadas | Daniel Pena | Ideia de entregador/sorvete, escopo, revisões e testes Windows relatados. |
| Código e desenhos geométricos | Implementação elaborada com apoio amplo de ChatGPT/Codex | Módulos, primitivas de personagens/cenário/objetos, testes e documentação; não copiados de uma base de jogo. Nenhuma licença geral escolhida para o projeto. |
| Python 3 | Python Software Foundation, https://www.python.org/; licença PSF: https://docs.python.org/3/license.html | Linguagem e biblioteca padrão. |
| Pygame 2.6.1 | Comunidade Pygame, https://www.pygame.org/; LGPL informada nos metadados do pacote | Desenho, eventos, tempo, retângulos, fontes e mixer. |
| Fonte padrão `freesansbold.ttf` / FreeSans | Free Software Foundation, copyright 2002; metadados do arquivo fornecido pelo Pygame declaram GNU GPL e indicam http://www.gnu.org/copyleft/gpl.html | `pygame.font.Font(None, ...)`; fonte do pacote, não copiada separadamente para recursos. Preservar licenças/avisos ao empacotar dependências. |
| House In a Forest Loop | HorrorPen, copyright 2012; [fonte original](https://opengameart.org/content/loop-house-in-a-forest); [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/) | Ogg sem alteração de conteúdo; cópia obtida do demo Godot, autoria/licença verificadas no README específico. [Créditos completos](assets/audio/CREDITOS.md). |
| ChatGPT/Codex | OpenAI, https://openai.com/chatgpt/ | Concepção, implementação, desenhos por código, testes, diagnóstico, documentação e Git. Finalidades, arquivos afetados e validações por marco em [fontes e IA](docs/06-fontes-e-ia.md). Ver declaração detalhada no registro de fontes e IA. |
| Enunciado | Professor Pedro Cândido; DOCX fornecido pelo usuário | Referência acadêmica principal, relida nesta revisão. Sem licença informada. |

Os três repositórios de jogos indicados pelo professor estão registrados como referências de estudo; não foi afirmada consulta de seus conteúdos nem adaptação de código deles. Não foram usados sprites/imagens externos ou gerados por IA. A música não foi gerada por IA. Os três integrantes devem compreender o conteúdo entregue. As contribuições são registradas conforme as atividades efetivamente realizadas, em [equipe e entrega](docs/16-equipe-e-entrega.md).

## Construção e materiais da entrega

O projeto passou por concepção, protótipo jogável, técnicas gráficas e revisões de interface, resolução e áudio. O histórico Git e os registros mantêm essas etapas, sem recriar datas ou contribuições. Os documentos iniciais descrevem o planejamento daquela época; o README apresenta a versão atual.

- [Concepção](docs/01-concepcao.md), [esboços e fluxo inicial](docs/02-telas-e-graficos.md) e [plano de etapas](docs/04-plano-de-etapas.md)
- [Diário](docs/05-diario.md) e [fontes e uso de IA](docs/06-fontes-e-ia.md)
- [Conferência dos requisitos, entregáveis e rubrica](docs/12-conferencia-do-enunciado.md)
- [Manual de código e técnicas](docs/13-organizacao-e-tecnicas.md)
- [Evidências e evolução](docs/14-evidencias-e-evolucao.md)
- [Roteiro da apresentação](docs/15-roteiro-apresentacao.md)
- [Equipe e fechamento da entrega](docs/16-equipe-e-entrega.md)

Os slides preparados em 07/10 precisam receber os três nomes, a divisão real de contribuições e ser incluídos no pacote/repositório. Até isso ocorrer, a apresentação é uma pendência de entrega. Também faltam confirmar o ensaio no computador da avaliação e preparar a cópia de segurança. O vídeo curto é recomendado. Antes de enviar o link ao professor, conferir o acesso público e o conteúdo da branch `main`.
