# Roteiro de apresentação

Equipe: Daniel Pena, John Lucas e Lucas Oliveira. Versão de 15/10/2026. A apresentação em `presentation/` tem 14 slides, com cerca de 10 a 12 minutos de exposição, seguidos de perguntas e 2 a 3 minutos de demonstração. As falas são sugestões para o ensaio e podem ser adaptadas sem alterar as informações técnicas.

A concepção do tema, gênero, obstáculos e itens é coletiva, conforme relato de Daniel. Os testes Windows foram conduzidos por Daniel. A programação teve geração ampla por ChatGPT/Codex, com registro no documento 06. A divisão abaixo é de exposição, não de autoria de módulos.

## Divisão sugerida

Daniel pode apresentar conceito, regras, evolução e dificuldades. John pode explicar estados, organização do código e colisões. Lucas pode apresentar parallax, quadros, partículas e a demonstração. Quem encerrar pode apresentar contribuições e créditos. Todos precisam saber explicar os conceitos centrais.

## Slides e falas

### 1 Corre que Derrete!

Tempo: 30 segundos.

O nosso projeto é uma corrida lateral em que o entregador precisa chegar ao cliente antes que o sorvete derreta. O personagem corre sozinho, e o jogador decide quando saltar. Vamos apresentar a ideia, as técnicas gráficas e depois mostrar uma partida.

### 2 A ideia do jogo

Tempo: 50 segundos.

Escolhemos juntos o tema, a corrida lateral e os objetos que aparecem no caminho. Queríamos uma partida curta, com controles simples, para colegas e jogadores iniciantes. O sorvete deu sentido às regras: o calor reduz a barra, os impactos fazem perder conservação e o gelo ajuda a recuperar. O objetivo de projeto foi criar um jogo pequeno, mas com começo, desafio e conclusão.

### 3 Regras e controles

Tempo: 50 segundos.

A conservação começa em cem por cento. O calor tira dois pontos percentuais por segundo ativo, e bater em cone ou caixa tira vinte. O gelo recupera até quinze, respeitando o limite de cem. Por exemplo, um impacto com oitenta deixa sessenta. A rota tem mil e oitocentos metros, e a dificuldade aumenta em três trechos. Para vencer, é preciso chegar com conservação acima de zero. A pontuação soma os metros percorridos e cem pontos por gelo.

### 4 O caminho entre as telas

Tempo: 45 segundos.

O jogo usa estados para decidir o que recebe comandos e o que aparece na tela. No menu, podemos iniciar ou ler as instruções. Na corrida, podemos pausar e retomar. A partida termina no resultado, que pode ser vitória ou derrota. O resultado permite reiniciar ou voltar ao menu. As opções de áudio estão no menu e na pausa. Ao ajustar o volume durante uma pausa, a corrida continua congelada.

### 5 Como o código se organiza

Tempo: 60 segundos.

O código separa os comandos, as regras e o desenho. A classe App recebe eventos e controla o estado. Run guarda a corrida e aplica as regras. Renderer desenha, e Window cuida da janela e da tela cheia. A cada repetição do loop, o jogo lê os comandos, atualiza a partida e desenha a tela. O tempo entra nos cálculos para o movimento não depender só da quantidade de quadros. A simulação usa passos fixos de um sessenta avos de segundo. Na pausa, a atualização da corrida para.

### 6 Salto, câmera e colisão

Tempo: 55 segundos.

No salto, o personagem recebe velocidade para cima. A gravidade faz ele voltar ao chão. Enquanto isso, a câmera acompanha o avanço da rota: os objetos se deslocam na tela, mas o HUD fica parado. Para colisões, o jogo usa caixas retangulares, chamadas hitboxes. O colliderect verifica quando elas se sobrepõem. Cada obstáculo pode causar dano uma vez por passagem. A proteção evita impactos seguidos por um curto intervalo. A caixa do cone é uma aproximação, não acompanha cada detalhe da sua forma.

### 7 Parallax no cenário

Tempo: 45 segundos.

O parallax cria profundidade usando velocidades diferentes. As nuvens andam devagar, os prédios ficam no meio e as fachadas próximas se movem mais rápido. São camadas de um cenário 2D. O fundo se repete para continuar a corrida sem terminar de repente. Na implementação, cada camada usa um fator aplicado à distância da câmera. A operação de módulo faz a repetição.

### 8 O movimento do personagem

Tempo: 45 segundos.

A animação funciona pela troca de quadros. Existem seis poses de corrida, alternadas dez vezes por segundo. As pernas mudam de posição e dão a impressão de movimento. No salto, o jogo escolhe uma pose para a subida e outra para a descida. Os quadros ficam guardados na memória. A animação muda o desenho, enquanto a caixa de colisão mantém o mesmo tamanho.

### 9 Partículas e avisos

Tempo: 45 segundos.

Os efeitos ajudam a entender o que aconteceu. A coleta produz cristais, o impacto gera faíscas e a conservação baixa mostra gotas. Cada partícula nasce com uma posição, uma velocidade e um tempo de vida. Ela se move e desaparece ao acabar esse tempo. O limite de cem partículas evita acumular efeitos. O aviso na tela e a mudança na barra complementam a informação. As partículas são visuais: quem calcula a perda de conservação é a regra da corrida.

### 10 Evolução do projeto

Tempo: 55 segundos.

Começamos com a concepção e um protótipo de formas simples. O histórico registra a corrida, o salto e as primeiras colisões antes das melhorias visuais. Depois entraram as camadas do cenário, os quadros e as partículas. Os testes no Windows mostraram que ampliar a janela deixava a imagem pouco definida. A solução foi desenhar na resolução final. Também corrigimos o rosto do cliente e adicionamos a música. As imagens mostram esses estágios, e os commits e o diário registram as mudanças.

### 11 O que precisou de ajuste

Tempo: 50 segundos.

Os testes ajudaram a encontrar problemas visíveis. Algumas setas apareciam como retângulos, então as instruções passaram a usar palavras. A imagem ficava pouco nítida em tela grande, então o desenho passou a usar a resolução final. O cliente frontal parecia ter um olho só e recebeu um rosto com dois olhos e sorriso central. Também verificamos regras, telas e reinício por testes automáticos. Daniel jogou no Windows e aprovou o visual e o áudio. O próximo cuidado é ensaiar no computador da avaliação.

### 12 Participação da equipe e da IA

Tempo: 45 segundos.

Daniel, John e Lucas participaram das escolhas do tema, da corrida lateral, dos obstáculos e dos itens. Daniel executou os testes no Windows e relatou os problemas usados nas revisões. ChatGPT e Codex geraram grande parte do código e apoiaram os desenhos, os testes automatizados e a documentação. Esse uso está registrado com finalidade, partes afetadas e validação. A nossa responsabilidade na apresentação é compreender as regras e explicar as técnicas do projeto.

### 13 Materiais e créditos

Tempo: 30 segundos.

A principal referência foi o enunciado do professor. O jogo usa Python e Pygame, e a arte é desenhada no código. A música é House In a Forest Loop, de HorrorPen, com licença Creative Commons Attribution três ponto zero. Os três repositórios sugeridos estão registrados, mas não copiamos código deles. Os créditos completos e o registro de IA acompanham o projeto.

### 14 Demonstração do jogo

Tempo: 2 a 3 minutos, após exposição e perguntas.

Agora vamos mostrar o jogo funcionando. Começamos pelo menu, iniciamos a corrida e mostramos salto, gelo e obstáculos. Durante a partida, apontamos o HUD e as camadas do cenário. Pausamos uma vez, abrimos Áudio e retomamos. No resultado, mostramos vitória ou derrota e a opção de jogar novamente. Se perdermos, explicamos a condição e reiniciamos. As imagens da apresentação ajudam a mostrar efeitos que não apareçam nessa partida.

## Ensaio e demonstração

Abrir o jogo antes da exposição e conferir o áudio, a pausa e F11 no computador escolhido. A demonstração deve mostrar menu, corrida, salto, coleta, HUD, pausa/Áudio e resultado/reinício. Se houver derrota, explicar a condição e reiniciar. Não é necessário forçar vitória e derrota na mesma demonstração curta. As imagens dos slides apoiam efeitos que não apareçam ao vivo.

Conferir o acesso ao repositório sem login, guardar uma cópia offline e, preferencialmente, gravar vídeo curto da versão final. As cenas preparadas devem continuar identificadas como imagens do renderizador, sem serem tratadas como partidas humanas.

A seção 11 do enunciado cita pesquisa, depuração, ideias e revisão conforme as regras da disciplina. A permissão para geração ampla de código não está expressa; confirmar esse alcance com o professor e manter o uso real declarado.
