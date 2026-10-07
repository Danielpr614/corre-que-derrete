# Cliente frontal e música de fundo — 07/10/2026

## Desenho do cliente

A captura enviada pelo usuário mostrou um único olho deslocado e boca irregular na ilustração de vitória. `draw_customer` em `game/animation.py` agora desenha dois olhos na mesma altura, simétricos em relação ao centro do rosto. Contorno claro e pupilas escuras contrastam com a pele; o sorriso é uma linha poligonal simples e centralizada. A mesma função atende chegada e ilustração da vitória. Não houve alteração nos quadros do entregador de perfil, hitboxes ou física.

## Música e origem

Recurso: `assets/audio/house_in_a_forest_loop.ogg`, **House In a Forest Loop**, **HorrorPen**, copyright 2012, **Creative Commons Attribution 3.0**. A declaração específica foi consultada no README de `2d/dodge_the_creeps` do repositório `godotengine/godot-demo-projects`, commit `3e08537616661a5883831628decab4c526260289`. O arquivo foi obtido dessa cópia, sem alterar seu conteúdo. A página original OpenGameArt é indicada pela declaração e não foi consultada nesta sessão. Links, hash, condições e atribuição estão em [créditos](../assets/audio/CREDITOS.md). A licença MIT do código Godot não foi usada como licença da música. Nenhum código, desenho ou fonte do demo foi copiado.

A faixa foi escolhida como fundo instrumental para a corrida. Não houve audição humana na nuvem: adequação musical, transição do loop e volume percebido devem ser avaliados no computador. Não foram adicionados efeitos sonoros nem dependências; Pygame 2.6.1 fornece o mixer.

## Módulos e controles

`game/audio.py` encapsula inicialização, volume, reprodução e preferências. Na entrada, `App` inicializa o áudio uma vez; `pygame.mixer.music.play(loops=-1)` mantém a repetição. Estados e reinícios não chamam play novamente. Inicialmente ligada a 15%, a música usa a preferência salva quando existente. Desligar chama pause; ligar chama unpause, preservando a posição. A pausa do jogo mantém a música tocando.

`game/app.py` disponibiliza Áudio no menu e na pausa. Na tela Áudio: Enter/Espaço liga ou desliga; setas esquerda/direita ajustam 5 pontos percentuais entre 0% e 100%; Esc volta à origem. A simulação só atualiza no estado playing, portanto abrir Áudio pela pausa congela movimento, conservação, partículas e animação, e sair retorna à pausa. F11 continua tratado pela janela.

`game/graphics.py` desenha estado, volume, barra, controles, crédito e avisos. Os menus com quatro opções usam espaçamento ajustado; resultado permanece com três. Fontes e desenhos continuam rasterizados na resolução nativa, mantendo 16:9.

Preferências: `.local/audio.json`, ignorado pelo Git; leitura validada e escrita por arquivo temporário com substituição. Sem permissão de escrita, a sessão continua e há aviso. Sem dispositivo ou arquivo musical acessível, o jogo funciona sem música. Caminhos partem da localização do módulo, não de caminhos pessoais ou do diretório atual do terminal.

## Verificações realizadas na nuvem

Ambiente: Python 3.12.14, Pygame 2.6.1, drivers SDL dummy. Nenhuma instalação adicional nesta sessão.

- `python -m unittest discover -s tests -q`: **59 testes passaram**, incluindo 11 novos de áudio. Verificados controles de teclado, limites, retorno à origem, congelamento da simulação, persistência, preferências inválidas, falhas de inicialização/carregamento/escrita e ausência de reinício da música entre telas. Ogg real carregado e reproduzido, pausado e retomado pelo mixer dummy.
- Reprodução dummy permaneceu ativa após 28 segundos, além dos aproximadamente 25,17 segundos decodificados da faixa; verificação de repetição sem audição.
- Inicialização por cinco quadros sem tela, incluindo execução a partir de outra pasta, concluída sem erro.
- Renderização e limites de textos dos menus de quatro opções e da tela Áudio, aberta por menu e pausa, em 960 × 540, 1920 × 1080, 800 × 600 e 600 × 900.
- Inspeção visual de imagens preparadas de chegada e vitória em 960 × 540 e 1920 × 1080, detalhe ampliado do rosto e tela Áudio Full HD. Dois olhos e sorriso central visíveis; entregador preservado de perfil. São estados preparados para inspeção, não capturas de partida humana.

A suíte inclui os testes anteriores de redimensionamento/F11 e independência da física. Full HD foi uma superfície renderizada na nuvem; não equivale a uma janela interativa ou tela cheia no monitor do usuário.

## Validação pendente no Windows

Verificar o rosto na chegada e na vitória em janela e F11; legibilidade e layout dos menus; ouvir a faixa, o loop e o volume inicial; ligar/desligar e ajustar volume; fechar/reabrir para conferir preferências; abrir Áudio durante a pausa e confirmar que a corrida permanece congelada. Testar o dispositivo real e a fluidez com música. A captura fornecida evidencia o problema anterior do rosto; não confirma a correção ou o áudio desta versão.
