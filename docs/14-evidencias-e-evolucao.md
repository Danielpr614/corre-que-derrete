# Índice de evidências e evolução

Consolidado em 07/10/2026. Base: histórico Git, diário, relatórios e mensagens/capturas fornecidas pelo usuário. Os documentos históricos permanecem com o contexto da época; pendências antigas podem ter sido resolvidas depois. Este índice não cria retrospectivamente testes ou contribuições.

## Marcos preservados

Todos os marcos abaixo são de 07/10/2026, conforme o histórico; isso não comprova dias distintos de trabalho ou uma duração de desenvolvimento não registrada.

| Marco | Commit e registro | Evidência efetiva |
| --- | --- | --- |
| 1 — Concepção | [bf1db57](https://github.com/Danielpr614/corre-que-derrete/commit/bf1db57); docs 01–04 e diário | Tema do usuário, escopo, regras propostas, esboços textuais, fluxo, plano de etapas e referências indicadas. Sem jogo nessa versão. |
| 2 — Protótipo | [2ef4366](https://github.com/Danielpr614/corre-que-derrete/commit/2ef4366); [relatório 07](07-prototipo-e-testes.md) | Corrida, salto, colisões, conservação, três trechos, estados e pontuação. Instalação limpa na nuvem; 27 testes, entrada dummy, compilação e pip check. |
| Revisão da interface | [52fb13f](https://github.com/Danielpr614/corre-que-derrete/commit/52fb13f); [relatório 08](08-revisao-interface.md) | Redimensionamento/F11, proporção, textos e percentuais corrigidos; 34 testes e inspeção de superfícies. |
| 3 — Técnicas e arte | [9c21d5f](https://github.com/Danielpr614/corre-que-derrete/commit/9c21d5f); [relatório 09](09-tecnicas-graficas.md) | Parallax, quadros, partículas, feedback e chegada; 44 testes e composição estática na nuvem. |
| Renderização nativa | [26d723c](https://github.com/Danielpr614/corre-que-derrete/commit/26d723c); [relatório 10](10-renderizacao-nativa.md) | Troca da cena ampliada pela rasterização nativa, refinamento da arte; 48 testes e inspeção Full HD. |
| Cliente e música | [23f755e](https://github.com/Danielpr614/corre-que-derrete/commit/23f755e); [relatório 11](11-cliente-e-audio.md) | Rosto frontal, Ogg CC BY 3.0, opções/persistência de áudio; 59 testes, Ogg real com mixer dummy e loop após 28 s. |
| Preparação documental para etapa 4 | Commit desta revisão, após `23f755e`; docs 12–15, README e diário | Conferência do DOCX, manual técnico, índice e roteiro. Não equivale a slides concluídos, vídeo, entrega formal ou defesa realizada. |

Os totais 27/34/44/48/59 são o tamanho da suíte em cada marco, não testes independentes que devam ser somados. O histórico inicial `aaab7cc` não deve ser usado como evidência de um recurso não descrito. Nenhum marco anterior foi reescrito.

## Evidência humana e evidência na nuvem

| Evidência recebida/registrada | O que permite afirmar | O que não permite afirmar |
| --- | --- | --- |
| Usuário jogou protótipo no Windows com Python 3.13.7; controles responderam; cinco capturas de menu/instruções/corrida/derrota/vitória | Execução humana desse protótipo e telas apresentadas. | FPS, versão do Pygame ou validação da música/técnicas acrescentadas depois. |
| Usuário confirmou que a revisão da interface abriu e funcionou | Funcionamento geral daquela revisão no computador. | Teste individual de todos os textos, F11 e tamanhos. |
| Relato de baixa resolução em janela ampliada/tela cheia | Problema percebido que motivou o diagnóstico da superfície fixa. | Resultado da correção antes de ela ser testada. |
| Captura da vitória com olho único/boca irregular | Problema visual anterior do cliente. | Validação posterior da correção. |
| **Confirmação atual:** “A versão atual foi testada no Windows e o visual e o áudio ficaram satisfatórios.” | Satisfação humana com visual e áudio da versão `23f755e` enviada anteriormente. | Ambiente completo, FPS, duração, checklist individual de colisões, persistência, pausa/F11 ou ensaio no computador do professor. |
| SDL dummy, testes e imagens nos relatórios 07–11 | Lógica, carregamento, controles programados, superfícies renderizadas e inspeções descritas. | Teclado/dispositivo/monitor reais ou audição humana pela IA. |

As capturas do usuário estão na conversa, **não arquivadas no repositório**. Não há pasta de evidências de Windows já entregue nem vídeo. Imagens de diagnóstico na pasta ignorada `work/` são intermediários da nuvem e não integram um ZIP do GitHub. Não tratá-las como capturas de partida humana.

## Como organizar as capturas para os slides

Seleção proposta, ainda a executar: recuperar as cinco capturas reais do protótipo e produzir capturas atuais no Windows de corrida, vitória, partículas e Áudio. Para cada imagem, anotar versão/commit, ambiente, origem humana ou renderização preparada, contexto e data real quando conhecida. Se a data de captura não for conhecida, informar isso em vez de usar a data do commit.

Na comparação, mostrar provisório → técnicas → resolução nativa. Se não houver captura intermediária real disponível, usar a diferença de código e os registros desse commit; uma reconstrução posterior deve ser identificada como reconstrução, nunca como captura histórica. Não executar versões antigas sobre a cópia de trabalho com alterações não salvas; usar checkout separado se for necessário reconstruir.

O PPTX/PDF deve incorporar as imagens selecionadas. Capturas da conversa e imagens temporárias não devem ser prometidas como arquivos anexados à entrega até estarem efetivamente organizadas.

## Contribuições conhecidas

| Responsável | Contribuição registrada |
| --- | --- |
| Usuário/estudante, nome não informado | Ideia inicial; definição do escopo solicitado; orientações das revisões; testes e capturas no Windows; avaliação atual de visual/áudio. Não há registro nominal de escrita de módulos pelo usuário. |
| ChatGPT/Codex, OpenAI | Apoio à concepção; implementação ampla do código, desenhos geométricos, testes e documentação; diagnóstico, revisões e operações Git autorizadas. Partes por etapa em docs 06. |
| Outros integrantes | Composição do grupo e contribuições não informadas. Não atribuir módulos, testes ou slides a pessoas fictícias. |

Preencher identificação e contribuições efetivas antes da entrega. Se for individual, registrar esse formato após confirmação; o nome da conta GitHub não comprova a identidade ou contribuição de um integrante.

## Verificações desta revisão documental

Relido o DOCX, conferidos módulos/funções, arquivos rastreados, dependência e histórico. Conferidos links locais e `git diff --check` antes do commit. Não houve nova instalação, nova partida, nova audição, teste Windows pela IA ou nova medição de FPS. A confirmação humana atual foi registrada sem ampliar seu alcance. A suíte de 59 testes pertence ao último marco de implementação; esta revisão só altera documentação.
