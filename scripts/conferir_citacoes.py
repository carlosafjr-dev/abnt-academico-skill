#!/usr/bin/env python3
"""Confere citações (sistema autor-data, ABNT NBR 10520:2023) contra a lista de referências.

Uso:
    python conferir_citacoes.py trabalho.docx|.txt|.md [--json]

O que verifica:
  - chamadas no texto sem referência correspondente (sobrenome + ano)
  - referências que nunca são citadas
  - chamadas no formato antigo em caixa alta, ex. (SILVA, 2020), quando SILVA é pessoa
  - "s.p." ou "online" na chamada (a norma pede só o ano)
  - em .docx: "et al.", "apud", "In:" sem itálico
  - referências online sem "Acesso em", URL entre < >, DOI fora do formato https://doi.org/

É um apoio heurístico: confira cada achado antes de reportar. Sobrenomes compostos,
entidades e títulos podem gerar falso positivo.
"""
import json
import re
import sys
import unicodedata
import zipfile
from pathlib import Path

YEAR = r"(?:1[5-9]\d{2}|20\d{2})"
YEAR_TOKEN = re.compile(r"\[?(" + YEAR + r")([a-z])?\??\]?")
REF_HEADINGS = re.compile(r"^\s*(REFER[ÊE]NCIAS|REFER[ÊE]NCIAS BIBLIOGR[ÁA]FICAS|BIBLIOGRAFIA|REFERENCES)\s*$", re.I)
END_HEADINGS = re.compile(r"^\s*(AP[ÊE]NDICE|ANEXO|GLOSS[ÁA]RIO|[ÍI]NDICE)\b", re.I)
UPPER = "A-ZÀ-ÖØ-Þ"
WORD = r"[A-ZÀ-ÖØ-Þ][\wÀ-ÿ'’\-]*"


def norm(s):
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9 ]", "", s.lower()).strip()


def read_paragraphs(path):
    """Devolve lista de (texto, runs) onde runs = [(texto, italico)] ou None."""
    p = Path(path)
    if p.suffix.lower() == ".docx":
        try:
            import docx  # python-docx
            d = docx.Document(str(p))
            out = []
            for para in d.paragraphs:
                runs = [(r.text, bool(r.italic) or bool(para.style and para.style.font and para.style.font.italic)) for r in para.runs]
                out.append((para.text, runs))
            return out
        except ImportError:
            with zipfile.ZipFile(p) as z:
                xml = z.read("word/document.xml").decode("utf8")
            out = []
            for para in re.findall(r"<w:p[ >].*?</w:p>", xml, re.S):
                runs = []
                for r in re.findall(r"<w:r[ >].*?</w:r>", para, re.S):
                    t = "".join(re.findall(r"<w:t[^>]*>(.*?)</w:t>", r, re.S))
                    runs.append((t, "<w:i/>" in r or '<w:i w:val="1"/>' in r or '<w:i w:val="true"/>' in r))
                out.append(("".join(t for t, _ in runs), runs))
            return out
    text = p.read_text(encoding="utf8", errors="replace")
    return [(line, None) for line in text.splitlines()]


def split_sections(paras):
    body, refs, in_refs = [], [], False
    for text, runs in paras:
        if REF_HEADINGS.match(text):
            in_refs = True
            continue
        if in_refs and END_HEADINGS.match(text):
            in_refs = False
            continue
        (refs if in_refs else body).append((text, runs))
    return body, refs


def parse_references(refs):
    entries = []
    for text, runs in refs:
        t = text.strip()
        if len(t) < 15:
            continue
        head = re.split(r"[,.]", t, maxsplit=1)[0].strip()
        first_word = head.split()[0] if head.split() else head
        is_person = bool(re.match(r"^[" + UPPER + r"\- ]+,\s*[" + UPPER + r"]", t)) and head.isupper()
        main = re.split(r"Acesso em", t, maxsplit=1)[0]
        years = {m.group(1) + (m.group(2) or "") for m in YEAR_TOKEN.finditer(main)}
        years |= {m.group(1) for m in YEAR_TOKEN.finditer(main)}
        entries.append({
            "texto": t,
            "entrada": head,
            "chaves": {norm(head), norm(first_word)},
            "anos": years,
            "pessoa": is_person,
        })
    return entries


def parse_citations(body):
    cits = []
    full = "\n".join(t for t, _ in body)
    # parentéticas: (Silva, 2020, p. 4; Souza; Lima, 2021)
    for m in re.finditer(r"\(([^()]*?" + YEAR + r"[^()]*)\)", full):
        inner = m.group(1)
        pending = []
        for seg in inner.split(";"):
            seg = seg.strip()
            ym = YEAR_TOKEN.search(seg)
            if not ym:
                pending.append(seg)
                continue
            first_author = pending[0] if pending else None
            pending = []
            # "Olson, 1977, p. 23 apud Smith, 1991" -> duas chamadas
            for idx, part in enumerate(re.split(r"\bapud\b", seg)):
                pm = YEAR_TOKEN.search(part)
                if not pm:
                    continue
                a = part[: pm.start()].strip().rstrip(",").strip()
                if idx == 0 and first_author:
                    a = first_author
                if not a or not re.match(r"^[" + UPPER + r"]", a):
                    continue
                a = re.sub(r"\s+et al\.?$", "", a).strip()
                cits.append({"autor": a.split(";")[0].strip(), "ano": pm.group(1) + (pm.group(2) or ""),
                             "trecho": m.group(0)[:120],
                             "original_apud": idx == 0 and "apud" in seg})
    # narrativas: Silva (2020), Silva e Souza (2020), Lima et al. (2019)
    for m in re.finditer(r"(" + WORD + r")(?:,\s*" + WORD + r")*(?:\s+e\s+" + WORD + r")?(?:\s+et al\.?)?\s+\((\[?" + YEAR + r"[a-z]?\]?)", full):
        a = m.group(1)
        if a.lower() in {"em", "no", "na", "de", "do", "da", "o", "a", "os", "as", "lei", "figura", "tabela", "quadro", "gráfico"}:
            continue
        y = YEAR_TOKEN.search(m.group(2))
        cits.append({"autor": a, "ano": y.group(1) + (y.group(2) or ""), "trecho": m.group(0)[:120]})
    return cits, full


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    paras = read_paragraphs(sys.argv[1])
    body, refs = split_sections(paras)
    if not refs:
        print("Aviso: seção REFERÊNCIAS não encontrada (título sozinho numa linha).")
    entries = parse_references(refs)
    cits, full = parse_citations(body)

    numeric = len(re.findall(r"\[\d{1,3}\]", full))
    report = {"sem_referencia": [], "nao_citadas": [], "formato_antigo": [], "chamada_com_sp": [],
              "sem_italico": [], "referencias_online": [], "aviso": []}
    if numeric > 10 and len(cits) < numeric:
        report["aviso"].append("O texto parece usar sistema numérico; este script confere autor-data.")

    used = set()
    for c in cits:
        key = norm(c["autor"].split()[0]) if c["autor"].split() else ""
        key_full = norm(c["autor"])
        year = c["ano"]
        hit = None
        for i, e in enumerate(entries):
            if (key in e["chaves"] or key_full in e["chaves"] or any(k.startswith(key_full) for k in e["chaves"] if key_full)) and (year in e["anos"] or year[:4] in e["anos"]):
                hit = i
                break
        if hit is None and c.get("original_apud"):
            continue
        if hit is None:
            report["sem_referencia"].append(f'{c["autor"]}, {year}  ← {c["trecho"]}')
        else:
            used.add(hit)
        if c["autor"].isupper() and len(c["autor"]) > 2:
            if any(e["pessoa"] and norm(c["autor"]) in e["chaves"] for e in entries):
                report["formato_antigo"].append(c["trecho"])

    for i, e in enumerate(entries):
        if i not in used:
            report["nao_citadas"].append(e["texto"][:160])

    for m in re.finditer(r"\([^()]*(\bs\.\s?p\.|\bonline\b)[^()]*\)", full, re.I):
        report["chamada_com_sp"].append(m.group(0)[:120])

    for text, runs in body + refs:
        if not runs:
            continue
        for rt, ital in runs:
            for term in ("et al", "apud", "In:"):
                if term in rt and not ital:
                    report["sem_italico"].append(f'"{term}" sem itálico em: {text[:100]}')

    for e in entries:
        t = e["texto"]
        if "Disponível em" in t and "Acesso em" not in t:
            report["referencias_online"].append("Sem 'Acesso em': " + t[:140])
        if re.search(r"Disponível em:\s*<", t):
            report["referencias_online"].append("URL entre < >: " + t[:140])
        if re.search(r"DOI:?\s*10\.", t):
            report["referencias_online"].append("DOI fora do formato https://doi.org/: " + t[:140])

    report["sem_referencia"] = sorted(set(report["sem_referencia"]))
    report["formato_antigo"] = sorted(set(report["formato_antigo"]))
    report["sem_italico"] = sorted(set(report["sem_italico"]))

    if "--json" in sys.argv:
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return
    titles = {
        "aviso": "Avisos",
        "sem_referencia": "Chamadas sem referência correspondente",
        "nao_citadas": "Referências não citadas no texto",
        "formato_antigo": "Chamadas em caixa alta (formato da norma antiga)",
        "chamada_com_sp": "Chamadas com s.p. ou online",
        "sem_italico": "Expressões que deveriam estar em itálico",
        "referencias_online": "Problemas em referências online",
    }
    print(f"Chamadas encontradas: {len(cits)} | Referências encontradas: {len(entries)}\n")
    for k, title in titles.items():
        items = report[k]
        print(f"## {title} ({len(items)})")
        for it in items[:200]:
            print(f"- {it}")
        print()


if __name__ == "__main__":
    main()
