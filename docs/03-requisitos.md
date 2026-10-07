# Relação com o enunciado

Fonte principal: `Projeto_Avaliativo_Jogo_2D_Python_Pygame_30_Pontos.docx`, professor Pedro Cândido. As referências abaixo usam as seções do documento. O anexo foi lido como fonte de requisitos acadêmicos; a ação autorizada pelo usuário nesta etapa é somente planejar.

**Nenhum requisito de execução está marcado como implementado.** A matriz apresenta cobertura planejada e a evidência que ainda será necessária.

## Requisitos obrigatórios — seção 4

| Aspecto exigido | Solução planejada | Evidência futura |
| --- | --- | --- |
| Python 3 e Pygame | Usar Python 3 e Pygame; evitar bibliotecas extras sem necessidade | Código e arquivo de dependências com versões verificadas |
| Laço principal | Eventos → atualização da simulação → renderização; controle de tempo com `pygame.time.Clock` | Explicação do laço e demonstração |
| Estados | Menu, instruções, corrida, pausa, vitória/derrota; reinício e saída | Percorrer o fluxo inteiro sem editar código |
| Interação | Teclado, instruções visíveis e feedback de salto, dano e coleta | Verificação dos controles e telas |
| Mecânicas | Entregar antes de zerar a conservação; saltar obstáculos e coletar gelo | Partidas com vitória e derrota |
| Colisões | AABB para obstáculos e gelo; resposta vertical no chão | Hitboxes, explicação e testes de contato |
| Pelo menos três técnicas gráficas | Parallax, animação por quadros e partículas | Demonstração e explicação da implementação de cada técnica |
| Interface | Conservação com número/barra, progresso, trecho e avisos | HUD legível durante o jogo |
| Progressão | Três trechos com aumento de velocidade e frequência de obstáculos | Comparação entre início e fim da rota |
| Desempenho | Recursos carregados antes da partida; partículas limitadas; alvo de 60 FPS | Medição no computador de demonstração; estabilidade ainda desconhecida |
| Organização | Módulos pequenos por responsabilidade; sem exigir orientação a objetos | Estrutura final, nomes e responsabilidades explicáveis |
| Reprodução | Completar README com ambiente e comandos realmente verificados | Instalação em ambiente limpo e execução pelo comando documentado |

## Etapas e entregáveis — seções 6 e 7

| Exigência | Planejamento |
| --- | --- |
| Concepção | Tema, gênero, público, regras, esboços, fluxo e tarefas nos documentos atuais |
| Protótipo jogável | Próximo marco: movimento, salto, colisões e conservação com arte provisória |
| Versão intermediária | Estados, HUD, progressão e as três técnicas gráficas; evidências datadas |
| Versão final | Instalação verificada, documentação, créditos e apresentação |
| Código-fonte completo | Entregar futuramente código e recursos; não existe nesta etapa |
| README e dependências | README inicial atual; instruções executáveis e `requirements.txt` serão definidos com o protótipo |
| Apresentação PPTX ou PDF | Produzir na finalização; estrutura sugerida no plano de etapas |
| Créditos | Registro inicial em `06-fontes-e-ia.md`; completar a cada uso de recurso |
| Evolução e divisão de tarefas | Diário atual; responsáveis humanos ainda não informados; registrar contribuições reais |
| Demonstração | Preparar versão executável e cópia de segurança; vídeo curto é recomendado no enunciado |

Datas de entrega/apresentação, turma e integrantes estão em branco no anexo e não foram informados. Não assumir prazo, composição de equipe nem responsáveis.

## Autoria e referências — seções 5 e 11

Não foi adotada uma base de jogo existente. A ideia de entregador e sorvete foi fornecida pelo usuário; a IA ajudou a detalhar a proposta. O planejamento propõe conservação, itens e progressão como regras integradas ao tema, mas essas partes ainda não são código autoral implementado.

Caso seja usada uma base existente, verificar e registrar: mudança relevante de mecânica, identidade visual própria, sistema adicional desenvolvido pela equipe, referências explícitas e explicação das partes originais/adaptadas. Para qualquer material externo, registrar autor, título, link e licença quando disponível. Material público sem licença explícita deve ser tratado prioritariamente como referência de estudo, conforme o enunciado.

## Rubrica — seção 9

| Critério | Pontos | Como preparar evidência |
| --- | --- | --- |
| Concepção e planejamento | 2 | Documentos atuais; estudo das referências ainda pendente |
| Funcionamento e mecânicas | 5 | Protótipo, controles, estados e equilíbrio |
| Aplicação de Computação Gráfica | 6 | Explicar coordenadas, camadas e as três técnicas no código e na demonstração |
| Design visual e experiência | 3 | Telas coerentes, instruções e feedback legíveis |
| Qualidade do código | 4 | Módulos coesos, caminhos de recursos portáveis e constantes |
| Estabilidade e testes | 2 | Verificações com resultados reais e problemas corrigidos |
| Documentação da construção | 3 | Diário, capturas reais, decisões, créditos e apresentação |
| Apresentação e defesa | 4 | Ensaio e compreensão do código por quem apresentar |
| Originalidade e fontes | 1 | Transformações, créditos, licenças e declaração de IA |
| Total | 30 | Planos futuros não substituem recursos implementados e demonstráveis |

A proposta prioriza conclusão e capacidade de explicar o trabalho. A matriz não é promessa de nota nem comprovação de atendimento final.
