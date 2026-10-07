# Roteiro de apresentação — Corre que Derrete!

Proposta de **13 minutos**, com demonstração dentro desse tempo. O enunciado recomenda 10–15 minutos de exposição, seguida de perguntas e demonstração; confirmar o formato com o professor. Se ele preferir a demonstração depois, usar os minutos 9:15–11:45 para aprofundar o código e fazer a demonstração ao final. Este arquivo é um roteiro, não o PPTX/PDF exigido.

Identificação para os slides: Daniel Pena, único integrante informado; 7º período de Engenharia da Computação; professor Pedro Cândido; entrega em 16 de outubro (ano de referência: 2026); apresentação com data a definir pelo professor. Contribuições conhecidas no índice 14. Não inserir uma divisão fictícia. Havendo equipe, distribuir blocos entre os integrantes e garantir que todos saibam explicar o código central. Ensaiar com cronômetro; o roteiro ainda não foi ensaiado.

## Slides, tempo e fala sugerida

| Tempo | Slide / conteúdo | Fala e evidência a preparar |
| --- | --- | --- |
| 0:00–0:45 | 1. Identificação e objetivo | “Corre que Derrete! é uma corrida lateral curta em Python e Pygame. O entregador avança sozinho; precisamos chegar ao cliente antes que o sorvete derreta.” Público: colegas e jogadores iniciantes. Identificar Daniel Pena. |
| 0:45–1:45 | 2. Conceito, escopo e referências | Mostrar esboço textual/fluxo dos docs 01–02. Explicar que conservação reúne tempo e dano numa regra ligada ao tema. Uma rota, três trechos, dois obstáculos e gelo. Não afirmar estudo dos três repositórios indicados; estão registrados como referências futuras. Explicar uso do Pygame e fonte musical efetivamente consultada. |
| 1:45–2:45 | 3. Regras, controles e estados | Conservação: 100%, -2 pontos percentuais/s, -20 por dano e +15 por gelo até 100%. Pontos: metros inteiros + 100/gelo. Espaço/cima salta, P/Esc pausa, menus por setas/Enter e F11. Mostrar diagrama do relatório 13 e vitória/derrota. |
| 2:45–4:00 | 4. Arquitetura e loop | Mostrar os principais módulos, sem uma lista ilegível de todos. “App trata eventos; Run aplica regras; Renderer desenha; Window gerencia apresentação.” Explicar Clock, passo 1/60 s e pausa sem consumir conservação. Mostrar trechos curtos de `main`/`App.update`. |
| 4:00–5:15 | 5. Movimento, câmera e colisões | Explicar mundo → tela e física independente da resolução. Gravidade e salto; AABB `colliderect`, consumo único e proteção. Destino é distância, cliente é contexto visual. Mostrar `Player.rect` e trecho de `Run.update`. Progressão: 260/300/340 e obstáculos mais próximos. |
| 5:15–7:15 | 6. Três técnicas gráficas | Cerca de 40 s cada: parallax com fatores 0,15/0,35/0,70; seis quadros de corrida a 10 trocas/s e dois de salto; partículas com vida, velocidade, transparência e limite 100. Mostrar imagens e as funções do relatório 13. Explicar a finalidade perceptiva de cada técnica. |
| 7:15–8:15 | 7. Evolução visível | Linha do tempo dos commits e comparação de capturas do protótipo/atual. “Preservamos planejamento, protótipo, técnicas e revisões em marcos separados.” Usar o índice 14 e rotular a origem das imagens. Não atribuir dias distintos aos commits da mesma data. |
| 8:15–9:15 | 8. Dificuldades, soluções e testes | Cena 960 × 540 esticada → renderização nativa/fontes maiores; símbolos sem glifo → texto por extenso; rosto frontal → dois olhos/sorriso. 59 testes dummy no último marco, instalação limpa anterior e testes Windows do usuário. Declarar que 60 FPS é alvo, sem medição. |
| 9:15–11:45 | 9. Demonstração ao vivo | Executar sequência abaixo. Mostrar controles, progressão, feedback, pausa/Áudio, F11 e conclusão/reinício. Não editar código ou usar vitória forçada como evidência de jogabilidade. |
| 11:45–13:00 | 10. Resultados, créditos, contribuições e IA | Visual/áudio confirmados satisfatórios no Windows pelo usuário. Dar crédito a HorrorPen/CC BY 3.0, Pygame/Python/fonte e ChatGPT/Codex. “A IA apoiou amplamente implementação, testes e documentação; o estudante forneceu a ideia e testou no Windows.” Explicar as contribuições registradas de Daniel Pena e as limitações. Abrir para perguntas. |

Para reduzir a 10 minutos, resumir conceito, arquitetura e evolução, mantendo explicação das três técnicas. Para chegar a 15 minutos, ampliar leitura do código e demonstração; não inventar testes ou alongar com volume de código.

## Demonstração — aproximadamente 2 min 30 s

1. **0–20 s:** menu e objetivo; abrir Como jogar rapidamente, voltar e iniciar.
2. **20–95 s:** jogar a rota (aproximadamente 61 s ativos se concluída), evidenciando salto, gelo, camadas/quadros, HUD e mudança de trecho. Tentar um impacto quando seguro para mostrar feedback; não prometer vitória se o ensaio não comprovar essa sequência. A conservação baixa pode aparecer ao fim; se não aparecer, explicar com captura real rotulada, sem fingir que ocorreu ao vivo.
3. **95–120 s:** mostrar resultado e cliente se houver vitória; selecionar Jogar novamente. Se houve derrota, explicar condição e reiniciar. Durante essa nova corrida, pausar, abrir Áudio, ajustar volume e voltar à pausa: a distância/conservação devem ficar congeladas. Retomar e alternar F11 uma vez, se testado no computador de apresentação.
4. **120–150 s:** voltar ao menu e encerrar; mencionar que preferências de áudio persistem. Evitar reabrir o jogo só para provar persistência se isso comprometer o tempo; usar evidência registrada após teste real.

Não é necessário forçar vitória e derrota na mesma demonstração curta. As capturas reais anteriores mostram ambas; ensaiar uma rota confiável. Se usar vídeo de segurança, avisar que é gravação, registrar versão/ambiente e não apresentá-lo como execução ao vivo.

## Dificuldades reais que podem ser explicadas

| Problema registrado | Causa/solução | Fonte |
| --- | --- | --- |
| Instalação inicial bloqueada na nuvem | Restrição de rede; instalação repetida com acesso permitido, sem cache, em venv novo. | Relatório 07. Não foi erro de compatibilidade comprovado do Pygame. |
| Retorno de F11 não restaurava tamanho em backend SDL do teste | Reaplicar tamanho quando a primeira saída mantém dimensões do desktop. | Relatório 08 / `Window.toggle_fullscreen`. |
| Setas viravam retângulos e percentuais eram ambíguos | Instruções por extenso, conservação com vírgula e regra em pontos percentuais. | Relatório 08. |
| Full HD parecia imagem esticada | Superfície baixa ampliada; corrigido com desenho/fontes/caches na resolução final. | Relatório 10. |
| Franjas em superfícies transparentes | Correção identificada nas imagens da nuvem e suíte repetida. | Relatório 10. |
| Cliente frontal tinha olho único e boca irregular | Função compartilhada corrigida com simetria e contraste; courier continua de perfil. | Relatório 11 e captura do usuário. |

Esses problemas foram registrados na implementação assistida; não dizer que um integrante os descobriu/resolveu pessoalmente sem evidência. Não inventar dificuldade de áudio: inicialização sem dispositivo é uma falha prevista e testada, não um incidente real relatado no Windows.

## Perguntas para ensaiar a defesa

- Qual é a diferença entre coordenadas de mundo, de tela e pixels da janela?
- Por que F11 não muda o salto ou a colisão? Onde a escala é aplicada?
- O que é AABB e por que a caixa do cone não segue sua silhueta?
- Por que `dt` entra no movimento? O que acontece em um quadro demorado?
- Como a pausa congela partículas e física, mantendo a música?
- Como os índices de animação são escolhidos? Onde termina a vida da partícula?
- Como o módulo mantém o fundo contínuo? Por que velocidades diferentes criam profundidade?
- O que ocorre se gelo, dano e chegada coincidirem? Como o reinício restaura objetos?
- Quais partes tiveram apoio de IA, que recurso externo foi reutilizado e qual a licença?
- O que os testes dummy comprovam e o que depende do computador real?

Preparar respostas localizando código e mostrando exemplos; não decorar frases sem compreender.

## Materiais ainda a preparar

- PPTX ou PDF com estes dez slides, identificação já informada, diagramas, capturas e créditos.
- Capturas reais selecionadas e comparação com protótipo, conforme índice 14.
- Pacote offline do jogo completo e ambiente verificado no computador da avaliação.
- Vídeo curto de segurança, recomendado pelo enunciado, ainda não gravado.
- Ensaio cronometrado, participação dos integrantes e registro de ambiente/estabilidade.
