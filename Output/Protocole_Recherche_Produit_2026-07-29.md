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

### Le filtre qui change tout : ne regarder que ceux qui ont tes armes

Quand tu es dans l'Ad Library, tu vas croiser deux types de boutiques :
- **Des marques installées** avec du budget, de l'antériorité, une équipe. Leurs résultats ne sont pas reproductibles avec ta trésorerie — les regarder t'induit en erreur.
- **Des boutiques e-commerce indépendantes** qui jouent avec les mêmes armes que toi.

**Comment les distinguer en 10 secondes :** ouvre le site de la boutique et repère les mécaniques typiques du e-commerce indépendant — sélecteur de bundle (« achetez-en 2, économisez X »), widget d'avis clients, guide des tailles, pop-up d'inscription email/SMS, barre de progression vers la livraison gratuite. Si tu vois cette signature, tu es sur une boutique comparable à la tienne. **C'est celle-là qu'il faut étudier.**

### L'analyse rétro saisonnière (l'étape que presque personne ne fait)

Les produits, même evergreen, ont des cycles. Un produit qui a explosé en septembre l'an dernier a de bonnes chances de recommencer.

**Version gratuite, faisable maintenant :** TikTok Creative Center donne les top ads par pays, par secteur et par période — remonte sur les mêmes mois des années précédentes. Google Trends confirme la saisonnalité d'une catégorie sur 5 ans, gratuitement.

**Version payante (~50-100 €/mois : AdSpy, TrendTrack, Kalodata, Pipiads) :** filtrer sur le même mois de l'année précédente + les 2 mois suivants, avec un seuil d'engagement, puis remonter sur 5 ans, marché par marché. On cherche des **patterns récurrents**, pas un produit à copier.

**Ma recommandation vu ta trésorerie :** commence gratuit. Un abonnement de veille est un bon investissement — mais il entre en concurrence directe avec ton budget publicitaire, et c'est le budget publicitaire qui produit les données. Un mois d'outil se prend **au moment où tu es prêt à lancer**, pas trois mois avant.

## Étape 2 — Scoring (15 min pour les 10)

Note chaque candidat sur les 4 critères. **Un critère à 0 est éliminatoire, quel que soit le total.**

| Critère | 0 | 1 | 2 |
|---|---|---|---|
| **Marge** (prix de vente constaté ÷ coût estimé produit+livraison) | < x3 | x3 à x4,5 | > x4,5 |
| **Demande croissante** | Annonces stables ou en baisse | Croissance visible depuis < 2 mois | Croissance forte et continue depuis 2-3 mois |
| **Time-to-market** | Produit installé depuis > 1 an, courbe plate | Produit récent mais signal faible | Explosion < 3 mois, ou saisonnalité qui se répète |
| **Contenu disponible** | Rien n'existe, tout à produire | Quelques vidéos exploitables comme référence | Beaucoup de contenu organique sur le produit |

**Critères de viabilité — vérifiés sur les finalistes uniquement, mais éliminatoires :**

| Critère | Seuil |
|---|---|
| **AOV atteignable** | ≥ 35 € par commande (bundle compris) |
| **ROAS BE visé** | < 1,5 |
| **Evergreen** | Demande toute l'année, pas un pic unique |
| **Produit léger** | Recommandé — le poids pèse sur le coût logistique et les délais |
| **TAM large** | Assez de monde pour absorber le scaling |
| **Récurrence / consommable** | Bonus fort, pas obligatoire |

**Bonus — les 5 raisons d'achat.** Compter combien le produit en coche : résout un problème · facilite la vie · fait gagner de l'argent · élève le statut · réunit une communauté.
**0 raison cochée = élimination immédiate**, quel que soit le score. Chaque raison cochée est un angle de test différent, donc un actif.

**Seuil de passage : 6/8 minimum, aucun 0, au moins 2 raisons d'achat.**

## Étape 3 — Vérification concurrentielle (20 min sur les 2-3 finalistes)

Pour chaque finaliste :
- **Qui le vend déjà, et où ?** Lister les marchés couverts (FR, IT, ES, DE…).
- **Reste-t-il un marché non exploité ?** C'est souvent là qu'est l'opportunité réelle, plutôt que dans une bagarre frontale.
- **Des boutiques récentes arrivent-elles à se placer ?** Si oui, le marché absorbe encore. Si les nouveaux entrants échouent malgré une forte demande, étudier ceux qui ont réussi (angle, timing, offre) plutôt que de répliquer ce qui ne marche plus.
- **Où le concurrent déçoit-il ?** Lire ses avis clients : les plaintes récurrentes sont l'endroit exact où se construit un angle différenciant (procédure complète : `Knowledge/Customer_Research_SOP.md`).

## Étape 3 bis — Le check conformité (5 min, et il est éliminatoire)

À faire **au moment du choix du produit**, jamais plus tard. C'est le seul risque de toute la chaîne qui soit **irréversible** : un SAV débordé se rattrape, un stock se recommande — des colis déjà expédiés non conformes, non. Une marque peut mourir de ça avec un ROAS à 4.

Pour chaque finaliste :
- **La catégorie est-elle réglementée ?** Les plus sensibles : cosmétique, alimentaire et compléments, électrique et électronique, jouet et puériculture, tout ce qui touche à la santé.
- **Quelles mentions sont obligatoires** sur le produit et l'emballage dans les pays visés (composition, avertissements, marquage de conformité, coordonnées du responsable de la mise sur le marché) ?
- **Dans quelle langue** l'étiquetage doit-il être fourni ?

Si un finaliste tombe dans une catégorie lourdement réglementée et que la réponse n'est pas claire → **il sort de la shortlist pour un premier lancement.** Ce n'est pas de la prudence excessive : c'est le seul poste où l'erreur ne se corrige pas.

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
