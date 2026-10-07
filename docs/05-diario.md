# Diário de desenvolvimento

Registrar ações realizadas separadamente de intenções. Datas no fuso do usuário (America/Sao_Paulo). Não usar este diário para simular histórico anterior.

## 07/10/2026 — Início da concepção

**Origem:** solicitação do usuário para planejar “Corre que Derrete!” com base no enunciado anexado. A ideia de corrida lateral, entregador, sorvete, obstáculos e itens de conservação veio do usuário.

**Estado encontrado:** repositório `corre-que-derrete` com um README breve e um commit inicial. Não foram encontrados arquivos de implementação no repositório.

**Ações realizadas nesta sessão com apoio de IA:**

- Leitura do texto do DOCX anexado, incluindo requisitos, etapas, entregáveis, rubrica e regras de autoria.
- Inspeção da estrutura e do estado Git do repositório.
- Redação da concepção, das regras propostas, de esboços textuais, do fluxo e do plano das técnicas gráficas.
- Mapeamento da proposta às exigências do professor.
- Organização do plano de etapas, das verificações futuras, deste diário e do registro de fontes/IA.
- Atualização do README para indicar o estágio real do projeto.

**Decisões propostas:** uma rota finita com três trechos; corrida automática e salto; conservação como recurso central; gelo como único coletável; dois obstáculos de chão; parallax, animação por quadros e partículas; posições de objetos definidas manualmente.

**Verificações realizadas:** leitura do anexo e inspeção dos arquivos do repositório. Os sete documentos foram conferidos quanto à presença dos requisitos e à distinção entre planejamento e implementação; os links locais foram verificados e `git diff --check` não apontou erros. Isso não equivale a testes do jogo.

**Não realizado:** programação do jogo, criação de arte final, consulta técnica aos repositórios externos citados, instalação de dependências para este projeto, execução, testes de controles/colisões, medição de FPS, validação de equilíbrio, slides ou vídeo. Não foi criado novo commit nem feita publicação remota nesta etapa.

**Contribuições:** o usuário forneceu a ideia e delimitou a etapa. ChatGPT/Codex apoiou a leitura e a redação dos arquivos listados em `06-fontes-e-ia.md`. A revisão humana, a identificação dos integrantes e a distribuição efetiva das tarefas estão pendentes; não atribuir a alguém trabalho ainda não realizado.

**Próximo marco:** revisão da concepção pelo estudante e, quando solicitada a implementação, protótipo com recursos provisórios. Valores numéricos dependem de verificação futura.

## 07/10/2026 — Etapa 2: protótipo jogável

**Solicitação:** avançar para o protótipo, preservar o planejamento no Git antes de implementar e registrar um segundo marco separado. Pontuação foi acrescentada aos requisitos pelo usuário.

**Preservação:** criado o commit `bf1db57` (`docs: registra marco 1 de concepcao e planejamento`) com o README e os seis documentos da etapa 1, antes de escrever código do jogo. A entrada anterior continua descrevendo apenas aquela primeira sessão.

**Implementado com apoio de IA:** entrada `main.py`; módulos `settings`, `entities`, `run`, `app` e `graphics`; corrida, salto, gravidade, obstáculos, colisões, gelo, derretimento, três trechos, vitória/derrota, menus, instruções, pausa, reinício, HUD e pontuação. Arte provisória com formas do Pygame e fonte padrão da biblioteca, sem áudio ou recursos externos de arte.

**Documentação e dependências:** Pygame 2.6.1 fixado em `requirements.txt`; README atualizado com comandos e instruções Windows/VS Code; relatório `07-prototipo-e-testes.md` criado; declaração de IA ampliada. Os documentos originais 01–04 permanecem como planejamento histórico.

**Verificações realizadas na nuvem:** 27 testes automatizados passaram; instalação do `requirements.txt` num ambiente virtual novo com Python 3.12.14 concluída; suíte repetida nesse ambiente com sucesso; `pip check` sem dependências quebradas; entrada executada por cinco quadros com SDL dummy a partir de outro diretório; compilação Python sem erro. O teste de reinício foi ajustado para realmente repetir três partidas na mesma instância do controlador e passou. Resultados e procedimentos detalhados no documento 07.

**Problema observado e solução:** a primeira instalação no ambiente novo falhou por restrição de rede do sandbox ao proxy. A instalação foi repetida com acesso de rede permitido e sem cache, e funcionou. Não foi observada falha funcional na suíte; isso não comprova ausência de bugs fora da cobertura.

**Limites:** não houve instalação no Windows, inspeção visual humana, teclado real, partida humana, ajuste de equilíbrio baseado em jogadores nem medição de FPS. O caminho vencedor do teste usa posições internas da rota. Parallax, animação por quadros e partículas seguem pendentes para a próxima etapa.

**Contribuições:** usuário definiu o escopo da etapa e a pontuação no HUD; ChatGPT/Codex redigiu código, testes e atualizações documentais e executou as verificações descritas. Não foi registrada revisão humana do código ou das telas. Integrantes e divisão de contribuições humanas continuam a definir.

**Marco Git:** commit separado com mensagem `feat: registra marco 2 do prototipo jogavel`; consultar `git log --oneline` para o identificador. Commits locais na branch `work`; nenhum `git push` foi executado. Publicação/sincronização da branch no GitHub permanece uma ação pendente.

**Próximo passo:** baixar/publicar a versão correta, executar no Windows, registrar observações reais e revisar dificuldades antes do marco 3 de gráficos e acabamento.

## 07/10/2026 — Revisão de interface após teste no Windows

**Evidência humana recebida:** usuário informou execução do protótipo anterior no Windows/Python 3.13.7, com controles responsivos. Cinco capturas na conversa mostram menu, instruções, corrida, derrota e vitória. Não inferir versão de Pygame, FPS ou teste dos novos modos de janela.

**Realizado com apoio de IA:** janela redimensionável/maximizável, F11 e restauração do tamanho; superfície lógica fixa com escala 16:9 e margens; setas substituídas por palavras; objetivo/menu revisados; conservação com uma casa decimal e vírgula; explicação de pontos percentuais e pontuação; revisão de alinhamentos, espaços e fonte padrão. Nenhuma constante física ou fórmula de pontuação mudou.

**Verificações:** 34 testes passaram na nuvem, incluindo sete novos testes de interface, renderização de seis telas/resultados em oito tamanhos, limites dos textos e simulação independente da resolução. Entrada executada por cinco quadros dummy. Inspecionadas três imagens geradas na nuvem (instruções, menu 4:3 e vitória em retrato). O documento 08 detalha tamanhos, comandos e limites.

**Falha real e correção:** o backend dummy não restaurou 800 × 600 na primeira saída de tela cheia; aplicada reaplicação condicional do modo se o tamanho estiver incorreto. Todos os testes passaram depois da correção.

**Documentação:** README atualizado, novo relatório 08 e declaração de IA ampliada. Atualizado o estado de publicação dos marcos anteriores, cujo push foi confirmado na sessão anterior.

**Pendências:** redimensionamento por arraste, maximização pelo sistema, F11 e jogabilidade desta revisão no Windows; nenhum novo teste interativo Windows foi executado pela IA. Sem nova instalação de dependências ou medição de FPS nesta sessão.

**Histórico:** ajuste separado com mensagem `fix: revisa interface e modos de janela`; envio à branch `work` autorizado pelo usuário, com confirmação ao fim desta sessão. Os commits de planejamento/protótipo são preservados.

## 07/10/2026 — Etapa 3: técnicas gráficas e acabamento

**Confirmação humana:** usuário informou que a revisão anterior abriu e funcionou no computador. Não relatou testes individuais de todos os ajustes de interface; não presumir validação de F11, maximização, cada texto ou de qualquer recurso desta nova etapa.

**Realizado com apoio de IA:** parallax de nuvens/prédios/fachadas; seis quadros de corrida e dois de salto; partículas de gelo, impacto e conservação baixa; feedback por formas, cores e avisos; cliente visível no destino e ilustração da entrega na vitória. Novos módulos `palette`, `parallax`, `animation` e `particles`. Arte desenhada pelo Pygame no código, sem novos recursos externos ou dependências.

**Preservado:** rota, constantes físicas, hitboxes, ordem de colisões/resultados, pontuação, controles, pausa/reinício, redimensionamento e F11. Efeitos são cosméticos, com limite de 100 partículas e vida finita; atualização pelo tempo de simulação.

**Verificado na nuvem:** suíte anterior passou; acrescentados dez testes de técnicas/efeitos e suíte final com 44 testes passou; entrada executada por cinco quadros dummy. Inspecionada montagem de quatro cenas construídas para avaliar composição estática, não capturas de partida humana. Procedimentos e limites em `09-tecnicas-graficas.md`. Não foi observado teste falhando nesta etapa.

**Não realizado:** teste desta etapa no Windows, avaliação humana da animação/parallax em movimento, medição de FPS, nova instalação de dependências, áudio, slides ou vídeo de partida. Sua confirmação de execução foi registrada apenas para a versão anterior.

**Documentação/histórico:** README e créditos atualizados; relatório 09 descreve as técnicas e recursos; commit próprio `feat: registra etapa 3 de tecnicas graficas`, com push solicitado para `work`. Confirmação do envio ao fim da sessão. Marcos anteriores permanecem no histórico.

**Próximo passo:** testar esta versão no computador, registrar observações reais e preparar apresentação e entrega final depois dos ajustes necessários.

## 07/10/2026 — Renderização nativa e arte em Full HD

**Relato recebido:** usuário percebeu imagem e textos esticados em janela ampliada/tela cheia e solicitou investigação e melhoria. Não é confirmação de testes da correção atual.

**Causa observada:** cena e fontes rasterizadas em 960 × 540 e ampliadas por `smoothscale`; quadros/fundos também tinham resolução fixa baixa. Corrigida a arquitetura para desenhar na resolução da área 16:9, com fontes nativas, recursos regenerados e cópia final sem escala. Novo módulo `drawing.py` converte apenas coordenadas gráficas.

**Acabamento:** detalhes adicionais no personagem, cliente, fachadas, cone, caixa e gelo; gradiente e sombras de painel. Recursos próprios no código com apoio de IA; nenhuma nova dependência ou imagem externa.

**Verificações reais:** 48 testes passaram ao final, incluindo quatro novos testes de resolução, apresentação sem interpolação, caches e independência da física. Testes anteriores de janela atualizados porque pressupunham a arquitetura removida. Comando de entrada por cinco quadros dummy. Inspeção de três cenas Full HD e nova corrida após corrigir franjas transparentes detectadas nas imagens; suíte repetida após essa correção. Detalhes em `10-renderizacao-nativa.md`.

**Preservado/pendente:** nenhuma mudança nas regras, constantes físicas, rota ou controles. Parallax, animação, partículas, pausa/reinício, proporção, redimensionamento e F11 continuam. Teste interativo Windows, DPI, fluidez, FPS e memória pendentes. Sem nova instalação nesta sessão.

**Registro:** README, diário e créditos atualizados; relatório 10 criado. Commit separado `fix: renderiza em resolucao nativa e refina arte`, com push autorizado para `work`; resultado confirmado ao fim da sessão.

## 07/10/2026 — Cliente frontal e áudio

**Pedido/evidência:** captura do usuário mostrou olho único e boca irregular no cliente da vitória. Solicitada correção compartilhada com a chegada e música licenciada com controles/persistência. A captura não valida a nova versão.

**Implementação assistida por Codex:** dois olhos simétricos com pupilas contrastantes e sorriso central; perfil do entregador preservado. Novo módulo audio.py, faixa Ogg licenciada incluída, Áudio no menu/pausa, controles, volume inicial 15%, loop contínuo e preferências locais; falhas não impedem jogar. Regras e técnicas gráficas preservadas.

**Fonte:** House In a Forest Loop, HorrorPen, CC BY 3.0, obtida da cópia Godot com autoria/licença declaradas no README específico. Créditos completos em assets/audio/CREDITOS.md; nenhuma licença inventada, nenhum áudio gerado por IA.

**Verificações reais:** 59 testes passaram; 11 novos de áudio. Mixer dummy carregou/reproduziu Ogg e permaneceu ativo após 28 s. Entrada por cinco quadros e caminhos a partir de outra pasta; layouts em quatro tamanhos. Inspeção estática de chegada/vitória em 960 × 540 e Full HD, rosto ampliado e tela Áudio. Sem audição, jogo humano ou janela interativa Windows. Relatório 11 detalha evidências e pendências.

**Histórico:** correção e áudio em um commit separado, com push solicitado para work; resultado informado ao encerrar. Pendente conferir rosto/F11, música, controles, persistência e pausa no computador.

## 07/10/2026 — Conferência documental e preparação da apresentação

**Confirmação humana recebida:** “A versão atual foi testada no Windows e o visual e o áudio ficaram satisfatórios.” Refere-se à implementação 23f755e enviada anteriormente. Não informa duração, hardware, FPS ou checklist individual; não presume validação desses aspectos.

**Trabalho realizado com apoio de Codex:** relido o DOCX disponível; conferidos código, dependência, histórico e registros. README atualizado com instruções/controles/regras/créditos e confirmação atual; matriz histórica 03 sinalizada; novos relatórios 12 (requisitos e pendências), 13 (organização/loop/colisões/técnicas), 14 (evidências) e 15 (roteiro proposto de 13 minutos). Verificados metadados de FreeSans incluída no Pygame, sem acrescentar arquivo de fonte.

**Verificações desta sessão:** conferência documental e links locais; git diff --check. Nenhuma mudança no código, nova instalação, suíte executada, audição, teste interativo ou medição de desempenho. Os 59 testes registrados são do último marco de implementação.

**Pendências reais:** nomes/turma/datas e divisão efetiva; slides PPTX/PDF com capturas arquivadas; ensaio/domínio do código; pacote/cópia offline e vídeo recomendado. Não há entrega formal realizada ou etapa 4 concluída declarada. Documentação em commit separado; push solicitado para work e resultado informado ao encerrar.

## Modelo para próximas entradas

- Data e marco:
- Integrante responsável e contribuição real:
- Objetivo da sessão:
- Arquivos alterados e decisões:
- Fonte ou IA utilizada, finalidade e partes afetadas:
- Verificações executadas, ambiente e resultados observados:
- Problemas encontrados e correções:
- Evidências existentes (commit, captura, vídeo ou arquivo):
- Pendências e próximo passo:
