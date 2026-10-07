# Conferência do enunciado e pendências de entrega

Revisão em 07/10/2026 sobre a implementação `23f755e`. Fonte relida: **Projeto Avaliativo — Desenvolvimento de Jogo 2D com Python e Pygame, 30 pontos**, professor Pedro Cândido, DOCX anexado pelo usuário. SHA-256 do arquivo: `d7c83ddf74fc618f8ad39602be742100113848f0ea76a9e3c5b2a48b413e0918`. O documento está disponível nesta conversa; não foi necessário solicitar outra cópia. Não foi incorporado ao repositório.

Esta conferência relaciona exigências acadêmicas ao código e aos registros. Não atribui nota nem comprova domínio na defesa oral. **Os requisitos funcionais estão implementados; a entrega acadêmica completa ainda tem pendências.**

## Requisitos obrigatórios — seção 4

| Requisito | Implementação e evidência | Situação / limite |
| --- | --- | --- |
| Tecnologia: Python 3 e Pygame | `main.py`, `requirements.txt`: Pygame 2.6.1; biblioteca padrão para os demais módulos. Python 3.12.14 na nuvem; usuário informou Python 3.13.7 no Windows anteriormente. | Implementado. Versão de Pygame instalada no Windows não foi informada. |
| Ciclo: eventos, atualização, renderização, tempo | `game/app.py:main`, `App.update`; `Clock.tick(60)`, eventos, passo fixo 1/60 s, desenho e apresentação. | Implementado; explicado no relatório 13. 60 FPS é alvo, não medição. |
| Estados e reinício/saída | `App.handle_event`, `activate`, `start`: menu, instruções, corrida, pausa, resultado de vitória/derrota, áudio; reiniciar, menu e sair. | Implementado. Testes em `tests/test_rules.py` e `test_audio.py`; capturas do protótipo recebidas na conversa. |
| Interação e feedback | Espaço/seta para cima, menus por teclado, instruções visíveis; flashes, avisos e partículas em `graphics.py` e `particles.py`. | Implementado. Controles do protótipo confirmados no Windows; confirmação atual é de visual e áudio satisfatórios, sem checklist individual. |
| Objetivo, regras, desafio e conclusão | `Run.update`: conservação, cones/caixas, gelo, derretimento e resultado; README e instruções. | Implementado. Vitória e derrota do protótipo documentadas pelo usuário; balanceamento humano não foi medido. |
| Colisões e resposta explicável | `Player.rect`, `WorldObject.rect`, `Run.update`: AABB com `colliderect`, consumo único, proteção e chão. | Implementado e testado; método e limites no relatório 13. |
| Pelo menos três técnicas gráficas | `Parallax`, `CourierAnimation`, `Effects`: camadas com velocidades diferentes, quadros e partículas. | As três estão implementadas; exigem explicação/demonstração pelo estudante. Há também câmera, transformações e composição. |
| HUD/painel | `Renderer.hud`: conservação, distância, trecho, pontuação, gelos, impactos e avisos. | Implementado; conservação com uma casa decimal e vírgula no HUD/resultado. |
| Progressão | `Run.stage/speed`, `build_route`: três trechos, velocidade 260/300/340 e intervalos 1200/950/650 nas sequências de obstáculos. | Implementado; não são três mapas independentes. |
| Desempenho estável no computador de demonstração | Cache de quadros/cenário e limite de 100 partículas; testes SDL dummy; relato atual de visual/áudio satisfatórios no Windows. | Evidência parcial: sem FPS medido, duração de teste ou identificação do computador da avaliação. Fazer ensaio nesse computador, especialmente F11/redimensionamento. |
| Organização coerente | Módulos por responsabilidade em `game/`, testes separados, constantes em `settings.py`. | Implementado; documentação no relatório 13. Não se exige orientação a objetos. |
| Reprodução com README e dependências | Comandos Windows/VS Code, ambiente, controles e estrutura no README; instalação limpa na nuvem registrada no relatório 07. | Documentado e executável com Python. Última versão foi testada no Windows segundo o usuário; procedimento de instalação limpa dessa versão no computador da avaliação não foi relatado. |

## Proposta, aprendizagem, autoria e referências — seções 1–3, 5 e 11

O projeto tem início, objetivo, desafio, encerramento e reinício; o tema veio do usuário, e a implementação foi elaborada com apoio amplo de ChatGPT/Codex. É uma corrida lateral com conservação do sorvete, gelo e progressão, não uma base de jogo existente renomeada. Coordenadas, tempo, composição e interação estão explicados no relatório 13. A capacidade de explicá-los é responsabilidade de quem apresentar.

Não foi reutilizado código dos três repositórios de jogos indicados pelo professor. Seus links foram registrados como referências para estudo, sem afirmar leitura dos conteúdos. Se houver estudo posterior, registrar concretamente o que foi aprendido. O enunciado não obriga copiar ou usar uma dessas bases. As exigências de transformação de uma base existente na seção 5 são condicionais e não se aplicam como obrigação de adaptação fictícia.

Arte: primitivas próprias da implementação assistida, sem imagens externas. Fonte padrão e biblioteca Pygame creditadas. Música: HorrorPen, **House In a Forest Loop**, **CC BY 3.0**, Ogg incluído, origem e atribuição em [créditos musicais](../assets/audio/CREDITOS.md). A cópia Godot foi usada apenas para obter a faixa e verificar sua declaração de licença; nenhum código do demo foi adaptado. Fontes e IA: [registro completo](06-fontes-e-ia.md). Não existe uma licença geral escolhida para o código do projeto; isso não altera a licença da música.

Não apresentar o código como escrito exclusivamente pelo estudante. O uso de IA está declarado com finalidade, partes afetadas e verificação. Nomes, composição do grupo e contribuições individuais ainda não foram informados. Datas e turma estão em branco no enunciado. A defesa e a observância das regras da disciplina não podem ser substituídas pelos testes automatizados.

## Etapas e entregáveis — seções 6 e 7

| Item | Evidência atual | Pendência |
| --- | --- | --- |
| Concepção | Commit `bf1db57`; docs 01–04: tema, gênero, público, regras, esboços textuais, fluxo e tarefas propostas. | Identificação e divisão real das contribuições humanas. |
| Protótipo jogável | `2ef4366`; relatório 07 e diário: movimento, salto, colisões, recursos provisórios e 27 testes. | Nenhuma funcionalidade desse marco pendente. |
| Versão intermediária | `52fb13f`, `9c21d5f`, `26d723c`, `23f755e`; UI, técnicas, renderização e áudio. | Consolidar capturas reais para os slides. |
| Versão final | Código atual, README, créditos, matriz, manual técnico, evidências e roteiro. | Apresentação PPTX/PDF, identificação, ensaio e pacote de entrega. Este registro documental não declara encerrada a etapa 4. |
| Código-fonte completo | Arquivos rastreados pelo Git, módulos, dependência e Ogg. `work/`, `.venv/`, `.local/` e caches ignorados. | Gerar/conferir pacote final sem arquivos temporários; não incluir preferências pessoais. |
| README | Instalação, execução, regras, controles, estrutura, créditos e limitações revisados. | Conferir o comando no computador da avaliação. |
| Dependências | `pygame==2.6.1`; instalação limpa e `pip check` registrados no marco 2. | Registrar eventual instalação nova no computador de demonstração quando ocorrer. |
| Apresentação PPTX ou PDF | [Roteiro de 13 minutos](15-roteiro-apresentacao.md) com demonstração e conteúdo técnico. | O roteiro Markdown não substitui o arquivo PPTX/PDF exigido. Montar/exportar slides com capturas e identificação. |
| Créditos | README, docs 06, arquivo de créditos junto da música. | Preencher nomes e contribuições reais; preservar atribuição ao redistribuir. |
| Evolução/divisão de tarefas | [Índice de evidências](14-evidencias-e-evolucao.md), commits e diário. | Nomes e divisão efetiva; capturas da conversa não estão arquivadas no Git. |
| Demonstração | `python main.py` executável com Python/Pygame; relatos de execução no Windows. | Ensaio na máquina da avaliação e cópia de segurança; vídeo curto recomendado. Não há `.exe` autônomo. Se o professor exigir especificamente esse formato, esclarecer/empacotar; o enunciado não especifica formato binário. |

## Conteúdo da apresentação e rubrica — seções 8–10

O roteiro 15 cobre identificação, conceito, fontes, regras/estados, arquitetura, técnicas, movimento/colisão/câmera/HUD/progressão, evolução, dificuldades, testes, demonstração, créditos e IA. Inclui instruções para inserir contribuições reais e para todos os integrantes participarem. Perguntas e domínio técnico ainda dependem de preparação humana.

| Critério / pontos | Onde está a evidência | O que ainda depende da entrega/defesa |
| --- | --- | --- |
| Concepção e planejamento — 2 | Docs 01–04, marco 1 | Apresentar conceito e esboços; declarar referências realmente estudadas. |
| Funcionamento e mecânicas — 5 | Código, testes de regras, relatos Windows | Demonstração, justificativa das regras e equilíbrio. |
| Computação Gráfica — 6 | Módulos e relatório 13 | Explicação fundamentada das três técnicas. |
| Design e experiência — 3 | Interface, arte, feedback; confirmação atual do usuário | Mostrar legibilidade e consistência durante a demonstração. |
| Qualidade do código — 4 | Organização, constantes, caminhos e caches | Explicar responsabilidades e escolhas. |
| Estabilidade e testes — 2 | Relatórios 07–11 e testes existentes | Instalação/ensaio no computador de avaliação e evidência de estabilidade. |
| Documentação da construção — 3 | Diário, índice e roteiro | Slides PPTX/PDF, capturas e contribuições. |
| Apresentação e defesa — 4 | Roteiro proposto | Ensaio, participação, demonstração e respostas; ainda não realizados. |
| Originalidade e fontes — 1 | Registro de fontes/IA e créditos musicais | Identificação humana e transparência durante a defesa. |

Não estimar uma nota de 30 pontos: os níveis da seção 10 dependem das evidências e da avaliação do professor.

## Checklist e condições — seções 12 e 13

| Verificação do professor | Registro atual |
| --- | --- |
| Abre pelo comando do README | Entrada testada na nuvem; execução Windows relatada. Ensaio na máquina da avaliação pendente. |
| Objetivo/regras/controles visíveis | Jogo e README. |
| Iniciar, jogar, concluir/perder e reiniciar sem editar | Implementado e testado; vitória/derrota do protótipo relatadas. |
| Colisões/limites testados | Testes de regras, interface/resolução; não equivalem a checklist interativo atual no Windows. |
| Caminhos portáveis e recursos no pacote | Caminhos derivados do módulo; Ogg rastreado; execução a partir de outra pasta registrada. |
| Dependência em ambiente limpo | Evidência no relatório 07, sem alegar instalação nova nesta revisão. |
| Sem senhas/caminhos pessoais/temporários/dependências ocultas | Arquivos rastreados conferidos nesta revisão; apenas Pygame externo. Pacote final deve excluir diretórios ignorados. |
| Apresentação com intermediárias e técnicas | Roteiro e índice prontos; PPTX/PDF e capturas arquivadas pendentes. |
| Contribuições e IA declaradas | IA e contribuição conhecida do usuário registradas; identificação/divisão nominal pendente. |
| Recursos/códigos externos creditados | Pygame/Python/fonte, faixa e IA; nenhum código de jogo externo adaptado. |
| Cópia de segurança e vídeo | Ainda não preparados como entregáveis; vídeo recomendado, não obrigação absoluta. |

Para a avaliação, preparar uma cópia offline e, preferencialmente, vídeo. Recurso futuro não recebe evidência de implementação; a nota pode ser individualizada em equipe. Se houver correção após a entrega formal, a seção 12 exige autorização do professor e registro da mudança. Não há notícia de entrega formal realizada nesta conversa.

## Ordem sugerida para finalizar

1. Preencher nomes, turma, datas e contribuições reais; revisar entendimento do código.
2. Montar PPTX/PDF a partir do roteiro, incluindo capturas reais e comparação das etapas.
3. Ensaiar no computador da avaliação, registrar ambiente e estabilidade; preparar demonstração e respostas.
4. Conferir pacote final com código, dependência, Ogg e créditos; guardar cópia offline e gravar vídeo curto de segurança.
