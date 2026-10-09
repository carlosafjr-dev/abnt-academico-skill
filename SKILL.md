---
name: abnt-academico
description: >
  Normaliza, revisa e edita trabalhos acadêmicos brasileiros conforme as normas ABNT
  vigentes (NBR 14724:2024, NBR 10520:2023, NBR 6023:2025, NBR 6022, NBR 6028, NBR 15287
  e correlatas) e, quando a revista ou instituição exigir, conforme o estilo APA 7. Use
  sempre que o usuário pedir para formatar, revisar, corrigir, padronizar ou montar TCC,
  monografia, dissertação, tese, projeto de pesquisa, relatório técnico ou artigo para
  periódico; para converter citações e referências; para conferir se citações e lista de
  referências batem; ou para preparar um manuscrito para submissão. Acione também quando
  aparecerem termos como "ABNT", "NBR", "APA", "normas técnicas", "normalização",
  "formatação acadêmica", "citação", "referências bibliográficas", "et al.", "apud",
  "sumário", "resumo e abstract", "folha de rosto", "ficha catalográfica", "banca",
  "orientador", "diretrizes para autores", mesmo que o usuário não diga a palavra norma,
  e quando ele anexar um .docx ou PDF de trabalho acadêmico pedindo ajustes.
---

# ABNT Acadêmico

Skill de normalização de trabalhos acadêmicos. O foco é deixar o documento conforme a norma
que de fato se aplica a ele, sem mexer no argumento do autor e sem inventar dado algum.

## Princípios que orientam todo o trabalho

1. **A norma que manda é a do destino do texto.** A hierarquia é: diretrizes da revista
   (para artigo) ou manual da instituição/programa (para TCC, dissertação, tese) > norma
   ABNT ou APA > convenções de mercado. Muitos manuais institucionais ainda seguem edições
   antigas; nesse caso, siga o manual e avise o usuário sobre a diferença em relação à
   norma vigente, para ele decidir com o orientador. Nunca "corrija" uma regra
   institucional explícita para a ABNT por conta própria.
2. **Forma, não conteúdo.** Normalizar é ajustar apresentação, citação, referência e
   estrutura. Reescrever frases, cortar trechos ou mudar argumentos só com pedido
   explícito. Se notar problema de conteúdo (afirmação sem fonte, citação que parece não
   dizer o que o texto atribui a ela), aponte como observação, sem alterar.
3. **Nada de dado inventado.** Página, ano, editora, DOI, volume, cidade e data de acesso
   vêm da fonte ou do usuário. Quando faltar, marque `[VERIFICAR: o que falta]` no lugar e
   liste na pendência. Se houver ferramenta de busca, confira DOI e metadados (Crossref,
   página da revista, catálogo da editora) antes de completar. Referência que não for
   encontrada em lugar nenhum vira alerta de possível referência inexistente, nunca é
   completada por suposição.
4. **Consistência acima de preferência.** Várias regras atuais da ABNT são escolhas
   (et al. ou todos os autores; sigla ou nome por extenso da entidade; negrito, itálico ou
   sublinhado como destaque; recuo de citação longa). Escolha uma forma, aplique no
   documento inteiro e diga qual foi escolhida.
5. **Transparência sobre a fonte da regra.** O texto integral das normas ABNT é pago. As
   regras desta skill vêm de guias de bibliotecas universitárias e de trechos públicos das
   normas, conferidos na data indicada em `references/normas-vigentes.md`. Em disputa com
   banca ou editor, recomende conferir o texto oficial (muitas universidades dão acesso
   pela Target GEDWeb ou pela ABNT Coleção) ou o serviço de normalização da biblioteca.

## Fluxo de trabalho

### 1. Entender o pedido

Identifique, perguntando só o que não der para inferir:

- **Tipo de documento:** TCC/monografia, dissertação, tese, projeto de pesquisa, relatório
  técnico ou artigo para periódico.
- **Destino e norma:** instituição e curso, ou revista. Existe manual, template ou
  diretrizes para autores? Se o usuário tiver o documento, peça ou leia; ele prevalece.
- **Sistema de chamada:** autor-data (padrão no Brasil) ou numérico. Não misture.
- **Tipo de tarefa:** revisar texto pronto, revisar arquivo Word, montar ou converter
  referências, conferir citação x referência, orientar estrutura, ou preparar submissão.

Se o usuário não souber a norma do destino e o trabalho for brasileiro, use ABNT vigente e
registre essa premissa no topo da entrega. Se for artigo para revista, a primeira coisa a
checar são as diretrizes da revista: é comum exigirem APA, Vancouver ou template próprio
mesmo no Brasil.

### 2. Carregar só os módulos necessários

| Situação | Arquivo |
|---|---|
| Qual edição está vigente, o que mudou, fontes | `references/normas-vigentes.md` |
| Papel, margens, fonte, espaçamento, paginação, títulos, ilustrações, tabelas, notas | `references/formatacao-geral.md` |
| Elementos e ordem de TCC, dissertação, tese, projeto e relatório; resumo; sumário | `references/estrutura.md` |
| Citações no texto (NBR 10520:2023) e notas | `references/citacoes.md` |
| Lista de referências (NBR 6023:2025), modelos por tipo de fonte | `references/referencias.md` |
| Artigo para periódico (NBR 6022) e preparação de submissão | `references/artigo-periodico.md` |
| Revista ou instituição que exige APA 7 | `references/apa.md` |
| Revisão completa de um trabalho, erros frequentes | `references/checklist-revisao.md` |

Para "revise meu TCC inteiro", leia `checklist-revisao.md` primeiro e abra os outros
módulos conforme os problemas aparecerem.

### 3. Executar

**Texto colado na conversa.** Devolva o texto corrigido e, em seguida, o relatório de
alterações (formato abaixo). Em texto longo, entregue por seção para não truncar.

**Arquivo .docx.** Use a skill `docx` para editar o próprio arquivo, no formato original,
e prefira alterações controladas (track changes), para que o autor e o orientador vejam
cada ajuste e aceitem ou recusem. Aplique formatação por estilos (Normal, Título 1 a 5,
Citação longa, Legenda, Referência), não por formatação manual parágrafo a parágrafo,
porque é isso que faz o sumário automático e a numeração funcionarem. Paginação com
pré-textuais contados e não numerados exige quebra de seção antes da Introdução. Nunca
edite o arquivo enviado no lugar: trabalhe numa cópia e devolva a versão nova.

**PDF.** PDF não é editável de forma confiável. Faça a revisão como relatório (página,
problema, correção sugerida) e ofereça editar o .docx se o usuário tiver.

**Conferência de citações x referências.** Para trabalhos longos em autor-data, rode
`scripts/conferir_citacoes.py` sobre o texto (.docx, .txt ou .md). Ele lista chamadas sem
referência, referências nunca citadas, chamadas no formato antigo em caixa alta e outros
sinais de inconsistência. O script é um apoio: revise os achados antes de reportar, porque
ele não entende contexto (por exemplo, sobrenomes compostos ou entidades).

```bash
python scripts/conferir_citacoes.py caminho/do/trabalho.docx
```

### 4. Entregar

Use sempre esta estrutura ao final de uma revisão:

```
## Premissas
Norma aplicada (ex.: ABNT vigente; manual X; diretrizes da revista Y), sistema de chamada,
escolhas de consistência feitas (ex.: et al. a partir de 4 autores; destaque em negrito).

## Alterações feitas
Agrupadas por tipo (citações, referências, estrutura, formatação), com 1 exemplo de
antes/depois por tipo e a contagem de ocorrências. Não liste cada vírgula.

## Pendências [VERIFICAR]
Dados ausentes que só o autor pode fornecer: páginas, datas de acesso, DOIs, referências
não localizadas.

## Pontos para decidir com o orientador ou a revista
Onde manual e norma divergem, ou onde a norma deixa escolha.
```

Em perguntas pontuais ("como cito duas obras do mesmo autor no mesmo ano?"), responda
direto com a regra e um exemplo, sem esse relatório.

## Pontos de atenção que mais geram erro

- Chamada de autor dentro do parêntese vai em maiúsculas e minúsculas: (Silva, 2020, p. 45).
  O formato em caixa alta (SILVA, 2020) é da norma antiga e deve ser convertido. Na lista
  de referências, o sobrenome continua em maiúsculas: SILVA, João.
- *et al.*, *apud*, *In*, [*S. l.*], [*s. n.*] e demais expressões latinas vão em itálico.
- ABNT não obriga Arial nem Times New Roman. Pede fonte tamanho 12 no texto e tamanho menor
  e uniforme para citação longa, notas, paginação, ficha catalográfica, legendas e fontes
  das ilustrações e tabelas. Arial ou Times são a recomendação usual das bibliotecas.
- Trabalho acadêmico se divide em seções com numeração progressiva (NBR 6024), não em
  capítulos. Seção primária começa em página nova (no anverso, se frente e verso).
- Toda ilustração e toda tabela tem fonte, inclusive quando é do próprio autor
  ("Fonte: elaborado pelo autor (2026)").
- Referência só entra na lista se foi citada no texto, e toda citação tem referência.
- Uso de IA generativa no trabalho: oriente a declarar conforme a política da instituição
  ou da revista (o guia do SciELO pede declaração e não aceita IA como autora). Detalhes em
  `references/artigo-periodico.md` e `references/referencias.md`.

## Limites

A skill não substitui o orientador, a banca nem o serviço de normalização da biblioteca,
que confere a versão final e emite a ficha catalográfica. Diga isso uma vez, quando for
relevante, sem repetir em toda resposta.
