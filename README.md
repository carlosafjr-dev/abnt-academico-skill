# Skill ABNT Acadêmico para Claude

Skill que aplica as normas ABNT (NBR 14724, NBR 10520, NBR 6023 e NBR 6022) diretamente no Claude.ai, cobrindo formatação, citações, referências bibliográficas e estrutura completa de trabalhos acadêmicos.

Criada por [Carlos Alberto Ferreira](https://github.com/carlosafjr) | [CAF Digital](mailto:carlosafjr@gmail.com)

---

## O que esta skill faz

Quando instalada, o Claude passa a:

- Formatar textos acadêmicos conforme as normas vigentes (2024/2026)
- Corrigir e orientar citações diretas, indiretas e por apud
- Montar referências bibliográficas de qualquer tipo de fonte
- Orientar sobre a estrutura completa de TCCs, monografias, artigos e dissertações
- Alertar quando há ambiguidade entre norma geral e regras da instituição

A skill é acionada automaticamente quando você menciona palavras como "ABNT", "TCC", "monografia", "citação", "referências", "NBR", "formatação acadêmica" etc.

---

## Estrutura do repositório

```
abnt-academico-skill/
├── SKILL.md                        # Arquivo principal da skill
└── references/
    ├── citacoes.md                 # NBR 10520 — citações diretas, indiretas, apud
    ├── estrutura.md                # NBR 14724 — estrutura completa do trabalho
    ├── formatacao-geral.md         # Margens, fonte, espaçamento, paginação
    └── referencias.md              # NBR 6023 — referências bibliográficas
```

---

## Como instalar no Claude.ai

### Pré-requisito

No momento, você precisa ter acesso ao plano **Pro** ou **Team** do Claude.ai, que permite o upload de skills customizadas.

### Passo a passo

1. **Baixe o repositório**

   Clique em **Code > Download ZIP** ou clone via terminal:

   ```bash
   git clone https://github.com/SEU_USUARIO/abnt-academico-skill.git
   ```

2. **Acesse o Claude.ai**

   Abra [claude.ai](https://claude.ai) e vá em **Settings** (ou Configurações).

3. **Localize a seção de Skills**

   Dentro das configurações, procure por **Skills** ou **Custom Skills** (o nome pode variar conforme a versão da interface).

4. **Faça o upload**

   Carregue a pasta completa `abnt-academico-skill/` como uma skill. O Claude precisa ter acesso tanto ao `SKILL.md` quanto à pasta `references/` com os quatro arquivos de módulo.

5. **Teste**

   Abra uma conversa nova e peça, por exemplo:

   > "Me ajuda a formatar essa citação conforme a ABNT."
   > "Como montar as referências do meu TCC?"
   > "Revise meu resumo segundo as normas ABNT."

   A skill deve ser acionada automaticamente.

---

## Cobertura das normas

| Norma | Conteúdo |
|---|---|
| NBR 14724 (2023) | Estrutura de trabalhos acadêmicos |
| NBR 10520 (2023) | Citações em documentos |
| NBR 6023 (2018) | Referências bibliográficas |
| NBR 6022 | Artigos científicos |
| NBR 6027 | Sumários |
| NBR 6028 | Resumos |

> As normas são recomendações gerais. Cada instituição pode ter variações próprias. Oriente-se também pelo manual da sua faculdade ou com seu orientador.

---

## Limitações conhecidas

- A skill não substitui revisão humana por um orientador ou bibliotecário especializado.
- Normas ABNT são atualizadas periodicamente. Verifique se a versão da sua instituição está alinhada com a versão coberta aqui (2024/2026).
- Para variações institucionais muito específicas (ex: normas internas de certas faculdades), o Claude irá alertar e pedir confirmação antes de aplicar.

---

## Contribuindo

Encontrou algo desatualizado ou quer sugerir melhoria? Abra uma **Issue** ou envie um **Pull Request**. Contribuições são bem-vindas.

---

## Licença

Distribuído sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
