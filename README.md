# Corre que Derrete!

Planejamento de um jogo 2D de corrida lateral e entrega de sorvete, para a disciplina de Computação Gráfica, em Python 3 e Pygame.

**Situação em 07/10/2026: etapa 1 — concepção.** Existe documentação; o jogo ainda não foi implementado. Não há comando de execução, dependências versionadas nem testes de jogabilidade realizados.

O entregador corre automaticamente por uma rua. O jogador salta obstáculos e coleta gelo para manter o sorvete conservado até o destino. Uma única rota terá três trechos de dificuldade crescente. A partida deverá durar aproximadamente um minuto, sujeito ao ajuste no protótipo.

## Documentação

- [Concepção, regras e controles](docs/01-concepcao.md)
- [Telas e técnicas gráficas](docs/02-telas-e-graficos.md)
- [Relação com o enunciado e a avaliação](docs/03-requisitos.md)
- [Etapas, organização e verificações futuras](docs/04-plano-de-etapas.md)
- [Diário de desenvolvimento](docs/05-diario.md)
- [Fontes, créditos e apoio de IA](docs/06-fontes-e-ia.md)

O enunciado `Projeto_Avaliativo_Jogo_2D_Python_Pygame_30_Pontos.docx`, do professor Pedro Cândido, é a referência principal dos requisitos. A solicitação desta etapa autoriza apenas planejamento; exigências de implementação e entrega descritas no documento estão registradas como trabalho futuro.

## Controles propostos

| Tecla | Ação |
| --- | --- |
| Espaço ou seta para cima | Saltar, quando estiver no chão |
| P ou Esc durante a corrida | Pausar ou retomar |
| Enter | Iniciar no menu ou jogar novamente no resultado |
| M | Voltar ao menu a partir da pausa ou do resultado |
| Esc no menu | Sair |

Os comandos serão exibidos nas telas. O fechamento da janela deverá funcionar em todos os estados.

## Estrutura atual e reprodução futura

Atualmente, o repositório contém este README e a pasta `docs/`. A arquitetura sugerida está no plano de etapas; pastas de código e recursos ainda não foram criadas.

Na etapa de implementação, registrar aqui a versão de Python realmente utilizada, o `requirements.txt` com a versão de Pygame validada, os comandos exatos de instalação e execução, a estrutura final e os problemas conhecidos. Não há instrução de instalação testada nesta etapa.
