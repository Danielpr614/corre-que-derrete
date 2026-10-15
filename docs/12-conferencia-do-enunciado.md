# Conferência do enunciado e da entrega

## Complemento de autoria e apresentação em 15 de outubro

Daniel informou nesta data que a escolha do tema, da corrida lateral, dos obstáculos e dos itens foi coletiva: Daniel Pena, John Lucas e Lucas Oliveira. O registro da equipe passa a incluir essa contribuição dos três, mantendo os testes Windows atribuídos a Daniel e a assistência à implementação atribuída a ChatGPT/Codex. As passagens abaixo sobre contribuições ainda não informadas descrevem o estado anterior a esse relato.

A apresentação foi reescrita com os três integrantes, explicações curtas e um guia de fala. Os arquivos e as imagens selecionadas ficam em `presentation/`. A instalação automatizada e os 59 testes da revisão anterior continuam registrados, sem serem descritos como testes humanos. O ensaio no computador da avaliação e a confirmação do alcance do uso de IA com o professor continuam necessários.


Revisão em **15/10/2026**, para a entrega de 16/10/2026. Equipe: **Daniel Pena, John Lucas e Lucas Oliveira**. Professor: Pedro Cândido. Turma: 7º período de Engenharia da Computação.

Foi lido integralmente o documento **Projeto Avaliativo Desenvolvimento de Jogo 2D com Python e Pygame**, incluindo suas tabelas, rubrica e checklist. O arquivo reenviado tem SHA-256 `d7c83ddf74fc618f8ad39602be742100113848f0ea76a9e3c5b2a48b413e0918`, igual ao enunciado conferido em 07/10. A base do código é a branch `work` em `19c5778`, com implementação do último marco funcional `23f755e`.

**Resultado:** o código apresenta os requisitos funcionais solicitados e passou pelos 59 testes automatizados desta revisão. A apresentação e o registro de contribuições foram atualizados. Restam a conferência do acesso público, o ensaio da equipe e a confirmação com o professor sobre o alcance da geração de código por IA. Este relatório não atribui nota nem declara concluída uma defesa que ainda não ocorreu.

## Proposta e objetivos das seções 1 a 3

O jogo é uma corrida lateral curta para colegas e jogadores iniciantes. O entregador avança sozinho, salta cones e caixas e coleta gelo para conservar o sorvete até o destino. A barra conecta o tema ao tempo e aos impactos. Uma rota de três trechos limita o escopo sem eliminar início, objetivo, desafio, conclusão e reinício.

Os conceitos de tempo, coordenadas, composição, movimento, animação, colisões e interface aparecem no código e são explicados no [manual técnico](13-organizacao-e-tecnicas.md). Os objetivos de aprendizagem também dependem da compreensão de cada integrante. Ter os recursos implementados não demonstra, por si só, domínio na exposição oral.

## Requisitos obrigatórios da seção 4

| Requisito | Evidência no projeto | Situação |
| --- | --- | --- |
| Python 3 e Pygame | `main.py` e `requirements.txt`, com `pygame==2.6.1` | Conferido; biblioteca padrão nos demais módulos |
| Loop e controle de tempo | `game/app.py:main`, `App.update`, `Clock.tick`, passo fixo de 1/60 s | Implementado e testado |
| Menu, partida, pausa/instruções, resultado, reinício e saída | `App.handle_event`, `activate`, `start` e estados do renderizador | Implementados; testes de regras, interface e áudio |
| Interação e feedback | Teclado, instruções, avisos, partículas, piscar e barra | Implementados; relato de uso no Windows por Daniel |
| Objetivo, desafio e resultado | `Run.update`: conservação, gelo, obstáculos e chegada | Implementados; testes incluem vitória, derrota e rota completável |
| Colisões explicáveis | `Player.rect`, `WorldObject.rect` e `colliderect` | AABB por retângulos; não é colisão pela silhueta |
| Pelo menos três técnicas gráficas | `Parallax`, `CourierAnimation` e `Effects` | Parallax, animação por quadros e partículas implementados |
| HUD | `Renderer.hud`: conservação, distância, trecho, pontos, gelos e impactos | Implementado; conservação com vírgula e uma casa decimal |
| Progressão | `Run.stage/speed` e `build_route` | Três trechos com maior velocidade e obstáculos mais próximos |
| Estabilidade no computador da avaliação | Caches, controle de tempo, limite de partículas e testes simulados | Parcial: precisa de ensaio no equipamento escolhido; sem FPS real medido |
| Código organizado | Módulos em `game/`, constantes e testes separados | Conferido; orientação a objetos não é obrigação do enunciado |
| Reprodução documentada | README com versões, comandos, controles e estrutura | Instalação limpa refeita nesta revisão; ensaio humano final ainda necessário |

Os três trechos pertencem à mesma rota, não são três mapas. O áudio melhora a experiência, mas não é contado como uma das três técnicas de Computação Gráfica.

## Referências e autoria das seções 5 e 11

A seção 5 condiciona as exigências de transformação ao uso de uma base existente. O projeto não adaptou o código dos três jogos indicados pelo professor. Portanto, não há uma base a ser apresentada como transformada. Os links continuam registrados como referências indicadas, sem afirmar estudo que não foi relatado.

A arte é construída por primitivas do Pygame no próprio código, com assistência de IA. A música externa é **House In a Forest Loop**, de **HorrorPen**, sob **CC BY 3.0**. O arquivo, o autor, a fonte e a licença estão em [créditos musicais](../assets/audio/CREDITOS.md). Python, Pygame, a fonte distribuída com o pacote e ChatGPT/Codex também constam dos créditos. A licença da música não se confunde com a do código do projeto, para o qual não foi escolhida uma licença geral.

O [registro de fontes e IA](06-fontes-e-ia.md) informa ferramenta, finalidade, partes afetadas e validação por etapa. Houve apoio amplo de ChatGPT/Codex à implementação, aos desenhos por código, aos testes e à documentação. A revisão de redação mantém essa declaração. Daniel forneceu decisões e testes no Windows; a concepção coletiva dos três integrantes foi informada por Daniel nesta revisão. Não se atribui programação ou validação a uma pessoa apenas por ela integrar a equipe.

O enunciado permite apoio de IA conforme as regras da disciplina e responsabiliza cada integrante por compreender o conteúdo. A autorização verbal relatada por Daniel não substitui os créditos e a explicação do código. A seção também trata de cópia não declarada e de omissão de fontes. A entrega não deve apresentar implementação assistida como programação humana exclusiva.

## Etapas da seção 6

| Etapa | Registro existente | Situação atual |
| --- | --- | --- |
| Concepção | `bf1db57`, documentos 01 a 04: tema, público, regras, esboços e fluxo | Marco preservado; tarefas iniciais eram propostas, não uma divisão já executada |
| Protótipo | `2ef4366`, diário e relatório 07 | Movimento, interação, colisões e formas provisórias registrados |
| Intermediária | `52fb13f`, `9c21d5f`, `26d723c` e `23f755e` | Interface, técnicas, nitidez, correções e música registrados |
| Final | Código atual e revisão documental de 15/10 | Slides e contribuições atualizados; ensaio e cópia de segurança pendentes |

Os marcos de implementação listados são de 07/10/2026. Não representam dias diferentes de trabalho. O histórico e o diário são evidências da evolução; os registros antigos foram mantidos com o contexto da época.

## Entregáveis da seção 7

| Entregável | O que existe | Pendência para o envio |
| --- | --- | --- |
| Código-fonte | `main.py`, `game/`, `assets/` e `tests/` completos | Conferir que o link e o ZIP abrem a versão correta |
| README | Objetivo, instalação, execução, regras, controles, estrutura, créditos e limites | Conferir acesso público e execução no computador da avaliação |
| Dependências | `requirements.txt`, com Pygame 2.6.1 | Instalação limpa concluída em 15/10 |
| PPTX ou PDF | PPTX e PDF de 15/10 em `presentation/` | Ensaiar as falas e a demonstração |
| Créditos | README, documento 06 e créditos junto da faixa | Manter atribuições no pacote final |
| Evolução e tarefas | Commits, diário e documento 14 | Concepção coletiva e testes Windows registrados; capturas selecionadas em `presentation/evidencias/` |
| Demonstração | Jogo executável com Python, relatos Windows e testes | Ensaiar no equipamento da avaliação e preparar cópia offline; vídeo curto recomendado |

O texto não exige um `.exe` autônomo. O comando `python main.py`, com as dependências instaladas, executa o jogo. O vídeo é recomendado como segurança; não substitui a demonstração em execução nem é descrito como obrigação absoluta.

## Estrutura mínima da apresentação da seção 8

A apresentação em `presentation/` cobre os onze itens abaixo:

1. Nome do jogo, três integrantes, gênero, público e objetivo.
2. Problema de projeto, conceito inicial e esboço ou fluxo.
3. Fontes realmente utilizadas e o que foi estudado ou reutilizado. Distinguir referências indicadas de conteúdos consultados.
4. Regras, controles, ciclo da partida e diagrama dos estados.
5. Principais módulos e suas responsabilidades.
6. Implementação de pelo menos três técnicas gráficas, com exemplos visuais.
7. Movimento, animação, colisão, câmera, camadas, HUD e progressão.
8. Capturas de versões intermediárias comparadas ao resultado atual.
9. Problemas reais, testes e soluções adotadas.
10. Demonstração ao vivo e análise breve do resultado.
11. Contribuições reais, créditos e declaração de IA.

O professor recomenda **10 a 15 minutos de exposição, seguidos de perguntas e demonstração**. Se aceitar a demonstração dentro do tempo, adaptar a distribuição sem suprimir as explicações. Todos os integrantes devem participar e saber explicar o código. O roteiro em Markdown acompanha o PPTX/PDF de 15/10 e não o substitui.

## Rubrica das seções 9 e 10

| Critério | Pontos | Evidência e atenção na avaliação |
| --- | --- | --- |
| Concepção e planejamento | 2 | Conceito, regras, esboço, fontes e marcos dos documentos 01 a 04 |
| Funcionamento e mecânicas | 5 | Loop, estados, salto, coleta, impacto, resultado, reinício e progressão demonstráveis |
| Computação Gráfica | 6 | Parallax, quadros e partículas, com explicação de como funcionam |
| Design e experiência | 3 | Legibilidade, HUD, feedback, consistência e acabamento |
| Qualidade do código | 4 | Responsabilidades dos módulos, constantes, caminhos e organização explicáveis |
| Estabilidade e testes | 2 | Instalação reproduzível, testes e ensaio no computador da avaliação |
| Documentação da construção | 3 | Slides, capturas, decisões, dificuldades, evolução e contribuições |
| Apresentação e defesa | 4 | Participação dos três integrantes, demonstração e respostas consistentes |
| Originalidade e fontes | 1 | Identidade e mecânica próprias, créditos e transparência sobre IA |
| **Total** | **30** | A soma define a rubrica, não uma nota já obtida |

A seção 10 classifica cada critério como excelente (90 a 100%), adequado (70 a 89%), parcial (40 a 69%) ou insuficiente (0 a 39%). A implementação não garante a faixa: evidência, explicação e avaliação do professor também contam. Computação Gráfica vale 6 pontos e defesa vale 4, por isso jogar durante toda a exposição não atende à finalidade da apresentação técnica.

## Verificações executadas em 15 de outubro

- Conferidos os hashes de todos os arquivos do ZIP anterior contra a árvore atual de `work`: nenhuma divergência.
- Criado ambiente virtual novo com Python **3.12.14** e instalado `requirements.txt`, com Pygame **2.6.1**.
- `python -m unittest discover -s tests -q`: **59 testes passaram**. As suítes cobrem regras, estados, interface, técnicas gráficas, resolução e áudio com SDL dummy.
- `python -m pip check`: nenhuma dependência quebrada.
- `main.py --smoke-frames 5`, com drivers dummy e chamado a partir de outra pasta: encerrou sem erro. Isso confere inicialização e resolução de caminhos.
- Conferidos caminhos do código, recursos, árvore de arquivos e créditos. Não foram encontrados segredos, caminhos pessoais ou dependências extras no código revisado.

Não houve nova partida humana, audição ou medição de FPS nesta revisão. A confirmação anterior de Daniel sobre visual e áudio no Windows continua válida para aquele teste. Os resultados automáticos não provam desempenho no notebook do professor.

## Checklist e condições das seções 12 e 13

| Verificação | Situação |
| --- | --- |
| Abre com o comando do README | Inicialização automatizada confirmada; Windows relatado anteriormente |
| Objetivo, controles e regras visíveis | Presentes no jogo e no README |
| Iniciar, concluir/perder e reiniciar sem editar | Implementado e coberto por testes |
| Colisões e limites testados | Suítes de regras e interface/resolução |
| Caminhos portáveis e recursos no pacote | Caminhos baseados no módulo, Ogg incluído e entrada testada fora da pasta |
| Dependências em ambiente limpo | Refeito nesta revisão |
| Ausência de segredos e temporários no pacote | Código conferido; excluir ambientes virtuais, caches e preferências ao empacotar |
| Apresentação com evolução e técnicas | Nova versão em `presentation/`, com os três integrantes e imagens de evolução |
| Contribuições e IA declaradas | IA, decisões coletivas dos três integrantes e testes Windows de Daniel registrados |
| Fontes creditadas | Créditos presentes; manter na redistribuição |
| Segurança | Preparar cópia offline e, preferencialmente, vídeo curto da versão final |

A seção 12 prevê versão de segurança se o jogo não abrir, avaliação apenas dos recursos demonstráveis, possível diferenciação da nota individual e necessidade de autorização para correções após a entrega. O grupo ainda precisa ensaiar e confirmar o funcionamento na máquina da avaliação.

## Referências e acesso da seção 14

As referências listadas pelo professor estão preservadas no documento 06. Não é obrigatório adaptar um dos jogos indicados e não houve reutilização do código deles. As fontes efetivas e os recursos utilizados estão separados dessas indicações.

Na consulta inicial de 15/10, o repositório estava **privado**, com `main` em `aaab7cc` e o jogo completo em `work`. Nesta revisão, a versão documental conferida será enviada a `work` e encaminhada à branch principal preservando o histórico. A visibilidade pública, solicitada por orientação adicional relatada por Daniel, precisa ser alterada nas configurações do GitHub e conferida sem login. Não há comando de alteração de visibilidade disponível na conexão usada nesta revisão.

Slides, capturas e contribuições foram organizados nesta revisão. A ordem de fechamento é: confirmar o alcance permitido do uso de IA, testar o link público da versão correta, ensaiar e guardar a cópia de segurança. Os campos pendentes só devem ser marcados como concluídos depois de executados.
