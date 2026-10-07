# Renderização nativa e acabamento Full HD

Data: 07/10/2026. Revisão do acabamento solicitada após relato de imagem e textos esticados em janela ampliada/tela cheia. Não foi recebida confirmação de execução desta revisão no Windows.

## Causa identificada no código

`Window` criava uma superfície fixa de 960 × 540, e `present()` usava `pygame.transform.smoothscale` para ampliá-la. Fontes eram rasterizadas em tamanhos de 23/27/40/64 pixels nessa superfície; quadros do entregador eram imagens de 82 × 88; fundos tinham altura de 540. Em 1920 × 1080, cada dimensão dobrava, incluindo todos os pixels dessas fontes e imagens. A interpolação suavizava a ampliação, sem acrescentar informação original.

O problema estava na arquitetura de rasterização, não nas coordenadas físicas ou no cálculo da área 16:9. Trocar somente o filtro não resolveria a falta de detalhe da fonte.

## Arquitetura atual

1. `window.py` continua calculando a área 16:9 centralizada, com margens e os mesmos eventos de redimensionamento/F11. `prepare_frame()` cria/reaproveita uma superfície do tamanho dessa área. Em Full HD, ela é 1920 × 1080.
2. `app.py` pede essa superfície antes do desenho e chama `Renderer.resize()`.
3. `graphics.py` mantém layout em coordenadas de referência 960 × 540, mas rasteriza texto diretamente com fontes do tamanho correspondente ao destino. O fator é `largura_do_destino / 960`.
4. `drawing.py` converte coordenadas, raios e espessuras das primitivas para pixels reais. Circulares/poligonais em superfícies opacas usam antialiasing do `pygame.gfxdraw`, que pertence ao pacote Pygame já utilizado.
5. Quadros e camadas são regenerados por geometria quando a resolução muda, ficando em cache durante os quadros seguintes. Nuvens e sprites usam fonte construída a 2× a resolução de destino e redução única para suavizar bordas transparentes. Isso é redução de um recurso mais detalhado, não ampliação das imagens antigas.
6. `Window.present()` apenas limpa as margens e copia a imagem nativa com `blit`; não usa `scale` ou `smoothscale` na cena final.

| Elemento | Antes | Em Full HD agora |
| --- | --- | --- |
| Superfície da cena | 960 × 540 ampliada | 1920 × 1080, copiada diretamente |
| Fonte pequena | 23 pixels ampliados | Fonte rasterizada em 46 pixels |
| Título | 64 pixels ampliados | Fonte rasterizada em 128 pixels |
| Quadro do entregador | 82 × 88 ampliado | 164 × 176, gerado de geometria em resolução maior |
| Altura das camadas | 540 pixels ampliados | 1080 pixels gerados no tamanho atual |
| Partículas/primitivas | Desenhadas pequenas e ampliadas | Desenhadas na resolução de destino |

Os números de fonte representam o tamanho solicitado ao Pygame; altura visível do glifo depende das métricas da fonte. Layouts lógicos e limites físicos de texto são conferidos separadamente pelos testes.

## Física e técnicas preservadas

Não houve alteração em `settings.py`, `entities.py`, `run.py` ou nas funções de controles. Posição, gravidade, salto, distância, velocidade, hitboxes, conservação, pontuação e dificuldade continuam em unidades lógicas. `drawing.py` não participa da detecção de colisões.

Parallax mantém fatores 0,15/0,35/0,70, com deslocamento gráfico convertido para pixels atuais. Corrida continua em seis quadros a 10 quadros/s e salto com poses por velocidade vertical. Partículas continuam em coordenadas de mundo, com a mesma vida, emissão e limite; o fator de resolução é aplicado apenas ao desenho.

Pausa e resultado continuam congelando os efeitos e o tempo da animação. Redimensionar ou desenhar não atualiza a simulação. A regeneração de recursos custa processamento durante a mudança de resolução; possíveis pausas e desempenho precisam ser observados no computador. Não houve medição de FPS nesta sessão.

## Acabamento e origem dos recursos

Estilo 2D simples com paleta compartilhada. Acrescentados capacete com brilho/tira, detalhes faciais, uniforme e mochila com costuras e símbolo; reflexo e faceta no gelo; sombras, faixa e lado escuro no cone; luz, lateral e etiqueta na caixa; gradiente de céu, detalhes de telhados, reflexos em vitrines, vasos e divisões da calçada; detalhes de roupa/cabelo/calçados do cliente e da porta do destino; sombras sob os painéis.

Tudo foi desenhado no código nesta implementação com apoio de ChatGPT/Codex. Não foram adicionados imagens externas, arquivos de fonte, sons, bibliotecas ou arte gerada por ferramenta de imagens. Fonte padrão do Pygame preservada. `pygame.gfxdraw` é um módulo da dependência já fixada em 2.6.1. Créditos da biblioteca e declaração de IA estão no registro 06.

## Verificações realizadas

Ambiente existente na nuvem: Linux, Python 3.12.14, Pygame 2.6.1 e SDL dummy. Nenhuma nova instalação de dependências ou teste interativo Windows nesta sessão.

- A primeira execução da suíte acusou pressupostos antigos nos testes da janela: existência de `window.scaled` e superfície obrigatoriamente 960 × 540. Esses testes foram migrados para verificar superfície nativa, limites físicos e lógicos e margens, mantendo os casos de proporção, estado e modos. Os 44 testes passaram após a adaptação.
- Adicionados quatro testes em `tests/test_resolution.py`; suíte final com **48 testes passou**. Verificam tamanho nativo de fontes/quadros/camadas, apresentação sem reamostragem, reaproveitamento/regeneração dos caches e ausência de alterações em física/efeitos ao desenhar em diferentes tamanhos.
- A apresentação em Full HD foi testada com uma linha de um pixel e chamadas de escala bloqueadas: linha e pixel vizinho permaneceram distintos. Isso comprova cópia sem interpolação, não é uma avaliação subjetiva de toda a arte.
- Continuam os testes de oito tamanhos da interface, incluindo Full HD, 4:3 e retrato; controles, salto, colisões, pausa/reinício, rota completa, parallax, quadros e partículas permanecem cobertos.
- Executado o comando de entrada por cinco quadros com SDL dummy, sem erro.
- Geradas e inspecionadas imagens nativas 1920 × 1080 de menu, corrida e vitória. Encontradas franjas nas bordas transparentes com antialiasing de `gfxdraw`; corrigidas evitando esse caminho em superfícies com alpha e construindo sprites/nuvens em resolução maior para reduzir uma vez. Suíte de 48 testes repetida depois da correção e nova imagem de corrida inspecionada.

Imagens intermediárias em `work/`, ignoradas pelo Git. Foram compostas com estados/valores preparados para inspeção; não são capturas de partida humana nem teste de tela cheia no Windows. Fontes/layout mostraram-se legíveis e sem cortes nas amostras. Nitidez percebida no monitor, escala DPI do sistema, fluidez e memória não foram medidos pela inspeção na nuvem.

## Validação no computador

Atualizar a branch `work`/ZIP. Comparar menu, instruções, HUD, corrida e resultados em 960 × 540, janela maximizada e Full HD com F11; conferir acentos, contornos, proporção e margens. Observar quadros e partículas em movimento, encaixe visual das colisões e o cliente na chegada. Testar redimensionamento repetido, retorno de F11, pausa durante salto/efeitos e reinício.

Registrar possíveis pausas durante regeneração de recursos, FPS e consumo de memória. Se o Windows estiver com escala de tela 125% ou 150%, conferir o resultado nessa configuração também; não foi configurada nem testada a política DPI do Windows na nuvem. Janelas muito pequenas continuam reduzindo legibilidade por falta de espaço físico.

Commit separado: `fix: renderiza em resolucao nativa e refina arte`. Envio normal para `work` autorizado pelo usuário, com confirmação ao fim da sessão, preservando os marcos anteriores.
