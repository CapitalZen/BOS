#!/usr/bin/env python3
"""Vérifie l'intégrité des références croisées de BOS.

Les fichiers Knowledge/, Core/ et les skills se citent mutuellement en
permanence (`Knowledge/X.md §3`). Un renommage casse ces liens en silence.
Ce script les vérifie. Inspiré des scripts/checks du dépôt jarvis-skills.

Usage : python3 scripts/check_refs.py
Sortie : code 0 si tout est intègre, 1 sinon.
"""
import glob
import os
import re
import sys

SOURCES = (
    glob.glob("Knowledge/*.md")
    + glob.glob(".claude/skills/*/SKILL.md")
    + glob.glob("Core/*.md")
    + ["CLAUDE.md"]
)

PATTERNS = [
    r"`((?:Knowledge|Core|Output)/[A-Za-z0-9_./-]+\.md)`",
    r"`(\.claude/skills/[a-z-]+/SKILL\.md)`",
]


def main():
    refs = {}
    for f in SOURCES:
        if not os.path.exists(f):
            continue
        txt = open(f, encoding="utf8").read()
        for pat in PATTERNS:
            for target in re.findall(pat, txt):
                refs.setdefault(target, set()).add(f)

    missing = {k: v for k, v in refs.items() if not os.path.exists(k)}

    # Les skills listés dans le routage de CLAUDE.md existent-ils ?
    claude = open("CLAUDE.md", encoding="utf8").read()
    routed = set(re.findall(r"^- `([a-z-]+)` — ", claude, re.M))
    on_disk = {os.path.basename(os.path.dirname(p))
               for p in glob.glob(".claude/skills/*/SKILL.md")}
    ghosts = routed - on_disk

    print(f"{len(refs)} références de fichiers · {len(routed)} skills routés dans CLAUDE.md")

    if not missing and not ghosts:
        print("OK — aucune référence cassée, aucun skill fantôme.")
        return 0

    for k, v in sorted(missing.items()):
        print(f"\nCASSÉ : {k}")
        for src in sorted(v):
            print(f"   cité dans {src}")
    for g in sorted(ghosts):
        print(f"\nSKILL FANTÔME : `{g}` est routé dans CLAUDE.md mais absent de .claude/skills/")
    return 1


if __name__ == "__main__":
    sys.exit(main())
