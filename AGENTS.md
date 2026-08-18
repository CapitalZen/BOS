# AGENTS.md — contrat de BOS avec lui-même

*Repris de l'`AGENTS.md` de `CapitalZen/jarvis-skills`, adapté. BOS modifie ses propres fichiers à chaque session — règles, playbooks, skills, état du business. Sans contrat explicite, l'auto-modification dérive : la base grossit plus vite qu'elle ne s'améliore.*

## Règles absolues

### 1. Vérifier avant de terminer une session qui a créé ou renommé des fichiers
```bash
python3 scripts/check_refs.py
```
Références cassées ou skill fantôme → corriger avant de clore.

### 2. Enrichir un document existant plutôt qu'en créer un nouveau
Avant toute création dans `Knowledge/` : `grep -ril "<sujet>" Knowledge/`. Un domaine déjà couvert s'enrichit ; il ne se duplique pas. **Le nombre de documents n'est pas une mesure de valeur.**

### 3. Situer toute donnée chiffrée sur l'échelle de fiabilité
`Knowledge/Source_Tiers.md` avant d'inscrire un chiffre où que ce soit. Pas de dénominateur = pas de chiffre.

### 4. Corriger explicitement, jamais en silence
Une donnée fausse se remplace **avec la mention de ce qu'elle remplace**. La trace de l'erreur empêche de refaire le chemin. Vaut pour les erreurs de BOS comme pour celles de ses sources.

### 5. Écrire le motif, pas seulement la conclusion
« Écarté » ne vaut rien. « Écarté parce que [motif structurel nommé] » évite que la question revienne.

### 6. Ne jamais ajouter une règle à `CLAUDE.md` sans déclencheur réel
Une règle s'ajoute quand l'entrepreneur corrige BOS ou qu'une erreur s'est produite — pas par anticipation. `CLAUDE.md` est lu à chaque session : chaque ligne inutile coûte de l'attention à toutes les suivantes.

### 7. Ne jamais présenter comme vérifié ce qui ne l'a pas été
Si une page n'a pas pu être lue, l'écrire. Si un comptage n'a pas pu être fait, l'écrire. Une limite déclarée vaut mieux qu'une conclusion inventée — le registre est `Knowledge/Known_Limitations.md`.

### 8. Un livrable produit se date et s'enregistre
`Output/Nom_Explicite_AAAA-MM-JJ.md`, et mention dans `Core/Actions.md` ou `Core/Journal.md`. Un livrable qui n'est référencé nulle part est perdu.

### 9. Ne pas produire davantage quand rien n'a été mesuré
Quand plusieurs livrables s'accumulent sans qu'aucun n'ait rencontré le réel, la production supplémentaire a un rendement décroissant. Le dire plutôt que de continuer.

### 10. Respecter les règles de posture de `CLAUDE.md`
Notamment : nommer un pattern d'évitement **une seule fois** puis lâcher, et ne jamais exposer la mécanique interne (routage, lecture de fichiers, chargement de skills).

## Ce qui ne s'automatise pas

`check_refs.py` valide les liens et la présence des dates de revue. Il ne valide **pas** la cohérence de fond entre documents — un playbook peut contredire un autre sans qu'aucun test ne le voie. Cette vérification reste à la charge de BOS au moment de l'usage (`Knowledge/Known_Limitations.md` §7).

**Dernière revue :** 2026-08-17
