# Corre que Derrete!

Protótipo de jogo 2D de corrida lateral, em Python 3 e Pygame, para a disciplina de Computação Gráfica.

**Etapa 2 — protótipo com revisão de interface, 07/10/2026.** O usuário informou teste interativo do protótipo anterior no Windows com Python 3.13.7: conseguiu jogar, os controles responderam e as capturas mostram menu, instruções, corrida, derrota e vitória. Nesta revisão, foram adicionados redimensionamento, maximização e F11, com textos corrigidos. Os 34 testes na nuvem passaram; os novos modos de janela ainda precisam de teste interativo no Windows. Não é a versão final da avaliação.

## Objetivo e regras

Entregue o sorvete antes que ele derreta! O entregador avança sozinho. Salte cones e caixas e colete gelo para chegar ao cliente com o sorvete conservado.

- Conservação inicial de 100%; derretimento de 2 pontos percentuais por segundo ativo.
- Impacto: perda de 20 pontos percentuais, uma vez por obstáculo, com proteção de 0,8 segundo.
- Gelo: recupera 15 pontos percentuais, limitado a 100%, e vale 100 pontos.
- Pontuação: 1 ponto por metro inteiro percorrido + 100 por gelo coletado; não é persistida. Exemplo: 658 m e 2 gelos resultam em 858 pontos. Impactos não descontam pontos; afetam a conservação.
- Perdas e recuperações são pontos percentuais, não porcentagens relativas ao valor atual: 80% menos 20 pontos percentuais resulta em 60%; 60% mais 15 resulta em 75%. Perto de 100%, o gelo recupera apenas o espaço restante.
- HUD e resultado mostram conservação com uma casa decimal e vírgula, por exemplo `18,5%`; o arredondamento é apenas visual, sem alterar a simulação.
- Rota fixa de 18.000 unidades gráficas, exibida como 1.800 m (escala ilustrativa de 10 unidades por metro).
- Três trechos de 6.000 unidades, com velocidades de 260, 300 e 340 unidades/s e intervalos de obstáculos de 1.200, 950 e 650 unidades.
- Vitória ao chegar ao destino com conservação positiva; derrota ao zerar.
- No mesmo passo: movimento/derretimento, impactos, coletas, limites e resultado. Um gelo pode salvar a entrega; se o valor final for zero, derrota tem prioridade sobre chegada.
- A pausa congela movimento, salto, derretimento, proteção e avisos. O reinício restaura todos os dados da corrida.

A duração ideal é aproximadamente 61 segundos de simulação. As posições dos objetos são fixas e há seis gelos; dois exigem salto. Não há salto duplo nem buracos.

## Controles

| Contexto | Tecla | Ação |
| --- | --- | --- |
| Corrida | Espaço ou seta para cima | Saltar quando estiver no chão |
| Corrida e pausa | P ou Esc | Pausar/retomar |
| Menu, pausa e resultado | Setas para cima/baixo e Enter | Escolher e confirmar opção |
| Instruções | Enter ou Esc | Voltar ao menu |
| Pausa e resultado | M | Voltar ao menu |
| Resultado | Enter com a primeira opção selecionada | Jogar novamente |
| Menu | Esc | Sair |
| Resultado | Esc | Voltar ao menu |
| Qualquer tela | F11 | Alternar tela cheia e janela |
| Qualquer tela | Arrastar bordas / maximizar | Ajustar o tamanho mantendo a proporção |
| Qualquer tela | Fechar a janela | Encerrar |

A área lógica continua em 960 × 540 (16:9); a janela pode ser redimensionada ou maximizada. A imagem inteira é escalada sem distorções ou recortes, com margens escuras quando necessário. F11 volta ao tamanho de janela anterior. Em janelas pequenas, o texto também fica pequeno: prefira 960 × 540 ou mais para leitura. Tamanho de janela não altera velocidade, gravidade ou hitboxes.

## Baixar e executar no Windows com VS Code

1. Use seu **Python 3.13.7 de 64 bits**, VS Code e a extensão Python da Microsoft. Se precisar instalar Python, marque a opção para adicioná-lo ao PATH. A nuvem foi verificada com Python 3.12.14. O usuário também informou que o protótipo anterior funcionou no Windows com Python 3.13.7; a revisão atual ainda precisa de confirmação nesse computador.
2. Abra o repositório no GitHub, selecione a branch `work` e use **Code → Download ZIP**. Extraia o ZIP. Outra opção, se tiver Git instalado, é clonar a branch `work` com o comando abaixo.
3. No VS Code, use **Arquivo → Abrir Pasta** e selecione a pasta que contém `main.py` e `requirements.txt`.
4. Abra **Terminal → Novo Terminal** e execute os comandos PowerShell abaixo, na raiz do projeto:

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe main.py
```

Para usar Python 3.12, como no ambiente da nuvem, substitua o primeiro comando por `py -3.12 -m venv .venv`. Se o ambiente virtual já existe, use o Python dele diretamente.

Os comandos usam diretamente o Python do ambiente virtual; não exigem ativação nem alteração da política de execução do PowerShell. Se `py` não existir, confirme a instalação do Python e use `python -m venv .venv` com a versão desejada de Python selecionada.

No VS Code, abra **Ctrl+Shift+P → Python: Select Interpreter** e escolha `.venv\Scripts\python.exe`. O jogo começa com uma janela redimensionável de 960 × 540; F11 alterna tela cheia. Selecione Iniciar e pressione Enter; Como jogar apresenta as regras.

Clonagem alternativa da branch publicada:

```powershell
git clone --branch work https://github.com/Danielpr614/corre-que-derrete.git
cd corre-que-derrete
```

Se a interface publicar em outra branch, use o nome informado por ela. Baixar a branch principal antes de incorporar o protótipo pode trazer apenas o projeto inicial.

## Executar na nuvem/Linux e verificar

Com Python 3.12:

```bash
python -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m unittest discover -s tests -v
SDL_VIDEODRIVER=dummy SDL_AUDIODRIVER=dummy .venv/bin/python main.py --smoke-frames 5
```

O último comando verifica inicialização e renderização sem janela visível e encerra após cinco quadros. Para jogar em um ambiente com desktop, execute `python main.py` com o ambiente correto, sem `SDL_VIDEODRIVER=dummy`.

No Windows, os testes automatizados também podem ser chamados assim:

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

Os testes configuram o driver `dummy` apenas dentro do processo de testes. Eles não validam a experiência de uma pessoa jogando.

## Estrutura e decisões técnicas

```text
main.py                Entrada e comando de execução
requirements.txt       Pygame 2.6.1
 game/
  settings.py          Constantes de movimento, regra e janela
  entities.py          Personagem, objetos, hitboxes e rota fixa
  run.py               Simulação, conservação, colisões e resultado
  app.py               Estados, eventos e laço principal
  graphics.py          Desenhos provisórios, textos, telas e HUD
  window.py            Janela, F11 e escala proporcional da imagem
 tests/
  test_rules.py        Regras, estados e renderização sem tela
  test_ui.py           Layout, proporção, textos e modos com SDL dummy
 docs/                 Planejamento, diário, créditos e relatório da etapa 2
```

O laço usa eventos, atualização e desenho. A simulação avança em passos de 1/60 s usando tempo acumulado; posições são números de ponto flutuante. Após um quadro muito demorado, limitar o tempo a 0,25 s evita grandes saltos: durante uma travada, o tempo da simulação pode ficar atrás do relógio real. A meta de renderização é 60 FPS, ainda sem medição no computador de demonstração.

Colisões usam retângulos AABB e `pygame.Rect.colliderect` em coordenadas de mundo. Para desenhar, subtrair o deslocamento da câmera; o HUD usa coordenadas de tela. Formas, cores e desenhos são gerados no código; a fonte é a padrão distribuída com Pygame. Não há caminhos pessoais nem arquivos externos de imagens/áudio. A execução foi verificada de fora da pasta do projeto usando o caminho de `main.py`.

## Evidências e limitações

- Ambiente virtual novo com Python 3.12.14 e Pygame 2.6.1; instalação pelo `requirements.txt` concluída e `pip check` sem dependências quebradas.
- 34 testes automatizados passaram (27 do protótipo + 7 da revisão): movimento, salto, colisões, conservação, progressão, estados, pausa, resultado, reinício, encerramento e chamadas de desenho com SDL dummy.
- Uma sequência programada conclui a rota real com seis gelos e sem impactos; ficar sem comandos leva à derrota. Isso comprova possibilidade lógica, sem medir dificuldade humana.
- Inicialização com cinco quadros dummy e compilação dos arquivos concluídas sem erro.
- **Evidência do usuário:** o protótipo anterior foi jogado no Windows com Python 3.13.7; controles responderam e cinco capturas mostram menu, instruções, corrida, derrota e vitória. Não foi informada a versão de Pygame nem uma medição de FPS.
- **Revisão na nuvem:** renderização em 320 × 240, 640 × 360, 960 × 540, 1280 × 720, 1366 × 768, 1920 × 1080, 800 × 600 e 600 × 900. Inspeção de imagens geradas de instruções, menu 4:3 e vitória em janela de retrato. São superfícies SDL dummy, sem janela de desktop interativa.
- **Pendente no Windows para esta revisão:** redimensionamento real, maximização, F11 repetido, retorno ao tamanho anterior, legibilidade após escala, fluidez e FPS; confirmar controles e resultados após atualizar.
- Arte provisória, sem áudio, ranking, salvamento ou executável `.exe`. Python é necessário para executar esta versão.
- **Ainda pendentes para o marco 3:** parallax, animação por quadros e partículas. A rolagem atual tem uma camada e o personagem é um desenho estático; o mínimo de três técnicas do professor ainda não está concluído.

## Documentação, autoria e histórico

- [Concepção original](docs/01-concepcao.md)
- [Plano original de telas e gráficos](docs/02-telas-e-graficos.md)
- [Requisitos do professor](docs/03-requisitos.md)
- [Plano de etapas](docs/04-plano-de-etapas.md)
- [Diário](docs/05-diario.md)
- [Fontes e apoio de IA](docs/06-fontes-e-ia.md)
- [Implementação e verificações da etapa 2](docs/07-prototipo-e-testes.md)
- [Revisão de interface e evidências Windows/nuvem](docs/08-revisao-interface.md)

O planejamento original foi preservado antes da implementação no commit `bf1db57`. O protótipo tem um marco separado, identificado pela mensagem `feat: registra marco 2 do prototipo jogavel`. Os documentos 01–04 preservam a proposta histórica; o estado efetivo está neste README e no documento 07. A pontuação foi acrescentada por solicitação da etapa 2.

Os marcos de planejamento (`bf1db57`) e protótipo (`2ef4366`) foram enviados ao GitHub na branch `work`. A revisão de interface tem commit separado (`fix: revisa interface e modos de janela`) e envio à mesma branch solicitado pelo usuário. O resultado do envio é confirmado ao encerrar a sessão. Para atualizar uma clonagem local limpa, use `git switch work` e `git pull --ff-only origin work`; quem baixou ZIP deve baixar novamente a branch `work`.

A ideia veio do usuário; a implementação e os testes foram redigidos com apoio de ChatGPT/Codex. O teste Windows informado pelo usuário está registrado separadamente dos testes na nuvem. Compreensão do código e verificação interativa das alterações continuam nas próximas atividades. O enunciado do professor Pedro Cândido segue como referência principal. A versão final também exigirá apresentação, créditos completos e demonstração.
