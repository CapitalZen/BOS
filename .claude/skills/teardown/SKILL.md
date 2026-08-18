# Skill: Teardown

Décortiquer une marque qui gagne, couche par couche, et en extraire des leviers **exécutables** classés par **rendement net**. Déclenché quand il faut construire une boutique, une offre, un funnel ou une créative et qu'on veut s'appuyer sur ce qui marche déjà plutôt que sur une intuition — ou quand l'entrepreneur veut monter son niveau d'analyse.

## Objectif

Fin de session : un fichier `Output/Teardown_[Marque]_[date].md` contenant les 7 couches décortiquées, chaque observation traduite en **effet net estimé sur le P&L**, filtrée par ce que l'entrepreneur peut réellement exécuter, et **au moins un levier appliqué dans la session** — pas la semaine prochaine.

**Critères de succès :** la marque analysée est prouvée rentable *avant* décortiquage ; chaque levier retenu est rattaché à une métrique de P&L nommée (CVR, AOV, CAC, réachat, taux de retour, marge) ; chaque levier écarté l'est pour un motif écrit ; au moins une chose est shippée ; les prédictions sont enregistrées pour vérification ultérieure.

## Croyances

- **On ne décortique jamais une marque avant d'avoir prouvé qu'elle gagne.** L'erreur la plus coûteuse du teardown est de copier un cadavre. Une boutique peut être belle, bien copywritée, bien structurée — et mourir. Cas documenté : Leishape, décortiqué le 04/08/2026, 2,5/5 sur Trustpilot et −80 % de trafic. Utile comme **contre-exemple**, désastreux comme modèle. La preuve de rentabilité précède l'analyse, toujours.
- **Une observation sans mécanisme de P&L est une anecdote.** « Ils ont un badge d'urgence », « leur hero a de la preuve sociale » ne valent rien tant qu'on n'a pas dit *quelle* métrique ça bouge et *de combien*. Le livrable n'est pas une liste de ce qu'ils font, c'est une liste de ce qui leur rapporte.
- **Rendement net, pas rendement brut.** Un levier qui monte le panier moyen de 15 % mais fait +8 points de retours est négatif. Un upsell qui convertit à 20 % mais casse la marge sur le produit d'appel est négatif. **Toujours soustraire : coûts de mise en œuvre, retours, SAV, complexité opérationnelle ajoutée.** Le simple scale, le complexe casse.
- **Ce qui est visible n'est pas ce qui produit le résultat.** On voit les tactiques du gagnant, jamais les vingt marques qui ont utilisé les mêmes et ont échoué. Le biais du survivant est la maladie native du teardown. Un levier n'est crédible que s'il est **répété chez plusieurs gagnants** ou qu'on peut expliquer *pourquoi* il marche.
- **Un levier non transférable est un levier inutile.** Copier une revendication de fabrication européenne quand on source en Chine, c'est mentir — et c'est ce qui tue les marques. Chaque levier passe par quatre portes : trésorerie, production/sourcing, compétence, véracité. Une porte fermée = levier écarté, pas « levier à retenir pour plus tard ».
- **Un marché n'a pas un seul stade de sophistication, il est stratifié par gamme de prix.** Décortiquer une marque premium et appliquer ses codes à une offre accessible produit un message hors sol. Toujours situer la marque analysée dans **sa strate**, et n'importer que ce qui traverse les strates (`Knowledge/Schwartz_Breakthrough_Advertising.md` §3).
- **Le teardown vaut au moment où on a quelque chose à construire.** Décortiquer une boutique six mois avant d'en ouvrir une, c'est de la consommation de méthode. Le teardown se déclenche *contre une décision en cours*, jamais dans le vide.
- **Trois marques battent une.** Un levier vu chez un seul acteur est une hypothèse. Vu chez trois, c'est un standard de catégorie. La comparaison croisée est ce qui sépare le teardown de la copie.
- **Le teardown se termine par un test, pas par un document.** Un enseignement non appliqué a un rendement net de zéro, quel que soit son intérêt intellectuel.

## Références

- `Knowledge/Schwartz_Breakthrough_Advertising.md` §3 — stades de sophistication, filtre des pubs qui tournent depuis 3+ mois, erreurs symétriques de sur/sous-sophistication, arbitrage géographique.
- `Knowledge/Ecom_Funnel_Architecture.md` — grille de lecture des couches 2 à 5 : hooks, structure de créative, landing, advertorial, les 7 mécaniques d'offre et les 3 niveaux.
- `Knowledge/Ecom_Meta_Ads_Playbook.md` — lecture des patterns concurrents, ROAS BE/Target, CRO et AOV, ce qui compte réellement dans la rentabilité.
- `Knowledge/Customer_Research_SOP.md` — message mining, à appliquer aux avis de la marque décortiquée (couche 7).
- `Knowledge/AI_Ecom_Ops_Stack.md` — cartographie des angles, à alimenter avec les sorties de la couche 2.

## Sources réellement accessibles

À vérifier avant de promettre quoi que ce soit — la disponibilité change selon l'environnement.

| Source | Ce qu'elle donne | Accès |
|---|---|---|
| Boutique de la marque | Structure, offre, CRO, panier, upsells | **BOS** (WebFetch) |
| Trustpilot / avis Google | Satisfaction réelle, défauts récurrents | **BOS** |
| Presse, levées, interviews | CA, financement, ancienneté | **BOS** (WebSearch) |
| Wayback Machine | Évolution du positionnement et des prix dans le temps | **BOS** |
| Séquence email | Relances, offres, cadence, réachat | **Entrepreneur** (inscription, 2 min) puis BOS analyse |
| Facebook Ad Library | Créatives actives, ancienneté des pubs | **Entrepreneur** (connexion requise) — BOS ne peut pas y accéder |
| TrendTrack / ad spy payants | Trafic, volume, spend | Payant (~30-90 €/mois) — **optionnel**, le socle gratuit couvre l'essentiel |

**Ne jamais prétendre avoir consulté l'Ad Library.** Si la couche 1-2 en dépend, demander une capture ou la liste des pubs actives — une demande précise, pas un devoir.

## Process

### Phase 0 — Cadrer la décision

Pas de teardown sans décision à éclairer. Ouvrir par : *« On décortique pour décider quoi exactement ? »*

Cibles valides : structurer une boutique, construire une offre, écrire des créatives, fixer un prix, monter une séquence email. Cible invalide : « pour apprendre ». Si la réponse est « pour apprendre », le teardown est prématuré → proposer de le déclencher au moment de la construction, et revenir à l'action en cours.

**Sortie :** une phrase — « on décortique X pour décider Y ».

### Phase 1 — Sélection et filtre de viabilité

Identifier 3 marques de la catégorie, puis **prouver qu'elles gagnent avant de les décortiquer**.

| Signal | Seuil de validation |
|---|---|
| Ancienneté | > 18 mois d'activité continue |
| Satisfaction | ≥ 4/5 sur un volume d'avis significatif (> 100) |
| Trajectoire de trafic | Stable ou croissante, pas en chute |
| Persistance publicitaire | Des créatives qui tournent depuis > 3 mois |
| Profondeur de gamme | Signe de réachat et de marge, pas de produit unique opportuniste |

**Deux échecs sur cinq → écarter comme modèle.** La marque peut rester au dossier comme **contre-exemple** : ce qui l'a fait échouer est souvent plus exploitable qu'une réussite, parce que le trou qu'elle laisse est une place libre. C'est exactement ce qui a produit l'angle de Velune.

**Sortie :** 3 marques validées + le motif de chaque écartée.

### Phase 2 — Décortiquage en 7 couches

Pour chaque marque, remplir les 7 couches. Ne pas se contenter de décrire : noter **pourquoi** ça marche.

1. **Trafic** — canaux, part organique/payant, ancienneté des pubs, formats dominants.
2. **Créative et hook** — les 3 premières secondes, mécanisme du hook, structure narrative, stade de conscience visé (`Ecom_Funnel_Architecture.md`).
3. **Funnel** — congruence pub → page, présence d'un advertorial, above the fold, réassurance.
4. **Offre** — structure, mécaniques employées parmi les 7, niveau d'offre (1/2/3), garantie, packaging.
5. **CRO et panier** — upsells, bundles, seuil de livraison gratuite, ancrage de prix, friction au checkout.
6. **Rétention** — séquence email, abonnement, cadeaux à paliers, programme de fidélité.
7. **Produit et opérations** — délais annoncés, politique de retour, promesses de qualité, ce que les avis négatifs révèlent des failles (message mining).

**Sortie :** tableau 7 couches × 3 marques. Les cases vides sont un signal, pas un oubli — une couche que personne ne travaille est soit inutile dans cette catégorie, soit une opportunité.

### Phase 3 — Traduire en rendement net

**C'est la phase qui distingue ce skill d'une liste d'observations.** Chaque élément relevé passe dans cette grille :

| Champ | Contenu |
|---|---|
| Levier | Ce qu'ils font, en une phrase |
| Métrique touchée | CVR, AOV, CAC, taux de réachat, taux de retour, ou marge unitaire — **une seule** |
| Effet brut estimé | Ordre de grandeur, assumé comme estimation |
| Coûts à soustraire | Mise en œuvre, retours induits, SAV, complexité opérationnelle |
| **Rendement net** | Effet brut − coûts |
| Confiance | Vu chez 1 marque (hypothèse) / 2 (probable) / 3 (standard de catégorie) |
| Coût de mise en œuvre | En euros **et** en heures |

**Règles de calcul :**
- Un levier qui monte l'AOV mais augmente les retours se calcule **net de retours**, jamais brut.
- Un levier qui ajoute une opération récurrente (packaging manuel, SAV supplémentaire) porte ce coût **à chaque commande** — il se déduit de la marge unitaire, pas une seule fois.
- Un levier gratuit à effet modeste bat souvent un levier coûteux à fort effet quand la trésorerie est contrainte. **Classer par rendement net rapporté au capital engagé**, pas par effet absolu.

**Sortie :** leviers triés par rendement net décroissant.

### Phase 4 — Filtre de transférabilité

Chaque levier passe quatre portes. Une seule fermée = écarté, avec le motif écrit.

1. **Trésorerie** — finançable avec l'argent réellement disponible aujourd'hui ?
2. **Production / sourcing** — le modèle de production le permet-il ? (Une revendication de fabrication locale est infaisable en sourcing lointain.)
3. **Compétence** — exécutable par l'entrepreneur, ou par BOS à sa place ? Si ni l'un ni l'autre, écarté.
4. **Véracité** — la revendication est-elle **vraie** pour ce produit ? Une promesse invérifiable est un risque juridique et le premier facteur de retours et d'avis négatifs.

**Sortie :** leviers retenus / leviers écartés avec motif. La liste des écartés a de la valeur — elle évite de reposer la question dans trois mois.

### Phase 5 — Mise en pratique dans la session

Un teardown qui finit en document a un rendement net de zéro.

- Prendre le levier n°1 de la liste retenue et **l'appliquer maintenant**. BOS produit : le copy, la structure de page, la séquence email, la mécanique d'offre.
- Si le levier n°1 dépend d'un prérequis bloqué (boutique inexistante, trésorerie), prendre le premier levier applicable **aujourd'hui** et le dire explicitement.
- Répartition BOS / entrepreneur affichée, comme pour tout plan.

**Sortie :** un livrable concret produit dans la session.

### Phase 6 — Enregistrer les prédictions et vérifier

Ce qui fait qu'un teardown compose au lieu de se répéter.

Pour chaque levier appliqué, écrire **avant** de le déployer : métrique visée, valeur actuelle, effet attendu, échéance de vérification. Puis revenir vérifier à l'échéance.

| Levier appliqué | Métrique | Avant | Attendu | Réel | Verdict |
|---|---|---|---|---|---|

Sans cette table, on ne saura jamais quel levier a réellement produit du rendement — et le teardown suivant repartira des mêmes suppositions. **La table se met à jour à chaque session où une donnée arrive.**

## Pièges

| Piège | Ce qu'il produit | Antidote |
|---|---|---|
| Décortiquer une marque en déclin | On copie ce qui l'a tuée | Phase 1 avant tout |
| Confondre visible et causal | On copie des tactiques cosmétiques | Exiger 2-3 marques par levier |
| Copier hors de sa strate de prix | Message hors sol, promesse intenable | Phase 4, porte 2 et 4 |
| Rendement brut au lieu de net | On dégrade la marge en croyant l'améliorer | Phase 3, soustraire systématiquement |
| Teardown sans décision à éclairer | Consommation de méthode déguisée en travail | Phase 0 |
| Finir sur le document | Rendement net zéro | Phase 5 obligatoire |
| Ne jamais vérifier après | Aucun apprentissage cumulé | Phase 6 |

## Mise à jour des fichiers

- `Output/Teardown_[Marque]_[date].md` — les 7 couches, la grille de rendement, les leviers retenus et écartés.
- `Core/Business.md` — la cartographie concurrentielle par strate, si elle bouge.
- `Core/Actions.md` — les leviers retenus deviennent des actions classées.
- `Core/Journal.md` — ce qui a été décortiqué, la décision éclairée, le levier appliqué.

---

**Dernière revue :** 2026-08-17
