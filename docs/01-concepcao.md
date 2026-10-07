# Concepção — Corre que Derrete!

Data: 07/10/2026. Estado: proposta para revisão pelo estudante; sem implementação.

## Identidade e escopo

Jogo de corrida lateral em uma rua urbana ensolarada. Um entregador precisa levar um sorvete até o cliente antes que ele derreta. Público: colegas da disciplina e jogadores iniciantes; sessões curtas e controles simples.

A proposta combina dois desafios: escolher o momento do salto e administrar a conservação do sorvete. A barra de conservação substitui vidas separadas, reduzindo a quantidade de regras e conectando o desafio ao tema.

Versão mínima: um personagem, uma rota finita, três trechos, dois obstáculos de chão (cone e caixa), um tipo de coletável (gelo), menu, instruções, pausa, vitória e derrota. Arte 2D simples, com paleta própria, sem necessidade de imagens geradas por IA. Não se prevê combate, multiplayer, loja, inventário, editor, salvamento ou ranking. Áudio é melhoria opcional posterior, não condição para concluir o escopo mínimo.

## Ciclo da partida

1. O jogador lê o objetivo e inicia pelo menu.
2. O entregador corre automaticamente; o cenário se desloca para a esquerda.
3. O jogador salta cones e caixas e coleta gelo por contato.
4. A rota passa de introdução a desafio moderado e, depois, ao trecho final.
5. Chegar ao destino com conservação positiva produz vitória; chegar a zero produz derrota.
6. A tela de resultado permite reiniciar, voltar ao menu ou sair.

## Regras propostas

Os números abaixo são hipóteses de partida para o protótipo, não valores testados nem requisitos do professor.

| Elemento | Regra inicial |
| --- | --- |
| Conservação | Começa em 100 pontos; varia entre 0 e 100 |
| Derretimento | Perda de 2 pontos por segundo de jogo ativo |
| Salto | Espaço ou seta para cima; apenas no chão, sem salto duplo |
| Obstáculo | Contato retira 20 pontos; o entregador continua correndo |
| Proteção após impacto | 0,8 segundo sem novo dano, com personagem piscando |
| Gelo | Recupera 15 pontos, limitado a 100; desaparece após uma coleta |
| Destino | Fim da rota de 18.000 unidades de mundo, a calibrar |
| Pontuação adicional | Não prevista; mostrar progresso e conservação é suficiente |

O personagem fica próximo ao primeiro quarto da tela no eixo horizontal. O jogador controla o salto, não a velocidade. O chão é contínuo, sem buracos; apenas obstáculos visíveis podem causar dano. Gravidade e velocidade vertical determinam o salto e o retorno ao chão.

O dano deve acontecer uma vez por contato, respeitando a proteção após impacto. Cada coletável só pode produzir efeito uma vez. Ao reiniciar, restaurar conservação, distância, posição, velocidade, objetos, partículas e temporizadores.

Na pausa, congelar movimento, derretimento, proteção após impacto e efeitos. O tempo usado nas regras será o tempo de simulação, não o relógio real enquanto a partida estiver pausada.

Para evitar ambiguidade no mesmo quadro: atualizar movimento e derretimento, resolver impactos, resolver coletas, limitar a conservação entre 0 e 100 e avaliar o resultado. Se a conservação final for zero, derrota tem prioridade; caso contrário, atingir a distância final produz vitória. Assim, o gelo coletado naquele quadro pode salvar a entrega. Esta ordem deverá ser demonstrada e revisada no protótipo.

## Progressão pequena e previsível

Uma única fase é dividida pela distância percorrida. Não são três mapas independentes.

| Trecho | Distância | Velocidade proposta | Organização do desafio |
| --- | --- | --- | --- |
| 1 — Saída da sorveteria | 0–6.000 | 260 unidades/s | Espaço inicial livre; obstáculos isolados; gelo fácil de alcançar |
| 2 — Rua movimentada | 6.000–12.000 | 300 unidades/s | Obstáculos mais próximos; algumas coletas exigem salto |
| 3 — Última entrega | 12.000–18.000 | 340 unidades/s | Sequências mais frequentes, com intervalos para aterrissar; destino visível ao final |

Com esses valores, a duração ideal sem pausa é aproximadamente 60,7 segundos (soma da distância de cada trecho dividida por sua velocidade). Sem gelo nem impactos, o sorvete dura 50 segundos: coletar gelo é parte do objetivo. Planejar inicialmente seis gelos ao longo da rota, com o primeiro antes de 20 segundos, e distribuição fixa para facilitar ajustes e demonstração.

Os obstáculos terão posições definidas manualmente, sem geração aleatória na versão mínima. Espaçamento será calculado a partir do tempo de salto e da velocidade local, deixando margem para reação e aterrissagem. Não sobrepor gelo e obstáculo de modo que o dano seja inevitável. Balanceamento, quantidade final de itens e viabilidade da rota dependem de testes futuros.

## Explicação para apresentar

“Corre que Derrete! é uma corrida lateral curta em que o personagem avança sozinho e o jogador decide quando saltar. O sorvete perde conservação com o tempo e com impactos; coletar gelo recupera parte dessa conservação. O objetivo é alcançar o cliente antes que a barra chegue a zero. A rua tem três trechos de dificuldade crescente. Para mostrar conceitos de Computação Gráfica, vamos usar parallax no cenário, animação por quadros no personagem e partículas na coleta de gelo e no derretimento.”
