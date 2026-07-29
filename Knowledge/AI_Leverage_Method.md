# Méthode — Piloter une IA comme les 5 % qui vont 10× plus vite

Comment obtenir d'une IA un travail réellement délégable. Sert deux usages : (1) BOS applique ces règles à lui-même dans ses interactions avec l'entrepreneur, (2) BOS les enseigne quand l'entrepreneur veut équiper son business ou ses clients.

*Distillé de : « La Méthode · d'après Andrej Karpathy ».*

---

## Le déclic

L'IA a changé de nature récemment, et la plupart des gens l'utilisent encore avec les réflexes d'il y a deux ans.
**Avant :** outil peu fiable, à corriger ligne par ligne. **Maintenant :** assez fiable pour qu'on lui confie de vrais morceaux de travail — *à condition de l'encadrer.* Résultat : un outil surpuissant exploité à 10 % de sa valeur.

## Comprendre la bête

Une IA est **un stagiaire surdoué** : mémoire et culture immenses, jugement nul. La pousser (« fais mieux ») ne sert à rien. La seule chose qui marche, c'est l'encadrement.

**Le faux problème : le prompt.** Quand la réponse est moyenne, on cherche la formule magique. Mais le prompt pèse peu. **Le vrai levier c'est le contexte** — qui vous êtes, l'objectif, les contraintes, les exemples. Demander une page de vente sans parler de son produit, de ses clients ni de son style, c'est demander au stagiaire de deviner. Et deviner, ça rate.

Trois techniques, dans cet ordre.

## Technique 1 — Lui donner une mémoire

Par défaut, chaque conversation repart de zéro. Les pros construisent une mémoire qu'ils maîtrisent : un espace persistant où ils décident au mot près ce que l'IA sait.

**À remplir une fois :**
```
Qui je suis : [métier, entreprise]
Ce que je fais : [offre, type de clients]
Mon ton : [3 adjectifs]
Mes règles : toujours [X], jamais [Y]
Réponds toujours dans ce cadre, sans me le redemander.
```
Y déposer aussi ses meilleurs livrables passés. Plus la mémoire est nourrie, plus la sortie est précise.

**C'est exactement ce que sont les fichiers `Core/` de BOS** — la mémoire tenue du business. Argument à donner à l'entrepreneur : « Ce que les gens font à la main dans un Projet, ton BOS le tient à jour tout seul. »

## Technique 2 — Cadrer comme un brief

Arrêter les demandes vagues. Un bon brief (une « spec ») répond à 4 questions :

| | Question | Contenu |
|---|---|---|
| 01 | **Objectif** | Le résultat visé, pas la tâche |
| 02 | **Contexte** | Ce qu'il doit savoir pour ne pas deviner |
| 03 | **Contraintes** | Ton, format, longueur, interdits |
| 04 | **Méthode** | D'un coup, ou par étapes à valider ? |

*Exemple (agent immobilier) — Objectif : un maximum de visites qualifiées. Contexte : appartement familial, quartier calme. Contraintes : chaleureux, jamais racoleur, 150 mots max. Méthode : proposer l'accroche, valider, puis rédiger.*

**Le prompt « interroge-moi »** — à utiliser quand on ne sait pas cadrer :
> « Avant de produire quoi que ce soit, pose-moi des questions pour cerner mon objectif. Ensuite, liste les décisions importantes et fais-les-moi valider avant de te lancer. »

Le rôle de l'humain n'est pas de rédiger — c'est de **décider**.

## Technique 3 — Rendre le résultat vérifiable (la plus puissante)

**Règle d'or : plus on donne à l'IA un moyen de vérifier son travail, meilleure elle devient.** Deux niveaux :

- **Niveau 1 — elle se relit.** Critères précis + relecture explicite : *« Avant la version finale, vérifie point par point que chaque critère est respecté. »* Utile, mais elle reste juge et partie.
- **Niveau 2 — le réel tranche.** Le meilleur juge, ce sont les données : clics, appels, ventes, réponses. *« Voici les résultats de mes 3 dernières annonces. Écris la prochaine dans l'esprit de ce qui a marché. »*

**Le piège où tout le monde tombe :** lancer la machine et disparaître. L'IA fait le travail, l'humain garde la trajectoire.

**Le « réel » selon le métier :** coach/formateur → messages reçus, appels réservés. E-commerce → ajouts au panier, ventes. Restaurateur → ouvertures d'email, réservations. Prestataire de services → réponses aux messages de prospection, RDV pris.

## Bibliothèque de prompts

1. **Angles morts** — « Avant d'exécuter, dis-moi les 3 angles morts de ma demande et pose-moi les questions qui te manquent. »
2. **Deux versions à tester** — « Propose 2 versions volontairement différentes (angle A vs angle B) pour que je les teste sur le réel. »
3. **Relecture du client sceptique** — « Relis ce texte comme mon client cible, pressé et sceptique. À quelle ligne décroche-t-il, et pourquoi ? »
4. **Apprendre du réel** — « Voici les résultats de mes 3 derniers [livrables]. Déduis 3 règles de ce qui marche chez moi, puis applique-les. »
5. **Mettre à jour la mémoire** — « Résume ce qu'on a décidé ici en 5 lignes que je collerai dans les instructions de mon Projet. »
6. **Rester dans la boucle** — « Avance par étapes. À chaque étape, montre-moi ton résultat et attends mon feu vert avant de continuer. »

## Dépannage

| Symptôme | Ce qui manque | Le réflexe |
|----------|---------------|-----------|
| « Réponses trop génériques » | Le contexte | Enrichir la mémoire : ton, exemples, meilleurs livrables passés |
| « Il part dans tous les sens » | Le cadrage | Faire un brief (4 questions), demander le mode étape par étape |
| « Toujours à côté de la plaque » | Le critère de réussite | Donner des critères précis, puis laisser le réel trancher |
| « Il invente ou se trompe sur un détail » | La vérification | Faire vérifier point par point, rester dans la boucle |

## La limite

> « Vous pouvez déléguer votre réflexion, mais pas votre compréhension. »

L'IA peut écrire, chercher, exécuter à la place de l'entrepreneur. Pas comprendre à sa place ce qui compte. L'objectif n'est pas de devenir expert du prompt — c'est de devenir le meilleur pilote de son IA.

**Implication pour BOS :** ne jamais laisser l'entrepreneur sortir d'une session avec un livrable qu'il ne comprend pas. Et systématiquement fermer la boucle de vérification — après chaque livrable envoyé dans le réel (message, page, publicité, offre), demander les chiffres au retour et les réinjecter. C'est ce qui transforme BOS d'un générateur de contenu en système qui apprend le business.
