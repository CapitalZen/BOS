#!/usr/bin/env python3
"""Construit l'index de recherche de la base de connaissance BOS.

Le découpage n'est PAS aveugle : chaque chunk est une section complète
(délimitée par ## ou ###), avec son chemin de titres conservé. Le titre
d'une section est le signal le plus fort de ce dont elle parle — il est
donc indexé séparément et pondéré fortement à la requête.

Chaque chunk porte sa provenance (fichier, titres, lignes) et la date de
dernière revue du document, pour que la sortie de recherche permette de
juger la fraîcheur sans rouvrir le fichier.

Usage : python3 scripts/kb_index.py
"""
import glob
import os
import re
import sqlite3
import sys

DB = "scripts/kb_index.sqlite"
# Skills métier BOS uniquement : les skills de design (brandkit, imagegen,
# minimalist-ui…) sont des instructions de rendu, pas de la connaissance
# business — les indexer polluerait chaque recherche.
BOS_SKILLS = ["find", "traffic", "offer", "funnel", "mindset", "chase",
              "digestion", "organize", "diagnosis", "onboard", "teardown"]
SOURCES = sorted(glob.glob("Knowledge/*.md")) + [
    f".claude/skills/{s}/SKILL.md" for s in BOS_SKILLS
]
MIN_CHARS = 120  # en dessous, la section est un simple titre de transition


def review_date(text):
    m = re.search(r"\*\*Dernière revue :\*\*\s*([\d-]+)", text)
    return m.group(1) if m else ""


def chunk(path):
    """Découpe un markdown en sections, en gardant le chemin de titres."""
    text = open(path, encoding="utf8").read()
    rev = review_date(text)
    lines = text.split("\n")

    doc_title = os.path.basename(path).replace(".md", "")
    if doc_title == "SKILL":
        doc_title = "skill:" + os.path.basename(os.path.dirname(path))

    out, h2, h3 = [], "", ""
    buf, start = [], 1

    def flush(end):
        body = "\n".join(buf).strip()
        if len(body) >= MIN_CHARS:
            path_parts = [doc_title] + [p for p in (h2, h3) if p]
            out.append(
                {
                    "file": path,
                    "doc": doc_title,
                    "heading": " > ".join(path_parts),
                    "body": body,
                    "line": start,
                    "rev": rev,
                }
            )

    for i, ln in enumerate(lines, 1):
        m2 = re.match(r"^##\s+(?!#)(.+)", ln)
        m3 = re.match(r"^###\s+(?!#)(.+)", ln)
        if m2 or m3:
            flush(i - 1)
            buf, start = [], i
            if m2:
                h2, h3 = m2.group(1).strip(), ""
            else:
                h3 = m3.group(1).strip()
        else:
            buf.append(ln)
    flush(len(lines))
    return out


def main():
    if os.path.exists(DB):
        os.remove(DB)
    con = sqlite3.connect(DB)
    con.execute(
        "CREATE VIRTUAL TABLE kb USING fts5("
        "heading, body, file UNINDEXED, doc UNINDEXED, "
        "line UNINDEXED, rev UNINDEXED, tokenize='unicode61 remove_diacritics 2')"
    )

    total = 0
    for path in SOURCES:
        if not os.path.exists(path):
            continue
        for c in chunk(path):
            con.execute(
                "INSERT INTO kb (heading, body, file, doc, line, rev) "
                "VALUES (?,?,?,?,?,?)",
                (c["heading"], c["body"], c["file"], c["doc"], c["line"], c["rev"]),
            )
            total += 1
    con.commit()

    undated = con.execute(
        "SELECT DISTINCT doc FROM kb WHERE rev = ''"
    ).fetchall()
    con.close()

    print(f"{total} sections indexées depuis {len(SOURCES)} documents → {DB}")
    if undated:
        print(f"⚠️  {len(undated)} document(s) sans date de revue : "
              + ", ".join(u[0] for u in undated))
    return 0


if __name__ == "__main__":
    sys.exit(main())
