---
name: abnt-academico
description: >
  Aplica as normas ABNT (2024/2026) em textos, artigos, TCCs, monografias e qualquer
  trabalho acadêmico. Use esta skill sempre que o usuário pedir para formatar, revisar,
  corrigir ou adaptar um texto às normas ABNT — incluindo formatação geral, citações
  diretas/indiretas, referências bibliográficas, estrutura de trabalho, títulos,
  sumário, resumo, paginação, figuras, tabelas e notas de rodapé. Deve ser acionada
  também quando o usuário mencionar termos como "NBR", "normas técnicas", "formatação
  acadêmica", "citação ABNT", "referências ABNT", "TCC", "monografia", "artigo
  científico" ou perguntar como fazer qualquer elemento estrutural de um trabalho
  acadêmico brasileiro.
---

# Skill: ABNT Acadêmico

Aplica, orienta e corrige textos segundo as normas ABNT vigentes (NBR 14724, NBR 10520, NBR 6023, entre outras).

## Fluxo de trabalho

1. Identificar o que o usuário precisa: formatar texto pronto, criar do zero, revisar citações, montar referências, ou orientar sobre estrutura.
2. Carregar o módulo de referência correspondente (ver seção abaixo).
3. Aplicar as regras e entregar o resultado corrigido ou orientado.
4. Se houver ambiguidade (ex: norma geral ABNT vs norma específica da instituição), alertar o usuário e perguntar qual prevalece.

## Módulos de referência

Para tarefas específicas, leia o arquivo correspondente em `references/`:

| Situação | Arquivo a ler |
|---|---|
| Formatação geral (papel, margens, fonte, espaçamento) | `references/formatacao-geral.md` |
| Citações diretas e indiretas | `references/citacoes.md` |
| Referências bibliográficas | `references/referencias.md` |
| Estrutura completa do trabalho | `references/estrutura.md` |

Se a tarefa envolver múltiplos aspectos ao mesmo tempo (ex: "revise meu TCC inteiro"), leia todos os módulos relevantes antes de responder.

## Regras de ouro (sempre aplicar, independente do módulo)

- Fonte: Arial ou Times New Roman, tamanho 12pt no corpo do texto
- Papel A4 branco, margens: superior 3cm, esquerda 3cm, inferior 2cm, direita 2cm
- Espaçamento 1,5 no corpo; simples em citações longas, notas de rodapé, legendas e referências
- Parágrafos justificados; referências alinhadas à esquerda
- Toda citação precisa de autoria — sem autoria = plágio

## Alertas importantes

- As normas ABNT são recomendações. Cada instituição pode ter variações próprias. Sempre orientar o usuário a confirmar com o orientador ou manual da faculdade.
- Se o usuário fornecer um texto para ser formatado, aplicar as regras diretamente e entregar o texto corrigido com comentários explicando cada mudança feita.
- Para dúvidas sobre citação de tipos específicos (site, apud, dois autores, sem autor, etc.), consultar `references/citacoes.md`.
