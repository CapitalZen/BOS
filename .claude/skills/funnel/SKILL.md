# Skill: Funnel

Optimiser le tunnel de conversion quand le trafic et l'offre sont déjà des hypothèses validées. Déclenché quand `diagnosis` identifie un problème de conversion en phase PMF — en 3e position (après trafic et offre) car c'est le cas le plus rare : assez de volume qualifié, offre structurée, mais la conversion casse.

Beaucoup d'entrepreneurs « optimisent le funnel » alors que le vrai problème est le volume ou l'offre. Ce skill **assume** : trafic suffisant pour apprendre, offre crédible — sinon **renvoyer** vers `traffic` ou `offer`. Ici : données d'abord, un levier à la fois, IA pour ~80% du travail (copy, structure, propositions de test).

## Objectif

À la fin de la session : carte du tunnel **complète**, métriques par étape, **comparaison aux benchmarks**, **plus gros drop-off identifié**, **recommandations priorisées** (levier #1), et **au moins une variante concrète** (copy réécrite, restructure page, plan de test) produite par BOS. Fichiers Core et Output à jour.

**Critères de succès :** décisions **chiffrées** ; une hypothèse de correction **à la fois** ; pas d'optimisation « au feeling ».

## Croyances

- **Le funnel est la dernière hypothèse.** Si trafic insuffisant ou offre non validée, le problème **n'est pas** le funnel — diagnostiquer autrement.
- **Data-driven, pas opinion-driven.** Chaque décision doit s'appuyer sur des chiffres (ou sur un plan explicite pour les obtenir).
- **Plus gros drop-off d'abord.** On perd le plus de monde à un endroit précis — c'est là le levier #1.
- **Un seul changement à la fois.** Sinon on ne sait pas ce qui a marché.
- **Des benchmarks standards existent.** Comparer **avant** de crier au désastre ou de se féliciter.
- **L'IA peut faire ~80% de l'optimisation** — réécriture, structure, suggestions A/B ; l'humain valide, publie, et respecte la discipline de mesure.

## Process

### Phase 1 — Mapper le tunnel complet

Pour **chaque étape**, nommer la source et la sortie :

**Source trafic** → **Landing / site** → **Intérêt** (scroll, clic, temps) → **Considération** (lead, panier, booking) → **Achat** → **Post-achat** (onboarding, usage, réachat, referral).

Adapter les libellés au modèle (SaaS, e-com, services, appels). Inclure **toutes** les branches (ex. email nurture, relances panier).

### Phase 2 — Collecter les données à chaque étape

Exemples de métriques (choisir ce qui colle au business) :

- Visiteurs uniques, sessions
- Clics CTA, taux de clic
- Leads / inscriptions / add-to-cart
- Checkout initié vs complété
- Achats, panier moyen
- Emails : envoi, ouverture, clic
- Appels : bookés, show rate, close rate

Si données manquantes → **première action** = instrumentation minimale (analytics, tableaux, exports) — pas « optimiser à l'aveugle ».

### Phase 3 — Comparer aux benchmarks standard

Utiliser des ordres de grandeur **indicatifs** (ajuster selon industrie et source) :

| Étape (indicatif) | Ordre de grandeur souvent cité |
|-------------------|--------------------------------|
| Landing → lead (B2B lead gen) | Variable ; viser amélioration vs baseline propre |
| Page produit → add to cart | ~2-5% visiteurs (e-com — très variable) |
| Checkout completion | Souvent 40-70% du checkout initié (à calibrer) |
| Email open (campagnes) | Souvent ~20-30% si liste engagée (très variable) |
| Email click | Souvent ~2-5% du send (variable) |

**Règle :** la valeur absolue compte moins que **ton** historique ; les benchmarks servent à contextualiser (« on est sous le plausible » vs « le problème est en amont »).

### Phase 3 bis — Élargir au parcours complet (Customer Journey Map)

Le tunnel de conversion s'arrête à l'achat. **Le parcours client, non** — et une partie des pertes se situe hors du tunnel, là où personne ne regarde.

Cartographier les cinq étapes, en notant à chacune **ce que la personne ressent** et **ce qui peut la faire décrocher** :

| Étape | Questions | Point de perte typique |
|---|---|---|
| **1. Découverte** | Où me voit-elle pour la première fois ? Que comprend-elle en 2 secondes ? | Message qui ne sélectionne personne |
| **2. Considération** | Que fait-elle entre la découverte et la visite ? Compare-t-elle ? | Absence de preuve, doute sur le sérieux |
| **3. Achat** | Le tunnel proprement dit | Friction, information manquante, prix mal justifié |
| **4. Attente et réception** | Que se passe-t-il entre le paiement et le colis ? Est-elle rassurée ? | **Silence après l'achat** — le point le plus négligé, et la première cause de litiges |
| **5. Usage et suite** | Obtient-elle le résultat promis ? Le dit-elle ? Rachète-t-elle ? | Aucune sollicitation d'avis, aucun flux de réachat |

**Ce que la carte révèle et que le tunnel cache :** les étapes 4 et 5 ne coûtent presque rien à améliorer et pèsent directement sur la marge — moins de litiges, plus d'avis, plus de réachats, du bouche-à-oreille. Un entrepreneur qui n'optimise que les étapes 1 à 3 travaille sur la moitié la plus chère de son parcours.

**Règle d'usage :** faire la carte **avant** de choisir quoi optimiser. Le plus gros gain n'est pas toujours dans le tunnel.

### Phase 4 — Identifier le plus gros drop-off

Calculer les **pertes relatives** entre étapes : où perd-on le plus de gens en proportion ou en volume absolu qualifié ?

Prioriser **une** étape pour la suite (levier #1). Documenter l'hypothèse (« friction checkout », « promesse landing ≠ offre », etc.) liée au chiffre.

### Phase 5 — Proposer des améliorations (levier #1 d'abord)

Pour l'étape retenue :

- **Copy** — titres, bullets, garanties, objections.
- **Structure** — hiérarchie page, ordre des sections, nombre de champs formulaire.
- **Design / UX** — lisibilité mobile, CTA visibles, charge cognitive.
- **Confiance** — preuve, risque inversé, clarté du next step.

BOS rédige **2-3 variantes** testables pour **un** changement principal (ex. headline seulement).

**Si e-commerce** — leviers spécifiques et détails dans `Knowledge/Ecom_Meta_Ads_Playbook.md` §6 :

- **L'AOV avant le taux de conversion.** Faire passer un panier de 30 à 60 € double la marge au même coût d'acquisition. Bundles en volume (1+1, 2+1 offert — « offert » déclenche un sentiment de gain plus fort qu'un pourcentage équivalent), cadeau physique ou e-book, seuils de livraison gratuite.
- **Le panier** : barre de progression vers un avantage, bumps avant paiement, badges de réassurance en haut et sous le bouton. Urgence uniquement si elle est réelle — une fausse rareté est une pratique trompeuse et le premier motif de litiges.
- **Les upsells post-achat** : même produit à prix réduit (consommables) ou complémentaire évident. Source d'idées gratuite : la section « fréquemment achetés ensemble » d'Amazon sur le produit.
- **Cartographier avant d'optimiser** : un outil de heatmap/session replay (Microsoft Clarity, gratuit) montre où les visiteurs décrochent. Le drop-off réel dicte quoi tester — pas l'intuition.

### Phase 6 — Implémenter avec l'IA (BOS)

- Réécriture des blocs prioritaires.
- Proposition de structure alternative (wireframe textuel).
- Si pertinent : plan de test A/B sur une variable — hypothèse, variante A/B, métrique de succès, durée minimale.

**Rigueur d'un A/B test :** deux versions affichées **simultanément** au même trafic (jamais « avant/après » sur deux semaines — CPM, saisonnalité et jours fériés faussent tout). Volume minimum réel avant conclusion (~500 conversions par variante en e-commerce) ; significativité à partir d'un score Z de 1,96 (95 %). En dessous du volume, ne pas tester : optimiser sur la base des drop-offs observés.

**La métrique de décision, c'est la marge nette par visiteur** — pas le taux de conversion, pas le CA par visiteur. Une variante qui convertit moins mais vend des paniers plus rentables gagne. Toujours recalculer le COGS moyen pondéré par la répartition réelle des offres avant de trancher.

### Phase 7 — Mesurer et itérer

- **1 changement** (ou une famille cohérente : ex. uniquement la page panier).
- **Mesurer** sur une fenêtre définie (souvent ~1 semaine minimum si volume suffisant — sinon plus long ou abandon du test statistique au profit de volumes plus hauts).
- Réévaluer : garder, itérer, ou passer au 2e drop-off.

## Output

| Fichier | Contenu |
|--------|---------|
| `Output/Funnel_Audit_[date].md` | Carte tunnel + données + benchmarks + drop-offs + reco + plan de test |
| `Core/Actions.md` | Actions prioritaires (mesure, implémentation, suivi) |
| `Core/Business.md` | Section conversion / funnel si utile (état, KPIs, expériences en cours) |

## Garde-fous

- **Ne JAMAIS optimiser le funnel si le trafic est insuffisant pour conclure** — d'abord le volume (`traffic`).
- **Ne JAMAIS changer plusieurs choses à la fois** — un changement, une mesure.
- **Ne JAMAIS optimiser sans données** — « je pense que c'est X » sans chiffres = interdit ; obtenir le minimum de métriques ou le dire explicitement.
- **Ne JAMAIS ignorer le contexte** — ~10 visiteurs/semaine : pas besoin d'A/B test statistique ; besoin de trafic ou de tests qualitatifs.
- **Ne JAMAIS traiter le funnel en premier si l'offre ou le volume n'est pas validé** — ordre PMF : offre / trafic avant conversion fine.
