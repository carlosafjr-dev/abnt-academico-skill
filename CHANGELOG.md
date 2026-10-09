# Changelog

## 2026-10-09: Revisão geral e inclusão de APA 7

### Correções de conteúdo normativo
- Citações (NBR 10520:2023): chamada com sobrenome em maiúsculas e minúsculas, (Silva, 2020);
  entidade por sigla ou por extenso; obra sem autoria com primeira palavra + [...];
  et al. opcional a partir de 4 autores; expressões latinas em itálico; recuo da citação longa
  como recomendação; localizadores para e-book, áudio, vídeo e documento jurídico; ponto final
  depois da chamada; grifo nosso ou grifo próprio; informação verbal no texto.
- Referências (NBR 6023:2025, 3ª ed., 21 maio 2025): mudanças conforme bibliotecas
  universitárias (e-localização, cidade do evento opcional, "julgado em", suplemento, ca.,
  séries, ISSN complementar, local omitido em documento online). Retiradas afirmações sem
  confirmação em fonte confiável (data de acesso opcional, modelos novos de podcast e rede
  social). Regra de 4 ou mais autores: convém indicar todos, permitido et al.
- Formatação (NBR 14724:2024): a norma não define tipo de letra; fonte menor e uniforme para
  citação longa, notas, paginação, ficha, legendas e fontes; margens de verso; paginação e
  ficha catalográfica em impresso e eletrônico; fonte obrigatória em ilustrações e tabelas.
- Estrutura: ficha catalográfica incluída; "Desenvolvimento" não é título de seção; sumário
  sem pré-textuais; resumo pela NBR 6028:2021 (sem quantidade fixa de palavras-chave);
  projeto de pesquisa (NBR 15287:2025) e relatório técnico (NBR 10719:2015).

### Novos módulos
- normas-vigentes.md, artigo-periodico.md, apa.md, checklist-revisao.md.
- scripts/conferir_citacoes.py: confere citações x referências.

### Fluxo
- Hierarquia de normas (revista ou instituição > ABNT/APA), regra de não inventar dado,
  edição de .docx com alterações controladas, relatório padrão de entrega, orientação sobre
  uso de IA generativa.

## 2026-07-31: Atualização de normas vigentes

### NBR 14724 (estrutura de trabalhos acadêmicos): 2011 → 2024 (4ª edição)
- Terminologia: "capítulos" foi substituído por "seções" em toda a documentação
- Seções primárias devem sempre começar em nova página (frente da folha, em trabalhos frente e verso)
- Ficha catalográfica: referência ao código AACR2 removida; em formato eletrônico, a ficha deve constar imediatamente após a folha de rosto
- Cidade e ano na capa: esclarecido que devem corresponder ao local/ano da instituição e da entrega, não da pesquisa
- Epígrafe: diferenciação entre epígrafe pré-textual (não segue NBR 10520) e epígrafes em abertura de seção primária (seguem NBR 10520)

### NBR 6023 (referências bibliográficas): 2018 (com errata 2023) → 2025 (3ª edição)
- Estrutura básica das referências permanece inalterada
- DOI passa a ser indicado em formato de URL completa
- Novos modelos de referência para podcasts e redes sociais
- Regra mais clara de data de acesso para conteúdo instável (redes sociais, wikis)
- E-localização adicionada para artigos eletrônicos sem paginação tradicional
- Cidade do evento deixou de ser obrigatória em referências de anais quando a informação não está disponível

### Não alterado nesta atualização
- NBR 10520:2023 (citações) já estava correta na versão anterior da skill
- NBR 6027 e NBR 6028 (sumário e resumo) sem mudanças identificadas que afetem o conteúdo já presente
- Regras gerais de formatação (margens, fonte, espaçamento) permanecem as mesmas

### Fontes consultadas
Guias e tutoriais de bibliotecas universitárias (UFU, PUCPR, UFMG, entre outras) e páginas especializadas em normalização acadêmica, todos posteriores à publicação oficial das novas edições pela ABNT. O texto integral e oficial das normas é vendido pela ABNT e não foi consultado diretamente linha por linha nesta atualização.
