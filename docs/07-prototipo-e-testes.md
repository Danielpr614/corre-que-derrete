# Etapa 2 — protótipo e verificações

Data: 07/10/2026. Implementação apoiada por ChatGPT/Codex, conforme solicitação do usuário. Sem validação humana de jogabilidade registrada.

Este documento preserva os resultados da sessão original da etapa 2. Posteriormente, o usuário informou teste interativo no Windows; a evidência e a revisão de interface estão no [relatório 08](08-revisao-interface.md).

## Implementado

Corrida automática, salto com Espaço/↑, gravidade e chão; cones e caixas alternados; colisões AABB, perda de 20 pontos percentuais e proteção de 0,8 s; seis gelos com recuperação de 15 pontos percentuais limitada a 100; derretimento de 2 pontos percentuais/s; rota finita com três trechos; vitória, derrota e prioridade de resolução no mesmo passo; menu, instruções, pausa, resultado, retorno ao menu, reinício e saída; HUD com conservação, distância, progresso, trecho, pontos, gelos e impactos.

Gráficos provisórios desenhados com retângulos, polígonos, círculos e linhas do Pygame. A fonte padrão é fornecida pela biblioteca. Não foram usados pacotes de imagens ou sons nem código de jogos de terceiros.

## Diferenças em relação à concepção

- Pontuação incluída por solicitação do usuário nesta etapa: um ponto por metro inteiro percorrido e 100 por gelo. Sem persistência ou bônus de vitória.
- Distância exibida em metros numa escala ilustrativa de dez unidades gráficas por metro; a rota lógica continua com 18.000 unidades.
- Arquitetura consolidada em `settings`, `entities`, `run`, `app` e `graphics`; as telas ficam em `graphics` e os estados em `app`, evitando um módulo extra para este tamanho de protótipo.
- Avisos textuais e personagem piscando após impacto fornecem feedback provisório. Parallax, animação por quadros e partículas ainda não foram implementados.

## Como os módulos se relacionam

`main.py` chama `app.main()`. `App` recebe eventos e controla estados. Durante a corrida, acumula o tempo de cada quadro e chama `Run.update()` em passos de 1/60 s. `Run` altera os dados das entidades e determina o resultado. `Renderer` lê esses dados e desenha o mundo e a interface.

O personagem tem posição vertical e velocidade de salto; seu avanço horizontal é a distância da corrida. Objetos têm posição de mundo, tipo, dimensões e indicação de contato já resolvido. Obstáculos permanecem desenhados após o contato, mas não causam dano novamente; gelos coletados desaparecem.

Pausar suspende a simulação e zera o acumulador; retomar não acumula o tempo passado na pausa. Reiniciar cria uma nova instância de `Run`, incluindo objetos e temporizadores. A janela fechada produz encerramento em qualquer estado.

## Ambiente e resultados realmente observados

Linux na nuvem, Python 3.12.14, Pygame 2.6.1 e SDL 2.28.4. A fonte das versões foi a execução do Python/Pygame e os metadados do pacote.

1. **Preservação do planejamento:** commit `bf1db57`, criado antes de escrever arquivos do protótipo.
2. **Primeira suíte:** 27 testes executados com o ambiente Pygame já disponível; todos passaram.
3. **Instalação nova:** criado um ambiente virtual separado, sem `--system-site-packages`. A primeira tentativa de `pip install -r requirements.txt` falhou por restrição de acesso ao proxy no sandbox, não por incompatibilidade comprovada da versão. Reexecutada com acesso de rede permitido e sem cache, baixou e instalou Pygame 2.6.1 com sucesso.
4. **Verificação no ambiente novo:** os 27 testes passaram novamente após ajustar o teste de reinício para três partidas sucessivas na mesma instância de `App`. `pip check` informou `No broken requirements found`.
5. **Comando de entrada:** iniciado com SDL dummy por cinco quadros, a partir de `/tmp`, usando o caminho absoluto de `main.py`; encerramento sem erro. Confirma independência do diretório corrente, não inspeção visual.
6. **Sintaxe:** `compileall` sobre entrada, módulos e testes terminou sem erro.

Os ambientes virtuais usados na nuvem estão fora do repositório e não fazem parte da entrega. O procedimento correspondente para Windows está no README, mas ainda não foi executado no Windows.

## Cobertura dos 27 testes

| Grupo | Quantidade | Evidência |
| --- | --- | --- |
| Regras | 17 | Movimento, consumo, pontuação, salto, colisões, proteção, recuperação, limites, progressão e resultados |
| Estados e tempo | 9 | Menu/instruções, teclas de salto, pausa, reinícios, retorno ao menu, saída, delta de tempo e repetição de teclas |
| Desenho dummy | 1 | Chamadas de renderização de todas as telas, ambos os resultados e objetos da rota sem exceção |
| Total | 27 | Todos passaram na nuvem |

Casos relevantes: dano uma vez por cone/caixa; salto evita uma caixa; gelo recupera uma vez; dois obstáculos sobrepostos não duplicam dano durante a proteção; gelo e impacto no mesmo passo respeitam a ordem; derrota prevalece sobre chegada quando o valor final zera; gelo no mesmo passo pode salvar a entrega; resultado interrompe movimento; pausa congela posição e temporizadores; três reinícios sucessivos restauram a corrida; fechar a janela funciona em todos os estados.

O teste de tempo compara dez segundos com quadros simulados a 30, 60 e 144 Hz: mesma distância de 2.600 unidades e conservação de 80. Isso verifica dependência do tempo na simulação, não FPS de renderização nem velocidade do computador.

O teste da rota completa usa dados internos para saltar antes dos obstáculos e dos gelos elevados. Conclui com seis coletas e zero impactos. Também foi executada uma simulação sem comandos, que termina em derrota. O agente programado não representa tempo de reação de uma pessoa, nem confirma que a partida é fácil, divertida ou bem equilibrada.

## Pendências no Windows

Registrar ambiente, procedimento e resultado ao executar cada item:

- Instalar Python/Pygame pelos comandos do README e abrir o jogo pelo VS Code.
- Inspecionar texto, acentos, símbolos, tamanhos e contraste nas cinco telas e nos dois resultados.
- Experimentar Espaço e ↑; verificar salto, aterrissagem, pausas, retomadas e fechamento da janela com entrada real.
- Jogar os três trechos e avaliar tempo de reação, contato visual com hitboxes, acesso aos gelos elevados e conservação.
- Medir estabilidade/FPS no computador de demonstração e registrar travadas se ocorrerem.
- Concluir ou perder, reiniciar várias vezes e confirmar restauração visual e funcional.

Os testes dummy fazem chamadas de desenho em superfícies sem tela. **Não houve validação visual humana, partida humana, medição de FPS nem instalação Windows nesta etapa.**

## Requisitos ainda futuros

O protótipo cobre as mecânicas, estados, colisões, HUD, progressão, organização e dependências. O requisito final de pelo menos três técnicas gráficas ainda depende de parallax, animação por quadros e partículas no marco 3. Arte final, apresentação PPTX/PDF, defesa, instalação no computador e evidências visuais permanecem futuras. Os planos não substituem essas entregas.
