# Etapa 3 — acabamento visual e Computação Gráfica

Data: 07/10/2026. Escopo preservado: uma rota, três trechos e os mesmos controles, regras, estados, colisões, pontuação e modos de janela. Não foram alteradas constantes físicas ou posições dos obstáculos/gelos.

## Confirmação de execução anterior no Windows

O usuário informou: “A versão revisada abriu e funcionou no meu computador”. Refere-se à revisão de interface anterior, commit `52fb13f`. Não foram informados testes individuais de F11, maximização, redimensionamento, textos ou precisão do HUD. O relato anterior indicou Windows com Python 3.13.7; esta confirmação não informou novamente versão, FPS nem novos arquivos de captura. Não extrapolar o relato para esta etapa 3.

## Organização e identidade visual

Paleta comum em `game/palette.py`: céu ciano, fundos suaves, cidade quente, uniforme azul, mochila alaranjada, gelo ciano e sorvete rosado. Fundo com contraste menor que os elementos de jogo. Menu, instruções e resultados mantêm painéis claros e fonte padrão do Pygame, com atalhos por extenso.

`graphics.py` compõe cenário, destino, objetos, personagem, partículas, feedback, HUD e sobreposições. As técnicas ficam nos módulos abaixo; `window.py` continua escalando a imagem lógica 960 × 540 para a janela. Colisões continuam em coordenadas de mundo, sem fatores de parallax ou alterações pelo tamanho dos desenhos.

## Parallax — `game/parallax.py`

Três superfícies transparentes são geradas uma vez: nuvens, prédios distantes e fachadas próximas. Para cada camada, o deslocamento é `distância_da_câmera × fator`, com repetição por módulo da largura da imagem. Desenhar cópias adjacentes cobre toda a tela.

| Camada | Fator | Efeito |
| --- | --- | --- |
| Nuvens | 0,15 | Movimento lento, sensação de distância |
| Prédios | 0,35 | Profundidade intermediária |
| Fachadas | 0,70 | Movimento mais rápido, próximo do jogador |
| Chão e objetos de jogo | 1,00 | Referência do deslocamento real da rota |
| HUD | 0,00 | Informação fixa na tela |

O sol é um elemento fixo de céu. Nenhuma camada muda hitboxes ou velocidade do jogador. As texturas são padrões próprios desenhados por primitivas, sem geração aleatória de obstáculos.

## Animação por quadros — `game/animation.py`

`CourierAnimation` gera seis superfícies de corrida com pernas alternadas e pequena variação de altura do corpo. A sequência é selecionada por `int(tempo_da_simulação × 10) % 6`, independente da taxa de renderização. Há duas superfícies aéreas: joelhos recolhidos quando a velocidade vertical é negativa (subida) e pernas estendidas quando é positiva ou zero (descida).

As superfícies têm transparência, capacete, uniforme, mochila térmica e sorvete. O desenho é alinhado à posição lógica do personagem; a hitbox original de 42 × 68 continua igual. Ampliar o desenho ou trocar a pose não modifica colisões. O tempo de simulação fica congelado na pausa e no resultado, congelando também a pose.

Um quadro adicional sem sorvete na mão do entregador é usado somente na ilustração de vitória. O cliente decorativo é desenhado com as mesmas primitivas e recebe o sorvete nessa ilustração.

## Partículas — `game/particles.py`

Cada partícula tem tipo, posição de mundo, velocidade, duração e vida restante. Atualizar posição/velocidade com delta de tempo; reduzir vida e remover as expiradas. Transparência diminui proporcionalmente à vida restante. A câmera é subtraída somente ao desenhar, mantendo o efeito no ponto onde ocorreu o evento.

| Evento | Emissão | Forma e cor |
| --- | --- | --- |
| Gelo coletado | 16 partículas por coleta | Pequenos cristais cianos |
| Impacto com dano efetivo | 12 partículas por impacto | Faíscas alaranjadas em cruz |
| Conservação abaixo de 25% | Duas gotas a cada 0,12 s | Gotas rosadas junto ao sorvete |

Vida inicial entre 0,4 e 0,9 segundo; gravidade visual de 190 unidades/s². Limite de 100 partículas simultâneas: descartar emissões que ultrapassem o limite. Usar um gerador pseudoaleatório exclusivo para efeitos, com semente 7; ele não participa das regras nem da rota.

`Run` possui um `Effects`. Contato com gelo ou impacto real chama `burst`; a atualização da simulação movimenta e expira as partículas. Contato protegido não produz novo efeito de dano. A pausa não chama atualização da corrida; reinício cria novos efeitos vazios. Resultado congela o estado visual existente, sem continuar emissão por trás da tela final.

## Feedback e chegada

Coleta: cristais, borda ciana breve, contorno do aviso e texto de recuperação/pontuação. Dano: faíscas, borda alaranjada breve, texto de perda e personagem piscando durante a proteção já existente. Se coleta e dano ocorrerem no mesmo passo, os dois conjuntos de partículas aparecem e a borda de dano tem prioridade.

Conservação baixa: gotas, barra alaranjada com contorno pulsante e aviso textual quando outro aviso não estiver ativo. Assim, avisos e formas complementam cores. A borda breve dura 0,35 segundo; pulsação usa o tempo de simulação e congela na pausa.

O cliente espera diante de uma fachada sinalizada que entra na tela nos últimos metros. Bandeira marca o destino. A condição de vitória continua sendo a distância final com conservação positiva; cliente e fachada não têm colisão. A tela de vitória mostra o entregador de mão vazia e o cliente com sorvete e marca de confirmação, acompanhados de “Sorvete entregue!”. Não há nova fase ou cutscene que altere o fluxo da partida.

## Recursos e autoria

Todos os cenários, quadros, cliente e formas de partículas foram construídos nesta sessão com primitivas do Pygame e apoio de ChatGPT/Codex. São arte simples definida no código; não foram usadas imagens de IA, sprite sheets externas, imagens baixadas, sons ou músicas. A fonte continua sendo a padrão distribuída com Pygame. Não há novas dependências: `pygame==2.6.1` permanece.

Pygame, comunidade Pygame: https://www.pygame.org/ e https://www.pygame.org/docs/. Metadados da biblioteca instalada já registravam LGPL. Créditos e declaração de IA estão em `06-fontes-e-ia.md`. Esta declaração não atribui ao estudante autoria exclusiva do código assistido nem pressupõe que já tenha compreendido todos os módulos.

## Verificações realmente realizadas

Ambiente da nuvem já disponível: Linux, Python 3.12.14, Pygame 2.6.1, SDL dummy. Nenhuma nova instalação de dependências ou medição de FPS nesta sessão.

- A suíte anterior de 34 testes passou após integrar as técnicas.
- Acrescentados dez testes relevantes; suíte final com **44 testes passou**, chamada com `python -m unittest discover -s tests -v` no ambiente de verificação.
- Os novos casos cobrem fatores e repetição do parallax; seis imagens de corrida distintas; escolha temporal e poses de subida/descida sem mudar hitbox; movimento, vida e limite de partículas; início/fim da emissão de gotas; coleta e dano reais com tipos diferentes; prioridade de feedback simultâneo; efeitos congelados na pausa e removidos no reinício; independência das regras em relação às emissões aleatórias; renderização de feedback e chegada.
- Os testes anteriores continuam cobrindo rota completa com salto programado, vitória/derrota, controles, conservação, pontuação, pausa, reinício, proporção, F11 por chamadas programáticas e renderização em oito tamanhos (320 × 240 a 1920 × 1080, incluindo 4:3 e retrato).
- Executado `main.py --smoke-frames 5` com SDL dummy; inicialização e encerramento sem erro.
- Gerada e inspecionada uma montagem estática de quatro cenas: coleta, salto com conservação baixa, aproximação do cliente e vitória. Não observados cortes nos textos principais; cliente e entrega aparecem nas posições previstas. Os valores e efeitos das cenas foram montados para inspeção, não são uma sequência de partida nem evidência de pontuação conquistada por uma pessoa. Arquivo intermediário em `work/etapa3-cenas.png`, ignorado pelo Git.

Nenhuma falha na execução dessas suítes foi observada nesta etapa. Testes que passam não garantem ausência de problemas fora da cobertura. Imagens estáticas e SDL dummy não comprovam fluidez perceptiva ou desempenho no computador.

## Teste necessário no Windows

Atualizar a branch `work` ou baixar novo ZIP e executar com o ambiente que já funciona. Observar profundidade em movimento, corrida/salto e retorno ao chão; reconhecer cristais de coleta, faíscas de dano e gotas; conferir avisos com conservação baixa; observar a aproximação do cliente e a entrega da vitória. Conferir que o desenho dos pés e obstáculos combina com a percepção das colisões.

Pausar durante efeitos e salto, retomar e reiniciar; verificar que partículas e animação congelam/restauram corretamente. Jogar com redimensionamento, maximização e F11 para confirmar a integração visual. Registrar FPS/fluidez com efeitos, legibilidade em tamanhos menores e eventuais erros reais.

## Explicação curta para apresentar

“O parallax cria profundidade ao deslocar nuvens, prédios e fachadas em frações diferentes da distância da câmera. O entregador alterna seis imagens de corrida pelo tempo da simulação e duas de salto pela velocidade vertical. As partículas são entidades temporárias, com velocidade, transparência e vida limitada: cristais para gelo, faíscas para impacto e gotas para derretimento. Essas técnicas só mudam a imagem; as colisões e regras continuam na simulação original.”

Marco separado: `feat: registra etapa 3 de tecnicas graficas`. Push normal para `work` autorizado pelo usuário; confirmar o resultado ao encerrar a sessão. Apresentação PPTX/PDF, revisão humana, teste no computador e pacote final seguem para a etapa 4.
