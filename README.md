# Skill ABNT Acadêmico para Claude

Skill que deixa trabalhos acadêmicos brasileiros conformes às normas ABNT vigentes e, quando a
revista ou a instituição exige, ao estilo APA 7. Serve para TCC, monografia, dissertação, tese,
projeto de pesquisa, relatório técnico e artigo para periódico.

Criada por [Carlos Alberto Ferreira](https://github.com/carlosafjr-dev) | Agência Ojuobá

**Instalação rápida no Claude.ai:** baixe o arquivo [`dist/abnt-academico.zip`](dist/abnt-academico.zip)
e envie em Configurações > Capacidades > Skills. Detalhes em [Instalação](#instalação).

---

## O que é

Uma skill é um pacote de instruções que o Claude consulta sozinho quando o assunto aparece na
conversa. Depois de instalada, não é preciso chamá-la pelo nome.

### O que ela faz

- Revisa texto colado na conversa ou arquivo Word (.docx), com alterações controladas, para você
  aceitar ou recusar cada ajuste.
- Converte citações do formato antigo, como (SILVA, 2020), para o formato atual, (Silva, 2020).
- Monta e confere referências, sem completar página, ano ou DOI por suposição. O que falta aparece
  marcado como `[VERIFICAR]`.
- Confere se toda citação do texto tem referência na lista, e se toda referência foi citada.
- Orienta a estrutura de cada tipo de trabalho, da capa aos anexos.
- Prepara artigos para submissão: diretrizes da revista, avaliação cega, declarações e uso de IA.
- Aplica APA 7 quando esse é o estilo exigido.

### O que ela não faz

Ela mexe na forma, não no conteúdo. Não reescreve argumentos nem corta trechos, a menos que você
peça. Também não substitui o orientador nem o serviço de normalização da biblioteca, que confere a
versão final e emite a ficha catalográfica.

### Normas cobertas

| Norma | Edição | Assunto |
|---|---|---|
| NBR 14724 | 2024 | Trabalhos acadêmicos |
| NBR 10520 | 2023 | Citações |
| NBR 6023 | 2025 | Referências |
| NBR 6022 | 2018 | Artigo em periódico |
| NBR 6024 | 2012 | Numeração das seções |
| NBR 6027 | 2012 | Sumário |
| NBR 6028 | 2021 | Resumo |
| NBR 15287 | 2025 | Projeto de pesquisa |
| NBR 10719 | 2015 | Relatório técnico |
| APA | 7ª edição | Estilo APA |

As fontes de cada regra estão em [`references/normas-vigentes.md`](references/normas-vigentes.md).

---

## Quando ela entra em ação

A skill é acionada quando a conversa trata de trabalho acadêmico ou de normalização:

- Termos de norma: ABNT, NBR, APA, normas técnicas, formatação acadêmica, normalização.
- Elementos do trabalho: citação, referências, et al., apud, sumário, resumo e abstract, folha de
  rosto, ficha catalográfica.
- Tipos de trabalho: TCC, monografia, dissertação, tese, projeto de pesquisa, artigo científico.
- Contexto de avaliação: banca, orientador, diretrizes para autores, submissão para revista.
- Envio de um .docx ou PDF de trabalho acadêmico com pedido de ajuste.

Exemplos de pedidos:

- "Converta estas citações para a ABNT atual."
- "Revise as referências do meu TCC e diga o que está faltando."
- "Confira se todas as obras citadas estão na lista de referências." (com o arquivo anexado)
- "Como cito duas obras do mesmo autor no mesmo ano?"
- "Quais elementos uma dissertação precisa ter, e em que ordem?"
- "Vou submeter para uma revista que pede APA. O que preciso ajustar?"

Se ela não for acionada, escreva "use a skill abnt-academico" no pedido.

---

## Instalação

### Requisitos

- Conta paga do Claude: Pro, Max, Team ou Enterprise. Skills personalizadas não funcionam no plano
  gratuito.
- Execução de código ligada (Configurações > Capacidades > "Execução de código e criação de arquivos").
  No Enterprise, um administrador precisa liberar execução de código, criação de arquivos e Skills.
- A skill instalada fica só na sua conta.

### Opção 1: zip pronto (recomendada para Claude.ai)

1. Abra [`dist/abnt-academico.zip`](dist/abnt-academico.zip) aqui no GitHub e clique no botão de
   download (ícone de seta, "Download raw file").
2. Não descompacte. O zip já contém a pasta `abnt-academico/` com o `SKILL.md` dentro, no formato
   que o Claude espera.
3. No Claude, abra Configurações > Capacidades, vá até a seção Skills e clique em "Enviar skill"
   (Upload skill). Escolha o zip.
4. Confira se a skill aparece na lista com o botão ligado.
5. Teste numa conversa nova: "Converta para a ABNT atual: (SILVA; SOUZA, 2020, p. 45)". A resposta
   esperada é (Silva; Souza, 2020, p. 45).

Os nomes dos menus podem mudar com atualizações do Claude. O caminho atual está na central de ajuda:
[Using Skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude).

### Opção 2: a partir do "Code > Download ZIP"

O zip que o GitHub gera pelo botão **Code > Download ZIP** vem com a pasta `abnt-academico-skill-main/`,
e o Claude exige que a pasta tenha o mesmo nome da skill. Por isso ele não serve direto. Para usar
esse caminho:

1. Baixe pelo **Code > Download ZIP** e descompacte.
2. Renomeie a pasta `abnt-academico-skill-main` para `abnt-academico`.
3. Apague a pasta `dist/` de dentro dela (opcional, só diminui o tamanho).
4. Compacte a pasta `abnt-academico` de novo em zip e siga os passos 3 a 5 da Opção 1.

### Opção 3: Claude Code

Clone direto na pasta de skills do usuário:

```bash
git clone https://github.com/carlosafjr-dev/abnt-academico-skill.git ~/.claude/skills/abnt-academico
```

Para atualizar depois: `git -C ~/.claude/skills/abnt-academico pull`.

### Atualizar ou desativar no Claude.ai

- **Atualizar:** remova a skill antiga na lista de Skills (opção de excluir) e envie o zip novo.
- **Desativar sem apagar:** use o botão de liga e desliga na lista.

---

## Como usar bem

O que mais melhora o resultado é dizer para onde o trabalho vai. A regra que vale é a do destino:
o manual da instituição ou as diretrizes da revista vêm antes da ABNT ou da APA.

- **Informe o tipo de trabalho e a instituição ou revista.** Exemplo: "TCC de Jornalismo da PUC-Rio"
  ou "artigo para a revista X".
- **Anexe o manual ou as diretrizes**, se tiver. A skill segue o documento e avisa quando ele diverge
  da norma vigente.
- **Prefira enviar o .docx.** Ela edita o próprio arquivo com alterações controladas. Em PDF, entrega
  um relatório com página, problema e correção sugerida.
- **Em trabalhos longos, peça por partes:** estrutura, depois citações, depois referências.
- **Peça a conferência de citações.** O script `scripts/conferir_citacoes.py` cruza as chamadas do
  texto com a lista de referências e aponta o que sobra ou falta.

Ao final de uma revisão, a entrega vem em quatro blocos:

1. **Premissas:** norma aplicada e escolhas de padronização.
2. **Alterações feitas:** agrupadas por tipo, com exemplo de antes e depois.
3. **Pendências [VERIFICAR]:** dados que só o autor pode fornecer, como página, data de acesso ou DOI.
4. **Pontos para decidir com o orientador ou a revista:** onde a norma deixa escolha ou o manual diverge.

---

## Estrutura do repositório

```
abnt-academico-skill/
├── SKILL.md                     fluxo de trabalho e princípios
├── references/
│   ├── normas-vigentes.md       edições vigentes, o que mudou, fontes
│   ├── formatacao-geral.md      NBR 14724 e 6024: página, fonte, títulos, ilustrações
│   ├── estrutura.md             elementos de TCC, dissertação, tese, projeto, relatório
│   ├── citacoes.md              NBR 10520:2023
│   ├── referencias.md           NBR 6023:2025
│   ├── artigo-periodico.md      NBR 6022 e checklist de submissão
│   ├── apa.md                   APA 7
│   └── checklist-revisao.md     revisão completa e erros frequentes
├── scripts/
│   └── conferir_citacoes.py     confere citações x referências (.docx, .txt, .md)
├── dist/
│   └── abnt-academico.zip       pacote pronto para enviar ao Claude.ai
├── CHANGELOG.md
└── LICENSE
```

---

## Limites e cuidados

- **Normas mudam.** A skill reflete as edições vigentes em outubro de 2026. Veja o
  [CHANGELOG](CHANGELOG.md) para saber a data da última revisão.
- **O texto oficial da ABNT é pago.** As regras vêm de guias de bibliotecas universitárias e trechos
  públicos das normas. Se a banca contestar um detalhe, vale o texto oficial ou a biblioteca da sua
  instituição.
- **Confira as pendências.** A skill não inventa dados. Referência que ela não encontra em nenhuma base
  pode não existir, o que é comum em listas montadas com ajuda de IA.
- **Declare o uso de IA** se a instituição ou a revista pedir.
- **A revisão humana continua necessária.** Orientador e biblioteca dão a palavra final.

---

## Para mantenedores

Depois de alterar qualquer arquivo da skill, gere o zip de novo a partir da raiz do repositório:

```bash
rm -rf /tmp/abnt-academico && mkdir -p /tmp/abnt-academico && \
cp -r SKILL.md CHANGELOG.md LICENSE references scripts /tmp/abnt-academico/ && \
(cd /tmp && zip -rq abnt-academico.zip abnt-academico -x "*/__pycache__/*") && \
mv /tmp/abnt-academico.zip dist/abnt-academico.zip
```

## Contribuindo

Encontrou algo desatualizado ou quer sugerir melhoria? Abra uma **Issue** ou envie um **Pull Request**.

## Licença

Distribuído sob a licença MIT. Veja o arquivo [LICENSE](LICENSE).
