# Programme e-commerce — de zéro à la bascule payante

**Créé le :** 04/08/2026 · **Document vivant** — voir « Comment l'utiliser » ci-dessous.

Ce document est la carte complète du projet, construite à partir de tout ce qui est déjà intégré dans `Knowledge/`. Il ne remplace pas `Core/Actions.md` (le quoi-faire-cette-semaine) ni `Core/Diagnosis.md` (le bottleneck du moment) — il donne la vue d'ensemble dans laquelle ces deux fichiers s'inscrivent, pour ne jamais perdre le fil entre deux sessions.

---

## Comment l'utiliser

- **Les sections de phase ci-dessous sont figées** — elles ne se réécrivent pas à chaque session, elles décrivent la méthode.
- **Le Journal du programme, en bas de document, est la seule partie qui s'enrichit.** Après chaque jalon réel (produit tranché, première vente, palier de dépense atteint, échec instructif), une entrée s'ajoute — jamais une réécriture des sections figées.
- **Une phase ne se saute pas et ne s'anticipe pas.** Le déclencheur de passage à la phase suivante est écrit à chaque fois — s'il n'est pas atteint, on reste dans la phase actuelle même si l'envie de scaler est là.

---

## Où on en est (au 04/08/2026)

**Phase 0 — Fondations**, en cours. Territoire tranché (mode & accessoires féminins à utilité). Produit : 4 archétypes scorés, vérification concurrence Ad Library en cours sur les 4. Boutique : pas encore montée. Contenu : pas encore publié. Budget : nul jusqu'à l'entrée en poste (date inconnue à ce jour — voir `Core/Diagnosis.md` #5).

---

## Phase 0 — Fondations

**Objectif :** sortir avec un produit tranché et une boutique prête à recevoir du trafic.

**Stratégies de référence :**
- Choix du produit et lecture des patterns concurrents — `Ecom_Meta_Ads_Playbook.md` §2
- Structure de boutique de niche brandée — `Ecom_Meta_Ads_Playbook.md` §1 (« La stratégie : boutique de niche brandée »)

**Déclencheur de sortie de phase :** produit tranché (par score + vérification concurrence) **et** boutique Shopify montée (thème, pages légales, pixel, capture email).

---

## Phase 1 — Lancement organique sans budget

**Contrainte du moment :** budget zéro jusqu'à l'entrée en poste. Cette phase ne dépend d'aucun euro.

**Objectif :** construire une audience, trouver le format de contenu qui répond sur ce territoire, et faire tourner le pixel + la capture email en continu — pas vendre.

**Stratégies de référence :**
- Cadence, formats, capture de données sans budget pub — `Ecom_Organic_Launch_Playbook.md`
- Immersion dans le vocabulaire et les frustrations réelles de l'audience, avant d'écrire le moindre angle — `Customer_Research_SOP.md` Étape 1 bis (BOS peut faire cette descente à la place de l'entrepreneur)
- Grille de formats, 20 hooks, calendrier semaine 1 déjà livrés — `Output/Territoire_Mode_Feminine_Utilite_2026-07-29.md`

**Déclencheur de sortie de phase :** cadence de publication tenue sur plusieurs semaines **et** un format identifié qui surperforme nettement les autres (vues, commentaires, ajouts au panier si la boutique est déjà en ligne).

---

## Phase 2 — Premières ventes et entrée en poste

**Ce qui change ici :** l'entrée en poste (conducteur) ouvre les premiers revenus, donc les premiers euros disponibles pour le projet.

**Objectif :** premières commandes réelles, en fulfillment sans stock ; échantillon produit acheté dès les premiers revenus de l'emploi ; réserve de trésorerie qui démarre.

**Stratégies de référence :**
- Le minimum réel pour démarrer (30-50 € le premier mois) — `Core/Business.md`
- CRO de base (landing page, panier, upsells) — `Ecom_Meta_Ads_Playbook.md` §6
- Séquence de financement (contenu → audience → premières ventes → réserve → bascule payante) — `Core/Business.md`

**Déclencheur de sortie de phase :** trésorerie ≥ ~3 000 € **et** au moins un format organique validé sur la durée (pas un coup de chance isolé).

---

## Phase 3 — Bascule payante prudente

**Objectif :** valider un ROAS BE tenable sur Meta Ads, avec un budget de test restreint (100-1500 €), avant d'engager plus.

**Stratégies de référence :**
- Configuration Meta Ads complète (profil, Business Manager, compte pub, page) — `Ecom_Meta_Ads_Playbook.md` §3 « Configuration »
- ROAS Break-Even et ROAS Target, calcul pondéré par bundle — `Ecom_Meta_Ads_Playbook.md` §3
- Testing CBO, paliers de scaling 100 → 1 500 € — `Ecom_Meta_Ads_Playbook.md` §3 « Le testing »
- Créatives : funnel TOFU/MOFU/BOFU, statics/vidéos/natives, itération vs déclinaison — `Ecom_Meta_Ads_Playbook.md` §4, `Ecom_Funnel_Architecture.md`

**Déclencheur de sortie de phase :** ROAS Target tenu sur plusieurs jours consécutifs, budget augmenté sans dégradation.

---

## Phase 4 — Scaling structuré

**Objectif :** passer d'une trouvaille à un système qui tient à des paliers de dépense croissants, sans casser la rentabilité.

**Stratégies de référence :**
- Pilotage du budget de 0 à 5 k/jour, puis de 5 k à 100 k/jour — `Ecom_Meta_Ads_Playbook.md` §3
- La checklist de marge — croissance d'abord jusqu'à ~10 k€/jour stable, marge ensuite (15-17 % net), scaling après — `Ecom_Meta_Ads_Playbook.md` §4
- Transition boutique de test → semi-marque, déclenchée à 50-100 ventes — `Ecom_Meta_Ads_Playbook.md` §6 bis
- Marché européen, TVA, ROAS BE complet tous coûts inclus — `Ecom_Meta_Ads_Playbook.md` §11

**Déclencheur de sortie de phase :** volume quotidien stable, effectif qui grandit au-delà de ce qu'une seule personne peut piloter.

---

## Phase 5 — Systèmes et équipe

**Objectif :** déléguer dans l'ordre qui protège la rentabilité plutôt que de recruter au feeling.

**Stratégies de référence :**
- Roadmap de délégation en 10 étapes (SAV en premier, COO en dernier) — `Recruiting_Playbook.md` §3 ter
- Recrutement de VA à l'étranger (nationalité, plateformes, salaires) — `Recruiting_Playbook.md` §3 bis
- Répartition BOS/entrepreneur sur les 9 compétences du métier — `Ecom_Meta_Ads_Playbook.md` §10

**Déclencheur de sortie de phase :** il n'y en a pas — cette phase est permanente, elle s'affine en continu.

---

## Stratégies transverses — à tout moment, quelle que soit la phase

| Sujet | Référence | Quand s'en servir |
|---|---|---|
| Recherche client (message mining, immersion) | `Customer_Research_SOP.md` | Avant tout copy, à chaque nouveau produit ou angle |
| Niveaux de conscience et de sophistication | `Schwartz_Breakthrough_Advertising.md` | Pour caler le ton d'une créative ou d'une page à l'audience visée |
| Offre et pricing | `PMF_Offer_Playbook.md` | Dès que les ventes stagnent malgré du trafic |
| Énergie, focus, discipline | `Entrepreneur_Success_Factors.md` | En cas de rythme qui décroche ou de doute — protocole énergie, formule Énergie × Focus × Input × Temps |
| IA comme levier | `AI_Leverage_Method.md`, `AI_Ecom_Ops_Stack.md` | Pour cadrer BOS ou tout autre usage IA du business |

---

## Résumé des déclencheurs de phase

| Phase | Déclencheur d'entrée | Déclencheur de sortie |
|---|---|---|
| 0 — Fondations | Départ du projet | Produit tranché + boutique montée |
| 1 — Organique sans budget | Boutique prête | Cadence tenue + format gagnant identifié |
| 2 — Premières ventes | Entrée en poste + revenus | Trésorerie ≥ ~3 000 € + format validé dans la durée |
| 3 — Bascule payante | Trésorerie suffisante | ROAS Target tenu plusieurs jours |
| 4 — Scaling structuré | ROAS Target stable | Volume qui dépasse la capacité solo |
| 5 — Systèmes et équipe | Volume qui dépasse la capacité solo | Permanent |

---

## Journal du programme

*Une entrée par jalon réel. Format : Date · Phase · Ce qui s'est passé · Décision.*

**04/08/2026 · Phase 0** — Programme créé. Vérification concurrence relancée sur les 4 archétypes du shortlist (accessoire coiffure 16/18, sous-vêtement sans armature 15/18, confort du pied 15/18, collant/bas renforcé 15/18) — en cours, résultats attendus. Aucun produit tranché à ce jour, aucune boutique montée, aucune vidéo publiée.
