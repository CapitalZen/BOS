# Protocole de maintenance de BOS

*Repris du `Documentation_Helper/MAINTENANCE.md` de `CapitalZen/jarvis-os`. BOS se modifie lui-même en permanence — sans déclencheurs explicites, la base dérive : un skill enrichi dont le playbook de référence n'est pas mis à jour, un fichier `Core/` qui contredit un autre, un document qu'on croit à jour et qui date de trois semaines.*

## Déclencheurs de mise à jour

| Ce qui change | Ce qu'il faut mettre à jour |
|---|---|
| L'entrepreneur donne un fait nouveau sur son business | `Core/Business.md` + entrée `Core/Journal.md` |
| Une action est faite, ou ne l'est pas | `Core/Actions.md` (tableau résultats) + `Core/Diagnosis.md` si ça révèle un blocage |
| Un problème est résolu ou apparaît | `Core/Diagnosis.md` (résolu → historique daté, nouveau → Impact/Preuves/Cause) |
| L'entrepreneur corrige BOS | **Règle ajoutée dans `CLAUDE.md`** (protocole §14) + entrée Journal |
| Un chiffre entre dans la base | Vérifier le tier dans `Knowledge/Source_Tiers.md`, écrire la source et le dénominateur |
| Une source nouvelle apporte une méthode | Le playbook `Knowledge/` concerné — **pas un nouveau fichier** si un existant couvre le domaine |
| Un skill est créé ou renommé | Le routage dans `CLAUDE.md` (deux endroits : liste courte §routing + section `.claude/skills/`) + `Knowledge/INDEX.md` |
| Un document `Knowledge/` est créé | `Knowledge/INDEX.md` + le sommaire des Knowledge dans `CLAUDE.md` |
| Une limite de BOS est découverte | `Knowledge/Known_Limitations.md` |
| Un livrable est produit | `Output/` avec date dans le nom + mention dans `Core/Actions.md` ou `Journal.md` |
| Une piste est écartée | **Le motif, pas seulement la conclusion** — sinon la question revient dans trois mois |

## Règles de fond

1. **Enrichir avant de créer.** Un nouveau fichier `Knowledge/` ne se justifie que si aucun existant ne couvre le domaine. Vérifier d'abord avec `grep -ril "<sujet>" Knowledge/`.
2. **Corriger explicitement, jamais en silence.** Quand une donnée s'avère fausse, écrire la correction **et** ce qu'elle remplace. La trace de l'erreur vaut mieux que sa disparition — c'est ce qui empêche de refaire le même chemin.
3. **Le motif prime sur la conclusion.** « Segment écarté » ne vaut rien ; « segment écarté parce que bien servi **et** hors de portée d'un sourcing 1688 » évite de reposer la question.
4. **Dater les revues.** Chaque document `Knowledge/` porte une ligne `**Dernière revue :** AAAA-MM-JJ` en pied.

## Vérifications

```bash
python3 scripts/check_refs.py    # références croisées + skills fantômes + fraîcheur
```

À lancer après toute session qui a créé ou renommé des fichiers.

## Ce qui n'est volontairement pas automatisé

La **cohérence de fond** entre documents. `check_refs.py` valide que les liens pointent quelque part ; il ne peut pas voir qu'un playbook affirme une chose et qu'un autre affirme le contraire. Cette vérification reste à la charge de BOS au moment de l'usage — c'est la limite n°7 de `Knowledge/Known_Limitations.md`.

**Dernière revue :** 2026-08-17
