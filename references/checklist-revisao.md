# Checklist de revisão completa

Ordem pensada para revisar um trabalho inteiro sem retrabalho: primeiro o que muda a
estrutura (e a paginação), depois o que é repetitivo (citações e referências), por fim o
acabamento. Marque cada item como conforme, corrigido ou pendente.

## 1. Premissas
- [ ] Tipo de documento e instituição ou revista identificados.
- [ ] Manual, template ou diretrizes conferidos; divergências com a ABNT anotadas.
- [ ] Sistema de chamada definido (autor-data ou numérico) e aplicado de forma única.
- [ ] Escolhas de consistência registradas (et al., sigla ou nome de entidade, destaque
      das referências, prenome por extenso ou abreviado).

## 2. Estrutura
- [ ] Todos os elementos obrigatórios presentes e na ordem certa (`estrutura.md`).
- [ ] Capa e folha de rosto: local e ano da entrega; natureza do trabalho completa e
      alinhada à direita; orientador com titulação.
- [ ] Ficha catalográfica emitida pela biblioteca (ou espaço reservado com aviso).
- [ ] Resumo e abstract: extensão, parágrafo único, palavras-chave no formato, abstract fiel.
- [ ] Sumário gerado pelos estilos, sem pré-textuais, igual aos títulos do texto.
- [ ] Listas de ilustrações e tabelas batendo com as legendas.
- [ ] Seções numeradas (não "capítulos"), primárias em página nova.
- [ ] Apêndices (do autor) e anexos (de terceiros) identificados corretamente.

## 3. Citações
- [ ] Chamadas em maiúsculas e minúsculas (sem SILVA, 2020).
- [ ] *et al.*, *apud* e demais expressões latinas em itálico.
- [ ] Página em toda citação direta.
- [ ] Citações com mais de três linhas em bloco, fonte menor, simples, sem aspas.
- [ ] Ponto final depois da chamada.
- [ ] *apud* usado com moderação e só com original inacessível.
- [ ] Grifos e traduções do autor indicados.

## 4. Referências
- [ ] Cada chamada tem referência e cada referência foi citada (use
      `scripts/conferir_citacoes.py`).
- [ ] Ano e grafia do autor iguais na chamada e na referência.
- [ ] Ordem alfabética (ou numérica), alinhamento à esquerda, simples, linha em branco.
- [ ] Destaque único e no elemento certo (livro ou periódico, não capítulo ou artigo).
- [ ] Documentos online com Disponível em e Acesso em; DOI em formato de URL.
- [ ] Nenhum dado completado por suposição; pendências marcadas [VERIFICAR].
- [ ] Referências suspeitas (não localizadas em base alguma) sinalizadas.

## 5. Ilustrações e tabelas
- [ ] Título acima com designação, número e travessão; fonte abaixo, inclusive nas do autor.
- [ ] Citadas no texto antes de aparecer e posicionadas perto da menção.
- [ ] Tabelas com bordas laterais abertas; quadros fechados.

## 6. Formatação
- [ ] Papel, margens, fonte, tamanhos e espaçamentos (`formatacao-geral.md`).
- [ ] Paginação começando a aparecer na Introdução, com contagem correta das pré-textuais.
- [ ] Títulos sem ponto final, destaque igual por nível, sem título "solto" no pé da página.
- [ ] Notas de rodapé em tamanho menor e simples.
- [ ] Siglas definidas na primeira ocorrência.

## Erros mais frequentes em TCC (vistos pelos serviços de normalização)
1. Chamadas no formato antigo em caixa alta, misturadas com o formato novo.
2. Obras citadas que não estão nas referências, e o inverso.
3. Ano diferente entre chamada e referência.
4. Citação direta sem página.
5. Citação longa formatada como curta, ou com aspas e recuo ao mesmo tempo.
6. Ilustração sem fonte, sobretudo as feitas pelo autor.
7. Sumário digitado à mão, com páginas erradas.
8. Numeração de página aparecendo nas pré-textuais.
9. Referências com destaque misturado (negrito e itálico) ou destaque no título do artigo.
10. Documentos online sem data de acesso; DOI ausente quando existe.
11. Resumo com vários parágrafos ou acima do limite; abstract que não corresponde ao resumo.
12. Uso de "capítulo" no lugar de "seção" e seção primária que não abre página nova.
