# Roteiro de apresentação - versão curta

Equipe: Daniel Pena, John Lucas e Lucas Oliveira. Revisão de 15/10/2026. São 7 slides, com notas de fala no PowerPoint e guia de 3 páginas em `presentation/`.

A seção 8 recomenda 10 a 15 minutos de exposição, seguidos de perguntas e demonstração. Menos slides permitem falar com apoio visual e mostrar recursos durante a partida; não eliminam o conteúdo pedido pelo professor.

## Divisão sugerida

Daniel: ideia, regras e evolução. John: funcionamento e colisões. Lucas: técnicas gráficas e demonstração. A divisão é de fala, não de autoria de módulos. Todos devem compreender os conceitos centrais.

## Slides e falas

### 1. Corre que Derrete!

O nosso jogo é uma corrida lateral: um entregador precisa chegar ao cliente antes que o sorvete derreta. Vamos explicar a ideia rapidamente e mostrar o jogo funcionando.

### 2. A ideia do jogo

Escolhemos uma corrida curta e simples de controlar, voltada para colegas e jogadores iniciantes. O tema liga o calor à conservação do sorvete. O personagem corre sozinho, enquanto o jogador salta obstáculos e pega gelo para chegar ao cliente.

### 3. Regras e controles

O calor reduz a barra com o tempo. Bater tira vinte pontos percentuais, e pegar gelo recupera até quinze, sem passar de cem. Por exemplo, um impacto com oitenta deixa sessenta. A rota tem mil e oitocentos metros em três trechos, cada vez mais rápidos. Para vencer, é preciso chegar com conservação acima de zero. Os pontos somam a distância e cem por gelo.

### 4. Como o jogo responde

O menu inicia a corrida. Podemos pausar, retomar e chegar à tela de resultado. Por trás disso, o programa repete três ações: lê as teclas, calcula o que mudou e desenha a tela de novo. App recebe os comandos, Run aplica as regras e Renderer desenha. Para detectar um impacto, ele compara caixas invisíveis ao redor do jogador e dos objetos. No salto, a gravidade traz o personagem de volta ao chão. A câmera desloca o cenário e mantém o painel de informações parado. Na pausa, os dados da corrida não avançam.

### 5. Três efeitos que aparecem no jogo

O primeiro é o fundo em camadas: as nuvens andam devagar e as lojas mais rápido. Isso dá profundidade e se chama parallax. O segundo é a troca de desenhos: o personagem alterna seis poses para parecer que está correndo e usa duas no salto. Isso é animação por quadros. O terceiro são partículas: pequenos cristais, faíscas ou gotas que aparecem, se movem e somem. No código, cada partícula tem um tempo de vida. Vamos apontar esses três recursos durante a partida.

### 6. Evolução do projeto

O protótipo tinha formas simples e as primeiras regras de corrida e salto. Depois entraram cenário, animação e efeitos. Os testes mostraram problemas de nitidez, símbolos nas instruções e no rosto do cliente. As revisões corrigiram esses pontos e acrescentaram música. As duas primeiras imagens são capturas de Daniel no Windows. A terceira é uma cena do código atual. As regras e as telas também passaram por testes automatizados, além das partidas no Windows.

### 7. Demonstração do jogo

Agora vamos abrir o jogo e mostrar a corrida. Durante a partida, apontamos a coleta, o impacto, as camadas do fundo, a troca de poses e os efeitos. Pausamos uma vez, mostramos o áudio e retomamos. No resultado, mostramos reinício ou retorno ao menu. As escolhas de tema, corrida lateral, obstáculos e itens foram coletivas, de Daniel, John e Lucas. Daniel fez os testes no Windows. ChatGPT/Codex geraram grande parte do código e apoiaram os materiais, conforme registrado no projeto. A música é de HorrorPen, com licença CC BY 3.0. Usamos o enunciado e Python/Pygame, sem reutilizar código dos três jogos sugeridos pelo professor.

## Ensaio

Deixar o jogo aberto, conferir música e F11 e ensaiar no computador escolhido. Mostrar corrida, salto, coleta, impacto, painel, pausa, Áudio e resultado/reinício. Apontar as três técnicas ao vivo. Se um efeito não aparecer na partida, usar a imagem do slide. Não é necessário vencer e perder na mesma demonstração curta.

As duas primeiras imagens de evolução são capturas de Daniel no Windows. A terceira e as cenas atuais são preparadas pelo renderizador, com essa origem registrada; não apresentar como partidas humanas completas.

A concepção é coletiva dos três integrantes, conforme relato de Daniel; os testes Windows têm registros dele. ChatGPT/Codex geraram grande parte da implementação e apoiaram os materiais. O registro completo permanece em `06-fontes-e-ia.md`. A seção 11 não autoriza expressamente geração ampla de código; confirmar esse alcance com o professor mantendo a declaração do uso real.
