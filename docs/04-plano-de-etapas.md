# Plano de etapas e organização

Estado: planejamento em 07/10/2026. Sem prazos inventados; calendarizar após conhecer a data de entrega e a disponibilidade do estudante/equipe.

## Marcos e critérios de conclusão

| Marco | Trabalho previsto | Critério para concluir | Situação |
| --- | --- | --- | --- |
| 1 — Concepção | Regras, escopo, esboços, técnicas, matriz de requisitos e registro de IA | Estudante revisa a proposta, define integrantes e estuda as referências selecionadas | Documentação inicial produzida; revisão e estudo pendentes |
| 2 — Protótipo jogável | Janela, laço, corrida automática, salto, chão, obstáculo, gelo, conservação, destino e reinício básico | Demonstrar coleta, impacto, vitória, derrota e reinício com formas provisórias | Não iniciado |
| 3 — Versão intermediária | Telas completas, HUD, três trechos, arte mínima, parallax, animação e partículas | Fluxo completo e três técnicas visíveis; primeira rodada de ajustes e verificações registrada | Não iniciado |
| 4 — Versão final | Ajustar equilíbrio, verificar instalação, documentar ambiente, créditos e problemas, montar slides e pacote | Execução reproduzível, evidências reais, ensaio e cópia de segurança | Não iniciado |

Desenvolver primeiro a mecânica com formas simples. Introduzir uma técnica gráfica por vez para facilitar a compreensão e a identificação de problemas. Melhorias opcionais só entram depois de cumprir os requisitos obrigatórios.

## Organização futura sugerida

Esta árvore é uma proposta, não uma lista de arquivos já existentes.

```text
README.md
requirements.txt       # versões realmente verificadas
main.py                # inicialização, laço, eventos e seleção de estado
game/
  settings.py          # tamanhos, velocidades, custos e limites
  run.py               # simulação da corrida, regras e reinício
  entities.py          # personagem, obstáculos, itens e colisões
  graphics.py          # câmera, fundos, animação e partículas
  screens.py           # menu, instruções, pausa, resultado e HUD
assets/                # recursos próprios ou com créditos e licenças
docs/                  # planejamento, evolução e fontes
presentation/          # PPTX/PDF final e evidências selecionadas
```

Funções e módulos são suficientes; classes só quando ajudarem a representar entidades ou estados. Posições lógicas em ponto flutuante; retângulos para colisão; dados da rota separados das funções de atualização. Carregar recursos antes da partida e resolver caminhos a partir do projeto, evitando caminhos pessoais. Ao reiniciar, centralizar a criação do estado inicial para evitar dados da partida anterior.

## Divisão inicial de tarefas

Integrantes não informados. Os papéis abaixo estão a distribuir; não representam contribuições humanas realizadas.

| Frente | Responsabilidade | Responsável |
| --- | --- | --- |
| Regras e programação | Laço, controles, salto, colisões, conservação e resultado | A definir |
| Gráficos e interface | Telas, recursos próprios, parallax, animação e partículas | A definir |
| Verificação e documentação | Testes, evidências, créditos, README e slides | A definir |

Se o trabalho for individual, a mesma pessoa assume as três frentes. Em equipe, registrar por data o que cada integrante realmente fez e preparar todos para explicar as partes centrais do código.

## Verificações futuras

Todos os itens abaixo estão **pendentes**. Registrar ambiente, procedimento, resultado observado e correção quando forem executados; não registrar apenas “funcionou”.

| Verificação | Resultado esperado |
| --- | --- |
| Salto e aterrissagem | Um salto por acionamento válido; sem salto duplo; retorno ao chão |
| Obstáculo e proteção | Dano coerente de 20; sem múltiplos danos durante a proteção |
| Coleta e limite | Um efeito por item; conservação nunca acima de 100 |
| Conservação e pausa | Perda proporcional ao tempo ativo; nenhum avanço enquanto pausado |
| Resultado simultâneo | Aplicar a ordem de atualização documentada e a prioridade de derrota quando o valor final for zero |
| Vitória e derrota | Ambas alcançáveis; nenhuma mudança após encerrar a corrida |
| Progressão | Velocidades e trechos mudam nos limites corretos; saltos continuam possíveis |
| Reinício repetido | Restaurar todo o estado; não duplicar itens, efeitos ou dano |
| Telas e encerramento | Menu, instruções, pausa, resultados e fechamento da janela funcionam |
| Técnicas gráficas | Fundos sem lacunas, animação temporizada e partículas removidas/limitadas |
| Balanceamento | Rota completável com coletas; tempo de reação suficiente e informação clara |
| Desempenho | Medir FPS e observar travadas no computador de demonstração, sobretudo com partículas |
| Reprodução | Instalar com dependências documentadas em ambiente limpo e executar de outro diretório |

Começar com verificações manuais do comportamento visível. Considerar testes automatizados para cálculos de conservação, limites e reinício quando existir código. Não criar testes que apenas repitam a implementação sem verificar regras relevantes.

## Preparação da apresentação final

Planejar exposição de 10–15 minutos, como recomendado no enunciado: identificação e objetivo; conceito e esboços; referências efetivamente estudadas; regras e fluxo; arquitetura; três técnicas gráficas; movimento e colisões; evolução com capturas reais; dificuldades e testes reais; demonstração; contribuições e IA.

Guardar capturas datadas de cada versão quando existirem. Preparar PPTX ou PDF na finalização, com créditos, cópia de segurança e, preferencialmente, vídeo curto. Nenhum desses artefatos foi produzido nesta etapa.
