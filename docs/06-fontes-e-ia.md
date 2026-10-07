# Fontes, créditos e apoio de IA

Registro iniciado em 07/10/2026. Diferenciar fonte lida, referência indicada e material efetivamente reutilizado.

## Fontes usadas nesta etapa

| Fonte | Autor/origem | Uso efetivo | Link/licença |
| --- | --- | --- | --- |
| Projeto Avaliativo — Desenvolvimento de Jogo 2D com Python e Pygame, 30 pontos | Professor Pedro Cândido; DOCX fornecido pelo usuário | Leitura e extração dos requisitos para planejamento | Arquivo `Projeto_Avaliativo_Jogo_2D_Python_Pygame_30_Pontos.docx`; sem URL ou licença informada |
| Ideia de “Corre que Derrete!” | Usuário desta conversa | Tema e mecânica inicial de entregador, sorvete, obstáculos e itens | Solicitação nesta conversa; sem identificação nominal informada |

O enunciado informa acesso às referências em 25/09/2026. Essa data pertence ao documento do professor e não comprova consulta dos links pelo estudante ou pela IA nesta sessão.

## Referências indicadas para estudo posterior

Os links abaixo foram lidos no enunciado, mas os conteúdos externos não foram consultados nesta etapa. Não há código copiado ou adaptado deles. Autor e licença de qualquer material efetivamente utilizado deverão ser verificados na ocasião.

| Referência | Link | Estudo futuro proposto |
| --- | --- | --- |
| Python Games — conta itspyguru | https://github.com/itspyguru/Python-Games | Comparar exemplos de movimento e rolagem |
| Pygame Simple Examples — conta Leonardpepa | https://github.com/Leonardpepa/pygame-simple-examples | Estudar eventos, laço e colisões em exemplos pequenos |
| Python Games Collection — conta veddegre | https://github.com/veddegre/python-games-collection | Observar organização, menus e reprodução |
| Documentação oficial do Pygame | https://www.pygame.org/docs/ | Confirmar APIs de eventos, tempo, superfícies, retângulos e transparência |
| GitHub Docs — licenças | https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository | Verificar permissões antes de reutilizar código |

Não escolher uma base pronta apenas para trocar imagens. Se houver adaptação futura, registrar arquivo/trecho de origem, alterações, motivo, licença e partes desenvolvidas pelo estudante/equipe.

## Declaração de IA — etapa 1

- **Ferramenta:** ChatGPT/Codex, da OpenAI (https://openai.com/chatgpt/). Não foi registrada uma versão específica do modelo.
- **Data:** 07/10/2026.
- **Finalidade:** apoiar a leitura do enunciado, reduzir o escopo, propor regras e técnicas gráficas, organizar documentação e explicar a proposta em português brasileiro.
- **Partes afetadas:** atualização de `README.md` e redação de `docs/01-concepcao.md`, `02-telas-e-graficos.md`, `03-requisitos.md`, `04-plano-de-etapas.md`, `05-diario.md` e deste arquivo.
- **Origem da ideia:** usuário; os detalhes de escopo, números iniciais, esboços, organização e verificações foram elaborados com apoio de IA nesta sessão.
- **Validação efetivamente realizada:** confronto documental da proposta com o texto do anexo e conferência da estrutura existente. As regras numéricas e as soluções técnicas ainda não foram validadas em execução.
- **Validação humana pendente:** estudante deve revisar as decisões, compreender as técnicas e, nas etapas seguintes, validar o código e registrar resultados observados. Não há aprovação humana da proposta registrada neste momento.
- **Limites:** nenhum código de jogo ou recurso visual final foi gerado; não foram realizados testes de jogabilidade nem inventados resultados, contribuições ou dificuldades de implementação.

## Atualização — IA e biblioteca na etapa 2

Data: 07/10/2026. Ferramenta: ChatGPT/Codex, da OpenAI; sem versão específica registrada.

**Finalidade:** implementar o protótipo autorizado pelo usuário, escrever verificações automatizadas e atualizar instruções/documentação. O código foi elaborado nesta sessão com apoio de IA; não foi copiado de um jogo de referência.

**Partes afetadas:** `main.py`, `game/__init__.py`, `game/settings.py`, `game/entities.py`, `game/run.py`, `game/app.py`, `game/graphics.py`, `tests/__init__.py`, `tests/test_rules.py`, `.gitignore`, `requirements.txt`, `README.md`, este registro, o diário e `docs/07-prototipo-e-testes.md`.

**Validação observada:** execução de 27 testes automatizados na nuvem, instalação em ambiente virtual novo, `pip check`, inicialização/renderização com SDL dummy por cinco quadros e compilação. O relatório 07 descreve os casos, a restrição inicial de rede e a solução. Não houve validação humana, teste visual, teste de Windows ou partida humana.

**Crédito de tecnologia:** Pygame 2.6.1, comunidade Pygame, https://www.pygame.org/ e https://www.pygame.org/docs/. Licença informada nos metadados da distribuição instalada: LGPL. Fonte padrão fornecida pelo pacote Pygame; não foi importada uma fonte de terceiros separadamente. Observar os avisos e licenças do pacote ao distribuí-lo. Python 3, Python Software Foundation, https://www.python.org/, é a linguagem/runtime.

**Recursos:** desenhos do protótipo foram construídos no código com primitivas do Pygame, com apoio de IA; sem imagens geradas, músicas, sons ou pacotes de arte externos. Não há adaptação de trechos dos repositórios de referência. Os links desses repositórios continuam como indicações de estudo futuro.

**Responsabilidade humana pendente:** ler e compreender o código e as regras, experimentar o protótipo no computador, confirmar a clareza das telas e registrar ajustes reais. A implementação assistida não deve ser apresentada como escrita exclusivamente pelo estudante.

## Atualização — revisão de interface

Data: 07/10/2026. ChatGPT/Codex apoiou a revisão solicitada após teste humano do usuário no Windows/Python 3.13.7 e cinco capturas fornecidas na conversa. As evidências humanas referem-se ao protótipo anterior.

Partes afetadas: novo `game/window.py` e `tests/test_ui.py`; alterações em `game/app.py`, `game/graphics.py`, nos textos de avisos de `game/run.py`, no README, no diário, neste registro e no novo relatório `docs/08-revisao-interface.md`. Finalidade: redimensionamento/F11, escala proporcional, legibilidade e clareza das regras.

Validação: 34 testes na nuvem (incluindo sete novos), oito tamanhos de superfícies SDL dummy, entrada por cinco quadros e inspeção de três imagens geradas na nuvem. Falha inicial de restauração de tamanho identificada pelo teste e corrigida. Nenhum teste interativo Windows desta revisão foi realizado pela IA; os detalhes estão no relatório 08. Não houve novos recursos externos ou bibliotecas adicionadas.

## Atualização — etapa 3: técnicas e arte no código

Data: 07/10/2026. ChatGPT/Codex apoiou a implementação autorizada de parallax, animação por quadros, partículas, feedback e chegada. A confirmação humana recebida dizia somente que a revisão anterior abriu e funcionou; não valida individualmente seus ajustes nem esta etapa 3.

Partes afetadas: novos `game/palette.py`, `game/parallax.py`, `game/animation.py`, `game/particles.py` e `tests/test_graphics.py`; composição em `game/graphics.py`, ligação de efeitos cosméticos em `game/run.py`, README, diário, este registro e `docs/09-tecnicas-graficas.md`.

Arte própria desta implementação assistida: camadas urbanas e nuvens, superfícies de quadros do entregador, cliente e formas de partículas, desenhados com primitivas. Sem sprite sheets externas, imagens geradas por IA, imagens baixadas, código de jogos de terceiros, sons ou novas bibliotecas. Fonte padrão do pacote Pygame e paleta compartilhada; créditos da tecnologia registrados acima.

Validação: 44 testes na nuvem, dez novos; inicialização por cinco quadros SDL dummy; inspeção estática de quatro cenas geradas com valores preparados. Não houve partida humana desta versão, teste Windows ou medição de FPS. Módulos e explicação técnica no relatório 09. Revisão humana e compreensão do código para apresentação continuam necessárias.

## Registro a completar a cada novo recurso ou uso de IA

Para código, imagem, fonte tipográfica, áudio, tutorial ou ferramenta: autor, título, link, licença disponível, data, arquivos/trechos afetados, uso (estudo/adaptação/reutilização), alterações e validação. Para IA, incluir ferramenta, finalidade, resultado adotado e como a pessoa responsável verificou esse resultado.

Recursos próprios futuros também devem ter autoria identificada. Não atribuir licença a recursos de terceiros sem verificá-la. Este registro não define uma licença para o projeto.
