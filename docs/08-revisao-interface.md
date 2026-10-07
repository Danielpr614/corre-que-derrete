# Revisão de interface — 07/10/2026

## Evidência recebida do usuário

O usuário informou que jogou o protótipo anterior no Windows com Python 3.13.7 e que os controles responderam. Anexou cinco capturas na conversa mostrando menu, instruções, corrida, derrota e vitória. A versão instalada do Pygame, a resolução do monitor, o procedimento completo de instalação e o FPS não foram informados.

Nas capturas, as setas aparecem como retângulos; os textos descrevem perdas/ganhos como porcentagens; HUD e resultado têm precisão diferente e usam ponto decimal no resultado. A vitória mostra 1.800 m, quatro gelos e 2.200 pontos: corresponde à fórmula implementada (1.800 + 4 × 100). Não inferir testes de pausa, redimensionamento ou tela cheia a partir dessas capturas.

Essas evidências foram recebidas pela conversa. Os arquivos originais das capturas não foram adicionados ao repositório. O relato confirma uso interativo do protótipo anterior, não da revisão implementada nesta sessão.

## Alterações

- `game/window.py`: janela com `pygame.RESIZABLE`, permitindo bordas e maximização pelo sistema; F11 alterna tela cheia e restaura o tamanho anterior de janela.
- Desenhar em uma superfície lógica fixa de 960 × 540. Escalar somente a imagem final usando `smoothscale`, centralizada em uma área exatamente 16:9, com margens escuras. Usar múltiplos de 16 e 9 evita distorção por arredondamento; pode haver uma pequena margem residual mesmo em tamanhos próximos de 16:9.
- Eventos de redimensionamento atualizam a referência à superfície que o Pygame 2 redimensiona automaticamente. Não recriar o modo em cada evento, preservando o comportamento de maximização do sistema.
- Coordenadas de mundo, dimensões de hitboxes, salto, gravidade, passo fixo e regras continuam independentes da resolução. Nenhuma constante física foi alterada.
- Instruções por extenso: “Setas para cima/baixo: selecionar” e “Espaço ou seta para cima: saltar”. Removidos os glifos de seta de todas as telas atuais.
- Menu: “Entregue o sorvete antes que ele derreta!”. Objetivo nas instruções: “A corrida é automática. Chegue ao cliente antes que o sorvete derreta!”. Isso elimina a formulação pouco clara “com sorvete”.
- Fonte padrão do Pygame mantida, sem depender de fontes instaladas no Windows. Reorganizado o texto das instruções em nove linhas, com corpo de 23 e espaçamento de 29 pixels; título e botões continuam centralizados. Atalhos de salto e pausa/F11 ocupam posições separadas no rodapé da corrida.
- Conservação no HUD e no resultado usa a mesma função: uma casa decimal e vírgula (`18,5%`, `0,0%`, `100,0%`). Distância usa metros inteiros nas duas telas, consistente com pontuação. Aviso de recuperação também usa vírgula decimal.

## Regras explicadas corretamente

Conservação é uma escala de 0% a 100%. Impacto retira **20 pontos percentuais**, calor retira **2 pontos percentuais por segundo ativo** e gelo acrescenta **15 pontos percentuais**, limitado a 100%. Não são fatores relativos ao saldo atual: impacto em 80% deixa 60%, e gelo em 60% deixa 75%. Gelo em 95% recupera somente cinco pontos percentuais; o aviso informa o ganho efetivo. A ordem de resolução no mesmo passo permanece a da etapa 2.

Pontuação = metros inteiros percorridos + 100 × quantidade de gelos coletados. Exemplo: 658 m e dois gelos = 858 pontos. Impacto afeta conservação, sem desconto direto na pontuação. Não há bônus de vitória nem pontuação persistente. Essas regras foram explicitadas no jogo e no README.

## Testes realizados na nuvem

Linux, Python 3.12.14 e Pygame 2.6.1, usando o ambiente de verificação já criado na etapa 2. Não foi feita nova instalação nem teste de Python 3.13 nesta sessão.

Comando: `python -m unittest discover -s tests -v` com o Python desse ambiente. Resultado final: **34 testes passaram** (27 anteriores e sete novos).

Os novos testes verificam proporção exata, centralização, ausência de recorte, dimensões mínimas sem valores negativos, formato decimal, alternância F11 com restauração de tamanho, ignorar repetição da tecla, limites dos textos e conservação idêntica nas telas, margens escuras e simulação idêntica em diferentes tamanhos.

Foram renderizados menu, instruções, corrida, pausa, vitória e derrota em cada tamanho:

| Tamanho da superfície | Resultado observado |
| --- | --- |
| 320 × 240 | Renderiza sem recorte; texto pequeno pela redução da imagem |
| 640 × 360 | Renderiza proporcionalmente |
| 960 × 540 | Resolução lógica de referência |
| 1280 × 720 | Escala proporcional |
| 1366 × 768 | Área 1360 × 765, centralizada com pequenas margens |
| 1920 × 1080 | Escala proporcional |
| 800 × 600 | Margens acima e abaixo para manter 16:9 |
| 600 × 900 | Margens maiores acima e abaixo; conteúdo completo |

**Falha encontrada e corrigida:** no primeiro teste de F11, o backend SDL dummy retornou tamanho de desktop (1024 × 768) na primeira tentativa de restaurar uma janela de 800 × 600. Uma segunda chamada de `set_mode` restaurou o tamanho. Implementada reaplicação condicional somente quando o tamanho retornado difere do solicitado. A suíte foi repetida após a correção e todos os testes passaram.

O comando de entrada `main.py --smoke-frames 5` foi executado com SDL dummy e terminou sem erro. Foram geradas e inspecionadas três imagens na nuvem: instruções em 960 × 540, menu em 800 × 600 e vitória em 600 × 900. Não foram observados textos cortados nessas imagens; título, botões e rodapés ficaram dentro dos painéis. As imagens são intermediários na pasta ignorada `work/`, não capturas de um desktop Windows.

## Pendências interativas no Windows

Atualizar a branch `work` ou baixar novo ZIP. Confirmar bordas de redimensionamento, botão de maximização, F11 no menu/corrida/pausa/resultado, retorno ao tamanho anterior e permanência do estado da partida. Conferir legibilidade, acentos e rodapés em tamanhos diferentes; testar salto/colisões após redimensionar. Medir FPS se necessário.

A nuvem testou modos por chamadas programáticas e SDL dummy. **Não simulou arrastar bordas de uma janela Windows, clicar no botão maximizar ou jogar esta revisão com teclado físico.** Janelas muito pequenas preservam o conteúdo, mas reduzem a legibilidade; recomenda-se pelo menos 960 × 540 para leitura confortável. Parallax, animação por quadros e partículas seguem para a etapa de acabamento.

## Autoria e histórico

O usuário identificou os problemas com testes e capturas. ChatGPT/Codex apoiou implementação, revisão de textos, testes e documentação. O ajuste terá um commit próprio, com mensagem `fix: revisa interface e modos de janela`, seguido de push normal para `work`, preservando os marcos anteriores. A confirmação do push é apresentada ao fim da sessão.
