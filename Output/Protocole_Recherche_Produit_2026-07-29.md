# Protocole de recherche produit — version exécutable

**Date :** 29/07/2026
**Pour :** débloquer la recherche produit, déclarée comme blocage principal
**Principe :** la recherche produit n'est pas un talent, c'est une procédure avec un début, une fin et un critère d'arrêt. Ce document la rend bornée dans le temps.

---

## Pourquoi ça bloque (et pourquoi ce n'est pas ta faute)

Trois raisons, aucune n'est un défaut personnel :

1. **Aucun produit n'est garanti.** Même à plusieurs millions de CA, personne ne sait à l'avance si un test va marcher. Si le critère de décision est « être sûr », la décision n'arrive jamais.
2. **Il n'y a pas de critère d'arrêt naturel.** On peut toujours regarder un produit de plus. Sans limite définie, la recherche devient infinie — donc anxiogène.
3. **C'est la partie la plus délégable du process**, et pourtant celle qu'on porte seul.

**La correction :** un nombre de candidats, une deadline, une grille de score. On prend le meilleur du lot **même s'il n'est pas parfait** — parce que le terrain tranche, pas l'analyse.

## Le critère d'arrêt (à graver)

> **10 candidats analysés maximum. 5 jours maximum. À la fin : le meilleur score part en test.**
> Si aucun candidat n'atteint le score minimum, on refait un cycle — mais on ne prolonge jamais le cycle en cours.

## Étape 1 — Sourcing des candidats (60 min)

**Ce qu'on cherche : des boutiques dont la dépense publicitaire est en croissance sur les dernières semaines.** Pas des produits « intéressants ». Le signal, c'est l'argent que quelqu'un d'autre met déjà.

**Sources gratuites, dans l'ordre d'efficacité :**

1. **Meta Ad Library** (gratuit, sans compte) — filtrer par pays (France, Italie, Espagne), catégorie « toutes les annonces ». Chercher des marques inconnues avec beaucoup d'annonces actives et des dates de lancement récentes. Le nombre d'annonces actives et leur date de mise en ligne sont visibles sans aucun outil payant.
2. **TikTok Creative Center** (gratuit) — top ads par pays et par secteur, avec tendances de croissance.
3. **Fil « Pour toi » TikTok / Reels entraîné volontairement** — interagir avec des pubs produits pendant 2-3 jours entraîne l'algorithme à en montrer davantage. Gratuit, et remarquablement efficace.
4. **Amazon Movers & Shakers / Best Sellers** par catégorie — indique la demande, pas la dépense publicitaire. À croiser, jamais à utiliser seul.
5. Outils payants (TrendTrack, Minea, AdSpy) — utiles pour lire le spend estimé et les courbes d'annonces actives. **Non indispensables pour le premier cycle** : l'Ad Library donne déjà le volume et l'antériorité.

⚠️ **Ce qu'on n'utilise pas :** les listes « top 10 produits gagnants 2026 » des blogs et des sites d'outils. Ces listes sont vues par des dizaines de milliers de personnes, elles décrivent des produits déjà surexploités, et elles ne portent aucune donnée de dépense. Chercher là, c'est arriver dernier.

**Sortie de l'étape 1 :** une liste brute de 10 produits, avec pour chacun le nom de la boutique, le lien Ad Library, le nombre d'annonces actives et la date de la plus ancienne annonce.

## Étape 2 — Scoring (15 min pour les 10)

Note chaque candidat sur les 4 critères. **Un critère à 0 est éliminatoire, quel que soit le total.**

| Critère | 0 | 1 | 2 |
|---|---|---|---|
| **Marge** (prix de vente constaté ÷ coût estimé produit+livraison) | < x3 | x3 à x4,5 | > x4,5 |
| **Demande croissante** | Annonces stables ou en baisse | Croissance visible depuis < 2 mois | Croissance forte et continue depuis 2-3 mois |
| **Time-to-market** | Produit installé depuis > 1 an, courbe plate | Produit récent mais signal faible | Explosion < 3 mois, ou saisonnalité qui se répète |
| **Contenu disponible** | Rien n'existe, tout à produire | Quelques vidéos exploitables comme référence | Beaucoup de contenu organique sur le produit |

**Bonus — les 5 raisons d'achat.** Compter combien le produit en coche : résout un problème · facilite la vie · fait gagner de l'argent · élève le statut · réunit une communauté.
**0 raison cochée = élimination immédiate**, quel que soit le score. Chaque raison cochée est un angle de test différent, donc un actif.

**Seuil de passage : 6/8 minimum, aucun 0, au moins 2 raisons d'achat.**

## Étape 3 — Vérification concurrentielle (20 min sur les 2-3 finalistes)

Pour chaque finaliste :
- **Qui le vend déjà, et où ?** Lister les marchés couverts (FR, IT, ES, DE…).
- **Reste-t-il un marché non exploité ?** C'est souvent là qu'est l'opportunité réelle, plutôt que dans une bagarre frontale.
- **Des boutiques récentes arrivent-elles à se placer ?** Si oui, le marché absorbe encore. Si les nouveaux entrants échouent malgré une forte demande, étudier ceux qui ont réussi (angle, timing, offre) plutôt que de répliquer ce qui ne marche plus.
- **Où le concurrent déçoit-il ?** Lire ses avis clients : les plaintes récurrentes sont l'endroit exact où se construit un angle différenciant (procédure complète : `Knowledge/Customer_Research_SOP.md`).

## Étape 4 — Décision et calcul avant test

Sur le gagnant, **avant** de dépenser un euro :
1. Demander un devis à un agent sur les 3 formats de bundle (1x, 2x, 3x)
2. Calculer le **COGS moyen pondéré** et le **prix moyen pondéré** (méthode : `Knowledge/Ecom_Meta_Ads_Playbook.md` §3)
3. En déduire **ROAS BE** et **ROAS Target**
4. Vérifier que le budget disponible permet d'aller au bout d'un cycle de test complet. **Si non, on ne lance pas** — un test sous-financé ne dit pas que le produit est mauvais, il ne dit rien du tout. C'est la seule dépense qui n'achète aucune information.

## Répartition BOS / toi

| Étape | Qui |
|---|---|
| 1 — Sourcing dans l'Ad Library | **Toi** (accès depuis ton navigateur), ~60 min. Tu me colles les liens et les captures |
| 2 — Scoring des 10 candidats | **BOS** — je remplis la grille et je justifie chaque note |
| 3 — Vérification concurrentielle et lecture des avis | **BOS** — analyse des marchés couverts, des plaintes clients, des angles disponibles |
| 4 — Calculs COGS/ROAS et go/no-go | **BOS** calcule, **tu** décides |
| Après : angles, scripts de créas, structure de boutique, copy, flows email | **BOS** |

**Ce que je ne peux pas faire à ta place :** accéder aux données de dépense en temps réel (l'Ad Library et les outils de veille demandent ta session navigateur). Le sourcing brut est la seule partie qui exige tes mains — une heure, une fois. Tout ce qui vient après est de l'analyse, et c'est mon travail.

## Le premier cycle, concrètement

- **Jour 1** — 60 min d'Ad Library, tu me ramènes 10 candidats
- **Jour 1 (soir)** — je te rends le scoring complet et les 2-3 finalistes argumentés
- **Jour 2** — je livre la vérification concurrentielle et les angles disponibles
- **Jour 3** — devis agent, calculs, décision go/no-go

**Trois jours pour transformer « je bloque sur la recherche produit » en un produit choisi et chiffré.** Le blocage n'est pas la difficulté de la tâche — c'est l'absence de bornes.
