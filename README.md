# Corre que Derrete!

Protótipo de jogo 2D de corrida lateral, em Python 3 e Pygame, para a disciplina de Computação Gráfica.

**Etapa 2 — protótipo jogável, 07/10/2026.** As regras, telas e gráficos provisórios estão implementados. A instalação e os testes sem tela passaram na nuvem. Validação visual, de teclado real, desempenho e jogabilidade no Windows ainda está pendente. Não é uma versão final da avaliação.

## Objetivo e regras

O entregador avança sozinho. Salte cones e caixas e colete gelo para chegar ao cliente antes que o sorvete derreta.

- Conservação inicial de 100%; derretimento de 2 pontos percentuais por segundo ativo.
- Impacto: perda de 20 pontos percentuais, uma vez por obstáculo, com proteção de 0,8 segundo.
- Gelo: recupera 15 pontos percentuais, limitado a 100%, e vale 100 pontos.
- Pontuação: parte inteira da distância em metros + 100 por gelo coletado; não é persistida.
- Rota fixa de 18.000 unidades gráficas, exibida como 1.800 m (escala ilustrativa de 10 unidades por metro).
- Três trechos de 6.000 unidades, com velocidades de 260, 300 e 340 unidades/s e intervalos de obstáculos de 1.200, 950 e 650 unidades.
- Vitória ao chegar ao destino com conservação positiva; derrota ao zerar.
- No mesmo passo: movimento/derretimento, impactos, coletas, limites e resultado. Um gelo pode salvar a entrega; se o valor final for zero, derrota tem prioridade sobre chegada.
- A pausa congela movimento, salto, derretimento, proteção e avisos. O reinício restaura todos os dados da corrida.

A duração ideal é aproximadamente 61 segundos de simulação. As posições dos objetos são fixas e há seis gelos; dois exigem salto. Não há salto duplo nem buracos.

## Controles

| Contexto | Tecla | Ação |
| --- | --- | --- |
| Corrida | Espaço ou ↑ | Saltar quando estiver no chão |
| Corrida e pausa | P ou Esc | Pausar/retomar |
| Menu, pausa e resultado | ↑ / ↓ e Enter | Escolher e confirmar opção |
| Instruções | Enter ou Esc | Voltar ao menu |
| Pausa e resultado | M | Voltar ao menu |
| Resultado | Enter com a primeira opção selecionada | Jogar novamente |
| Menu | Esc | Sair |
| Resultado | Esc | Voltar ao menu |
| Qualquer tela | Fechar a janela | Encerrar |

## Baixar e executar no Windows com VS Code

1. Instale **Python 3.12 de 64 bits** (marque a opção para adicioná-lo ao PATH), VS Code e a extensão Python da Microsoft. A nuvem foi verificada com Python 3.12.14; Windows ainda não foi testado.
2. Após publicar a branch do protótipo no GitHub, abra o repositório, selecione essa branch e use **Code → Download ZIP**. Extraia o ZIP. Outra opção, se tiver Git instalado, é clonar a branch `work` com o comando abaixo.
3. No VS Code, use **Arquivo → Abrir Pasta** e selecione a pasta que contém `main.py` e `requirements.txt`.
4. Abra **Terminal → Novo Terminal** e execute os comandos PowerShell abaixo, na raiz do projeto:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe main.py
```

Os comandos usam diretamente o Python do ambiente virtual; não exigem ativação nem alteração da política de execução do PowerShell. Se `py` não existir, confirme a instalação do Python e use `python -m venv .venv` com Python 3.12 selecionado.

No VS Code, abra **Ctrl+Shift+P → Python: Select Interpreter** e escolha `.venv\Scripts\python.exe`. O jogo abre uma janela de 960 × 540. Selecione Iniciar e pressione Enter; Como jogar apresenta as regras.

Clonagem alternativa, **após a branch estar publicada**:

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
  graphics.py          Desenhos provisórios, telas e HUD
 tests/
  test_rules.py        Regras, estados e renderização sem tela
 docs/                 Planejamento, diário, créditos e relatório da etapa 2
```

O laço usa eventos, atualização e desenho. A simulação avança em passos de 1/60 s usando tempo acumulado; posições são números de ponto flutuante. Após um quadro muito demorado, limitar o tempo a 0,25 s evita grandes saltos: durante uma travada, o tempo da simulação pode ficar atrás do relógio real. A meta de renderização é 60 FPS, ainda sem medição no computador de demonstração.

Colisões usam retângulos AABB e `pygame.Rect.colliderect` em coordenadas de mundo. Para desenhar, subtrair o deslocamento da câmera; o HUD usa coordenadas de tela. Formas, cores e desenhos são gerados no código; a fonte é a padrão distribuída com Pygame. Não há caminhos pessoais nem arquivos externos de imagens/áudio. A execução foi verificada de fora da pasta do projeto usando o caminho de `main.py`.

## Evidências e limitações

- Ambiente virtual novo com Python 3.12.14 e Pygame 2.6.1; instalação pelo `requirements.txt` concluída e `pip check` sem dependências quebradas.
- 27 testes automatizados passaram: movimento, salto, colisões, conservação, progressão, estados, pausa, resultado, reinício, encerramento e chamadas de desenho com SDL dummy.
- Uma sequência programada conclui a rota real com seis gelos e sem impactos; ficar sem comandos leva à derrota. Isso comprova possibilidade lógica, sem medir dificuldade humana.
- Inicialização com cinco quadros dummy e compilação dos arquivos concluídas sem erro.
- **Pendente no computador:** telas e legibilidade, comandos com teclado real, fluidez, FPS, equilíbrio, instalação Windows e partidas humanas.
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

O planejamento original foi preservado antes da implementação no commit `bf1db57`. O protótipo tem um marco separado, identificado pela mensagem `feat: registra marco 2 do prototipo jogavel`. Os documentos 01–04 preservam a proposta histórica; o estado efetivo está neste README e no documento 07. A pontuação foi acrescentada por solicitação da etapa 2.

Os commits desta sessão são locais na branch `work`; não foi realizado `git push`. Para disponibilizá-los no GitHub, publique/sincronize a branch pela interface, se essa opção estiver disponível, ou use `git push -u origin work` no ambiente que contém estes commits. Não é possível publicar os commits da nuvem a partir de uma cópia local antiga sem primeiro transferi-los.

A ideia veio do usuário; a implementação e os testes foram redigidos com apoio de ChatGPT/Codex. Revisão humana, compreensão do código e validação no computador são parte das próximas atividades. O enunciado do professor Pedro Cândido segue como referência principal. A versão final também exigirá apresentação, créditos completos e demonstração.
