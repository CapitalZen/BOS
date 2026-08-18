#!/usr/bin/env python3
"""Recherche dans la base de connaissance BOS, avec traçabilité obligatoire.

Ce que cet outil garantit, et qui est le point important :

1. **Il ne choisit jamais à la place de BOS.** Il renvoie N candidats
   classés, chacun avec son score, son fichier, son chemin de titres et
   sa date de revue. Le choix est ensuite explicite et citable.

2. **Il signale l'ambiguïté au lieu de la masquer.** Quand les deux
   premiers scores sont proches, la réponse est marquée AMBIGUË : deux
   sections différentes répondent, il faut lire les deux.

3. **Il admet quand il ne sait pas.** Sous un seuil de pertinence, le
   verdict est INSUFFISANT — la consigne est alors de lire le fichier
   directement, jamais de répondre depuis un extrait faible.

4. **Il élargit la requête au vocabulaire métier.** « fournisseur » et
   « agent » désignent la même chose selon les sources ; sans expansion,
   la moitié des sections pertinentes reste invisible.

Usage :
    python3 scripts/kb_query.py "comment négocier avec un agent chinois"
    python3 scripts/kb_query.py --n 8 "hook créative trois secondes"
"""
import argparse
import json
import os
import re
import sqlite3
import sys

DB = "scripts/kb_index.sqlite"
SYN = "scripts/kb_synonyms.json"

STOP = {
    "le", "la", "les", "de", "des", "du", "un", "une", "et", "ou", "a", "à",
    "au", "aux", "en", "je", "tu", "il", "on", "que", "qui", "quoi", "pour",
    "avec", "dans", "sur", "est", "sont", "ce", "cette", "mon", "ma", "mes",
    "comment", "pourquoi", "quel", "quelle", "faire", "fait", "plus", "pas",
    "the", "of", "to", "and", "is", "it",
}

AMBIGU_RATIO = 0.90   # top2/top1 au-dessus → deux réponses concurrentes
SEUIL_FAIBLE = 0.55   # score normalisé du meilleur en dessous → insuffisant


def expand(query):
    syn = json.load(open(SYN, encoding="utf8"))
    words = [w for w in re.findall(r"\w+", query.lower()) if w not in STOP and len(w) > 2]
    out = list(words)
    for w in words:
        out.extend(syn.get(w, []))
    seen, uniq = set(), []
    for w in out:
        if w not in seen:
            seen.add(w)
            uniq.append(w)
    return words, uniq


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("query")
    ap.add_argument("--n", type=int, default=5)
    args = ap.parse_args()

    if not os.path.exists(DB):
        print("Index absent — lancer d'abord : python3 scripts/kb_index.py")
        return 2

    base, terms = expand(args.query)
    # OR sur les termes étendus ; le classement fera le tri.
    fts = " OR ".join(f'"{t}"' for t in terms)

    con = sqlite3.connect(DB)
    try:
        rows = con.execute(
            "SELECT heading, body, file, line, rev, "
            # le titre pèse 8x le corps : une section INTITULÉE « négocier
            # avec un agent » répond mieux qu'une qui mentionne le mot au détour
            "  bm25(kb, 8.0, 1.0) AS score "
            "FROM kb WHERE kb MATCH ? ORDER BY score LIMIT ?",
            (fts, args.n),
        ).fetchall()
    except sqlite3.OperationalError as e:
        print(f"Requête invalide : {e}")
        return 2
    con.close()

    if not rows:
        print(f'AUCUN RÉSULTAT pour « {args.query} »')
        print("→ Consigne : lire directement le document pertinent. Ne pas répondre de mémoire.")
        return 1

    # ------------------------------------------------------------------
    # Reclassement explicite. BM25 sert au RAPPEL (ramener les candidats
    # plausibles) ; il est mauvais en PRÉCISION sur cette base, pour deux
    # raisons observées en test :
    #   - une section INTITULÉE « Négocier le MOQ » se faisait battre par
    #     une section plus longue qui répétait les mots au fil du texte ;
    #   - le glossaire, fait de définitions courtes, remontait sur des
    #     questions « comment faire », où il ne répond jamais.
    # Le reclassement corrige les deux, et chaque facteur est affiché pour
    # que le choix reste auditable.
    # ------------------------------------------------------------------
    def frac(mots, blob):
        blob = blob.lower().replace("’", "'")
        return sum(1 for w in mots if w in blob) / len(mots) if mots else 0.0

    veut_definition = bool(
        re.search(r"\b(c'est quoi|cest quoi|définition|definition|signifie|veut dire|acronyme)\b",
                  args.query.lower())
    )

    enrichi = []
    for heading, body, f, line, rev, sc in rows:
        bm = -sc
        h_cov = frac(base, heading)                      # titre = intention
        b_cov = frac(base, heading + " " + body)         # couverture réelle
        prior = 1.0
        motif = []
        if h_cov > 0:
            prior *= 1 + 1.2 * h_cov
            motif.append(f"titre {h_cov:.0%}")
        if "Glossaire" in f:
            prior *= 1.6 if veut_definition else 0.45
            motif.append("glossaire" + ("+" if veut_definition else "−"))
        enrichi.append({
            "heading": heading, "body": body, "file": f, "line": line,
            "rev": rev, "bm": bm, "h_cov": h_cov, "cov": b_cov,
            "final": bm * prior, "motif": ", ".join(motif) or "—",
        })

    enrichi.sort(key=lambda e: -e["final"])
    rows = [(e["heading"], e["body"], e["file"], e["line"], e["rev"], -e["final"])
            for e in enrichi]
    scores = [e["final"] for e in enrichi]
    top = scores[0]

    # --- Test de pertinence réel : la couverture des termes de la question ---
    # Le score BM25 brut ne dit RIEN de la pertinence absolue : il classe les
    # documents entre eux, il ne sait pas dire « aucun ne répond ». Sur une
    # question hors base, le premier résultat sort quand même à 100 %.
    # Le test qui décide est donc : combien des mots de la question posée
    # apparaissent réellement dans le passage trouvé ?
    def couverture(heading, body):
        blob = (heading + " " + body).lower()
        blob = blob.replace("’", "'")
        hits = sum(1 for w in base if w in blob)
        return hits / len(base) if base else 0.0

    cov = [e["cov"] for e in enrichi]
    cov_top = cov[0]

    if cov_top < 0.40:
        verdict = "INSUFFISANT"
        consigne = (f"Seuls {cov_top:.0%} des termes de la question apparaissent "
                    "dans le meilleur passage — la base ne couvre probablement "
                    "pas ce sujet. Lire le document concerné, ou le dire "
                    "franchement. NE PAS répondre depuis ces extraits.")
    elif len(scores) > 1 and scores[1] / top > AMBIGU_RATIO and cov[1] >= cov_top - 0.1:
        verdict = "AMBIGU"
        consigne = ("Deux sections répondent de façon comparable. Lire les "
                    "DEUX avant de trancher, et dire laquelle a été retenue.")
    elif cov_top < 0.65:
        verdict = "PARTIEL"
        consigne = (f"{cov_top:.0%} des termes seulement sont couverts — le "
                    "passage éclaire une partie de la question. Compléter "
                    "par une autre recherche ou par la lecture du fichier.")
    else:
        verdict = "NET"
        consigne = ("Citer le passage retenu avec son fichier et son titre "
                    "dans la réponse à l'entrepreneur.")

    print(f'Requête   : « {args.query} »')
    print(f'Termes    : {", ".join(base)}  (+{len(terms)-len(base)} synonymes)')
    print(f"Verdict   : {verdict}")
    print(f"Consigne  : {consigne}\n")

    for i, e in enumerate(enrichi, 1):
        rel = e["final"] / top * 100
        extrait = re.sub(r"\s+", " ", e["body"])[:280]
        print(f"[{i}] {rel:5.1f}%  couverture {e['cov']:3.0%}  ({e['motif']})")
        print(f"      {e['heading']}")
        print(f"      {e['file']}:{e['line']}"
              + (f"   revu {e['rev']}" if e["rev"] else "   ⚠ non daté"))
        print(f"      {extrait}…\n")

    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except BrokenPipeError:
        os._exit(0)
