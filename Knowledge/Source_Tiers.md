# Hiérarchie des sources — ce qui a valeur de preuve, et ce qui n'en a pas

*Créé le 17/08/2026, après une erreur réelle. Inspiré du `source-tiers` de `CapitalZen/dashboard_monde`, adapté au régime de sources de BOS.*

## Pourquoi ce document existe

Le 17/08/2026, BOS a inscrit dans `Output/Message_Mining_Sans_Armature_2026-08-17.md` que le concurrent Celyssia était noté **« 4,3/5 sur 90+ avis »**, avec pour faiblesse « un maintien insuffisant au-delà du bonnet D ». Les deux affirmations venaient de blogs de comparaison rémunérés à la commission. Le relevé Trustpilot réel a donné **4,1/5 sur 2 190 avis** — un facteur 24 sur le volume — et le maintien s'est révélé être **le thème le plus loué** de la marque, pas sa faiblesse.

BOS avait pourtant averti l'entrepreneur, dans le même document, que ces blogs étaient affiliés et non neutres. **L'avertissement n'avait pas été appliqué à ses propres chiffres.** D'où cette règle : le niveau de confiance d'une source doit être explicite, pas implicite.

## L'échelle

| Tier | Nature | Usage autorisé |
|---|---|---|
| **1 — Preuve** | Données de l'entrepreneur (ventes, analytics, retours clients reçus) · études institutionnelles avec méthode et échantillon publiés (IFOP, INSEE, Cochrane) · relevés bruts avec dénominateur (avis Trustpilot/Amazon comptés) · sources officielles et textes de loi | **Chiffrable. Peut fonder une décision, entrer dans `Core/` comme fait, être cité dans du copy.** |
| **2 — Corroboration** | Presse professionnelle sourcée · communiqués d'entreprise sur leurs propres chiffres · documentation technique de fournisseurs · rapports sectoriels payants | **Utilisable, avec la source nommée.** Un chiffre de tier 2 se présente toujours avec son émetteur — c'est souvent un chiffre marketing. |
| **3 — Hypothèse** | Transcripts de vidéos de praticiens · posts X/LinkedIn d'opérateurs · articles de blog de marques · retours d'expérience individuels | **Bon pour les mécanismes et les angles, jamais pour les chiffres.** Un enseignement de tier 3 s'installe dans `Knowledge/` comme méthode ; un chiffre de tier 3 ne s'installe nulle part sans confirmation tier 1-2. |
| **4 — Intéressé** | Contenu monétisé sur ce qu'il évalue : blogs d'avis affiliés, comparatifs à commission, contenus vendant une formation sur le sujet traité | **Aucune valeur de mesure.** Utile pour une seule chose : lire quelles objections le vendeur juge nécessaire de traiter. Jamais comme preuve de quoi que ce soit. |

## Les règles opérationnelles

1. **Un chiffre de tier 3 ou 4 n'entre jamais dans `Core/` ou `Knowledge/` comme fait.** Il peut y entrer comme *affirmation attribuée* — « X affirme que… » — et seulement si ça sert à quelque chose.
2. **Quand un tier 1 contredit un tier 3-4, le tier 1 gagne sans discussion**, et la correction s'écrit explicitement plutôt que de remplacer la donnée en silence. La trace de l'erreur vaut mieux que sa disparition.
3. **Reconnaître un tier 4 :** le site touche-t-il une commission sur ce qu'il évalue ? La réponse est presque toujours oui pour un blog dont le seul contenu est « avis sur [produit] ». Signal complémentaire : aucune note négative, aucun dénominateur, aucune date.
4. **Un chiffre sans dénominateur n'est pas un chiffre.** « 4,3/5 » ne veut rien dire sans « sur combien d'avis ». Cette exigence a été encodée dans les prompts de collecte du 17/08 ; elle vaut pour toute donnée que BOS produit ou reprend.
5. **Le tier prime sur la commodité.** Une source tier 1 difficile à obtenir bat une source tier 4 immédiate. Quand seul du tier 3-4 est accessible, la conclusion se présente comme provisoire et le document dit ce qui reste à vérifier.

## Régime de sources propre à cet entrepreneur

Il consomme beaucoup de **tier 3** — transcripts de praticiens e-commerce, posts d'opérateurs. C'est légitime : ce sont d'excellentes sources de mécanismes, d'angles et de séquences opératoires, et plusieurs enseignements solides de `Knowledge/` en viennent.

Le piège est de reprendre leurs **chiffres**. Cas rencontrés le 17/08 : un pouvoir d'achat annoncé à 3 000 Md$ contredit par la vidéo elle-même ; un « 0 à 5 000 €/jour en 8 jours » qui décrit un pic isolé sur 10 jours, sans jamais mentionner le profit. Les deux étaient du tier 3 présenté comme du tier 1.

**Le réflexe à tenir :** de ces sources, prendre le raisonnement, laisser les chiffres.
