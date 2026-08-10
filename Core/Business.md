# Business

**Stade :** pivot en cours (07/08/2026). L'e-commerce (Velune) est **mis en pause** après ses tout premiers signaux réels (voir Historique ci-dessous) — nouvelle direction retenue : **vente d'intégration/automatisation IA aux PME**, business de service.

## Direction actuelle — Intégration/automatisation IA pour PME (depuis le 07/08/2026)

**Modèle :** vendre des automatisations et outils construits avec Claude Code à des petites entreprises (artisans, commerces locaux, PME) — pas de produit physique, pas de stock, pas d'avance de trésorerie nécessaire. Business de service à marge quasi totale, ce qui règle structurellement la contrainte de budget zéro qui pesait sur l'e-commerce.

**Deux méthodes d'entrée retenues :**
1. **Méthode Reddit** — vivre dans r/smallbusiness (et équivalents : r/entrepreneur, r/SaaS, r/NoCode), repérer une vraie douleur exprimée par un dirigeant, construire gratuitement une solution avec Claude Code, la proposer sans démarchage préalable. Pied dans la porte → upsell vers des projets payants.
2. **Sites web pour commerces locaux** — repérer des entreprises locales avec un site absent ou médiocre, construire une maquette gratuite avec Claude Code, l'envoyer directement. Conversion en projet payant (quelques centaines d'euros), puis upsell vers des automatisations (prise de rendez-vous, suivi client, etc.).

**Méthodologie complète déjà disponible :** `Knowledge/AI_Integration_Playbook.md` — diagnostic chiffré, cadre légal (AI Act), formation, premiers gains mesurés, sur-mesure, pilotage. Couvre largement plus en profondeur que les contenus qui ont déclenché le pivot (déjà distillé et évalué de façon critique avant même ce soir).

**Secteur recommandé (07/08/2026, recherche BOS sur la zone Franconville 95130/gare) :** **cabinets dentaires** — cluster réel identifié sur rue de la Station (au moins 5 cabinets), tâches de fond répétitives (prise de RDV, relances patients, devis) exactement adaptées à l'automatisation, marges solides (pas de mono-commerce fragile). **Secours : agences immobilières** — cluster confirmé jusque sur la place de la Gare elle-même, mêmes atouts (suivi client, génération de documents). Artisans (plombiers/électriciens) écartés en premier choix : forte concurrence de plateformes de leads nationales, plus difficile de différencier. **Limite de cette recherche à connaître :** pas d'accès à une carte/API de géolocalisation — ce sont des patterns de densité par annuaires (PagesJaunes, mairie), pas une liste d'entreprises géolocalisées à 5 km exacts. Vérification terrain à faire par l'entrepreneur avant le premier contact.

**Secteur confirmé le 07/08/2026 : cabinets dentaires.** Nuance apportée par l'entrepreneur, pertinente et à garder : ils ont en général déjà une secrétaire, mais un vrai budget. **Conséquence sur l'angle de pitch :** ne jamais présenter l'automatisation comme un remplacement de la secrétaire (objection n°1 du playbook, « l'IA va me remplacer ») — viser ce qu'elle n'a pas le temps de faire. Cadrage : « libère du temps », jamais « remplace ».

**Correction du 07/08/2026 (soir) — la prise de RDV passe par Doctolib (ou téléphone).** Repéré à temps par l'entrepreneur avant tout contact client : Doctolib gère déjà la prise de RDV 24/7 et un rappel automatique basique — proposer ça comme angle aurait été immédiatement disqualifiant en conversation. **Angles qui restent réellement ouverts, indépendants de Doctolib :**
- Relance des devis en attente (Doctolib ne fait pas de suivi commercial)
- Rappel de contrôle pour les patients sans RDV depuis 6-12 mois (revenu récurrent qui se perd)
- Remplissage des créneaux annulés à la dernière minute (liste d'attente non exploitée)
- Demande d'avis Google automatique après RDV (levier d'acquisition locale, rarement systématisé)

**Question de diagnostic à poser en premier contact, pas à supposer :** est-ce que le cabinet a une liste patient exploitable (contact, dernière visite, devis en cours) en dehors de Doctolib, ou tout est enfermé dans Doctolib sans export simple ? Conditionne la faisabilité technique réelle.

**Recherche approfondie sourcée le 07/08/2026 — verdict par angle :**
- **Rappel de RDV / no-show : angle à écarter.** 4,7 % de no-show chez les dentistes en 2024 (source primaire Doctolib, confirmée par la presse professionnelle — `information-dentaire.fr`, `lequotidiendumedecin.fr`) — chiffre réel, mais Doctolib vend déjà cette solution et communique dessus (rappels automatiques, taux divisé par 3). Terrain occupé.
- **Relance des devis en attente : plausible mais concurrencé.** Le chiffre « 50 % des devis jamais suivis » vient de **La Fraise**, éditeur spécialisé (3000+ dentistes clients) — c'est un chiffre marketing d'un concurrent déjà bien implanté, pas une étude indépendante. Le problème est réel (la concurrence en vit), mais le marché n'est plus vierge.
- **Rappel des patients inactifs (6-12 mois sans RDV) : angle le plus différencié.** Fréquence clinique légitime (Cochrane), aucun concurrent spécialisé identifié dessus — mais zéro donnée externe sur le taux de perte ou l'impact CA. À prouver avec les données du cabinet pilote, pas avec une stat nationale (elle n'existe pas).
- **Liste d'attente sur annulation : à vérifier au cas par cas.** Peut-être déjà couvert par les offres Doctolib récentes (source secondaire, non confirmée à 100 %) — à demander directement au cabinet.
- **⚠️ Avis Google automatique — angle à reformuler, pas à garder tel quel.** Risque déontologique réel : le décret 2020-1658 (art. R.4127-215 CSP) interdit aux chirurgiens-dentistes de solliciter des témoignages à but promotionnel, et l'Ordre national milite activement en 2026 pour faire supprimer les avis Google des praticiens (`information-dentaire.fr`, `ordre-chirurgiens-dentistes.fr`). Une relance automatique systématique après chaque RDV correspond exactement à la pratique visée. **Reformulation nécessaire :** questionnaire de satisfaction interne (détection d'irritants), envoi vers Google non systématique/non filtré sur la note — c'est ce que font les concurrents existants (Carescore 39,50€/mois, DentalIAssist) pour rester conformes.

**Stratégie de pitch qui en découle :** au premier contact, demander ce qui est déjà inclus dans l'abonnement Doctolib du cabinet (tranche le flou sur devis/liste d'attente) ; remplacer les statistiques nationales absentes par un comptage réel sur les données du cabinet (devis en attente, patients sans RDV depuis 6-12 mois) — preuve locale, plus convaincante qu'un chiffre national de toute façon.

Sources principales : information-dentaire.fr, lequotidiendumedecin.fr, media.doctolib.com (communiqué officiel), ordre-chirurgiens-dentistes.fr, cochrane.org, indy.fr (comparatif logiciels dentaires).

**Ce qui reste à faire, dans l'ordre :** repérer 3-5 cabinets précis autour de la gare de Franconville ; en parallèle, méthode Reddit ; produire la première solution gratuite ; convertir en premier client payant. Suivi des missions réelles : `Core/Journal_Missions_IA.md`.

## Historique — E-commerce / Velune (en pause depuis le 07/08/2026)

Direction retenue le 29/07/2026, produit tranché le 04/08/2026 (sous-vêtement sans armature/sans couture, archétype « Velune »), marque construite et lancée le 06/08/2026 : comptes Instagram et TikTok créés (`velune.fwi`), système de contenu et de marque livré (`Output/Velune_Content_System/`), premier post publié sur les deux plateformes, premier signal réel obtenu (un like, après avoir dépassé un blocage réel de peur du jugement — voir `Core/Diagnosis.md`). Sourcing 1688/Alibaba préparé (`Output/Sourcing_Soutien_Gorge_Sans_Armature_2026-08-04.md`) mais RFQ jamais envoyées.

**Raison de la pause :** préférence exprimée pour la vente d'automatisation IA après plusieurs contenus reçus sur le sujet, le 07/08/2026 — au moment même où Velune obtenait sa toute première traction. Nommé et discuté avant la décision (voir `Core/Diagnosis.md`) ; décision prise consciemment par l'entrepreneur, pas un abandon silencieux.

**Condition de reprise :** tout le travail est conservé en l'état (comptes, contenu, sourcing) — reprise possible à tout moment sans repartir de zéro si la nouvelle direction ne convient pas ou en complément plus tard.

## Modèle visé (historique, e-commerce)
Boutique de niche brandée construite autour d'un produit à fort potentiel, acquisition Meta Ads, marché européen. Référence méthodologique : `Knowledge/Ecom_Meta_Ads_Playbook.md`.

## Territoire
**Mode & accessoires féminins à utilité** — croisement des niches « rose » et « mode à utilité », choisi le 29/07/2026. Structure : boutique de niche large (le site ne bouge pas d'un test à l'autre, seule la fiche produit change). Détail complet : `Output/Territoire_Mode_Feminine_Utilite_2026-07-29.md`.

Raison du choix : c'est le seul croisement qui active les deux moteurs — identité/émotion (organique) et problème-solution (payant). Le contenu produit pour l'organique se recycle directement en créatives payantes.

**Précision du 01/08/2026 — territoire identifié, pas habité.** Interrogé sur le sujet, l'entrepreneur a répondu : *« c'est un univers que j'ai identifié comme porteur, pas que j'habite. »* Ce n'est pas un problème de choix — le territoire a été retenu sur des critères de marché, ce qui est la bonne base (`Knowledge/Entrepreneur_Success_Factors.md` §8 : la familiarité départage, elle ne sélectionne pas). Mais la conséquence est opérationnelle et doit être tenue :

- **Le coût d'immersion est réel et se paie d'avance** — vocabulaire exact, hiérarchie réelle des frustrations, codes de l'audience (`Knowledge/Customer_Research_SOP.md` Étape 1 bis).
- **Le point faible attendu n'est donc pas le choix du produit mais la couche message** : angles et copy qui sonnent justes pour une audience dont on n'est pas membre.
- **C'est très largement portable par BOS** — cartographier les écoles de pensée d'un marché, ses points de friction et son vocabulaire est exactement ce que BOS sait faire à la place de l'entrepreneur. À produire avant toute écriture de créative.
- **Option restée ouverte, non tranchée :** si un univers réellement habité par l'entrepreneur passe aussi les critères économiques, il l'emporterait sur celui-ci. La question n'a pas été posée et ne sera pas relancée (mode A).

## Stratégie d'entrée (historique Velune)
**Organique d'abord**, bascule payante ensuite (`Knowledge/Ecom_Organic_Launch_Playbook.md`). Décision prise après révision du diagnostic : la trésorerie ne bloque plus, la régularité devient le facteur critique.

## Produit (historique Velune)
**Tranché le 04/08/2026 :** sous-vêtement sans armature/sans couture, marque Velune. Voir Historique plus haut.

## Marché (historique Velune)
France, orientation retenue avec le lancement organique. À trancher plus précisément si Velune reprend.

## Finances
- **Trésorerie disponible aujourd'hui :** **quasi nulle** (rectifié le 01/08/2026 — les 1 500 € sont un objectif, pas un capital détenu)
- **1 500 € = objectif de trésorerie à fin décembre 2026**, pas un point de départ
- **Capacité d'épargne mensuelle :** **nulle jusqu'à l'entrée en poste.** Source identifiée : le futur emploi de conducteur (TP Marchandises sur Porteur, puis ADR / citernes), une fois les charges déduites. Déclaré le 01/08/2026 : « rien tant que je n'ai pas l'emploi en question ».
- **Conséquence :** la date d'entrée en poste est **le jalon qui commande tout le calendrier financier** du projet — pas une variable secondaire.
- **Seuil de référence :** ~3 000 € pour lancer des tests Meta Ads sérieux ; 5 000 € pour tester et itérer sans contrainte

**Ce que change le budget quasi nul.** Rien sur la stratégie : la voie organique était déjà retenue et elle ne demande pas de budget publicitaire. Ce qui change, c'est que **le coût de démarrage doit être ramené à son minimum absolu** et que rien ne peut être engagé avant que des revenus existent.

**Le minimum réel pour démarrer :**

| Poste | Montant | Quand |
|---|---|---|
| Un échantillon produit (pour filmer) | 15-40 € | Dès le produit tranché |
| Nom de domaine | ~10 € | Avec la boutique |
| Shopify | ~1 €/mois les premiers mois, puis ~30 € | **Seulement quand il y a de la demande à convertir** |
| Tournage, montage, publication | **0 €** | Un téléphone suffit |

**Total pour exister en ligne et publier : de l'ordre de 30 à 50 € sur le premier mois.** Le reste s'auto-finance : les premières ventes paient la boutique, la boutique paie les échantillons suivants, et la transition semi-marque (1 000-2 000 €) ne se déclenche qu'après 50-100 ventes — donc financée par le business, jamais par l'épargne.

**Séquence de financement retenue :** contenu (0 €) → audience et signaux de demande → premières ventes en fulfillment sans stock → réserve constituée → bascule payante prudente. C'est la seule séquence qui fonctionne sans capital de départ, et elle est documentée (`Knowledge/Ecom_Organic_Launch_Playbook.md`).

## Temps disponible
**2 h par jour** (~14 h/semaine, ~300 h sur l'horizon de l'objectif). Format de travail recommandé : un bloc unique de 2 h en concentration totale, ou 3 × 50 min si le rythme de la journée l'impose (`.claude/skills/organize/SKILL.md`). **Tournage en lots** — une session de tournage alimente plusieurs jours de publication.

## Acquisition (historique Velune)
Organique lancé (Instagram + TikTok, `velune.fwi`), Meta Ads prévu plus tard si reprise.

## Actifs déjà en place
- **Une base de méthode complète et à jour** — PMF, recherche client, offre, SEO, e-commerce, IA, intégration IA en entreprise. C'est un actif réel : la plupart des débutants paient une formation pour moins que ça.
- **Un copilote IA** capable d'exécuter recherche, analyse concurrentielle, construction d'automatisations et d'outils (Claude Code), copy, structure de site, prospection.
- **Velune** : marque construite, comptes créés, premier contenu en ligne — en pause, pas perdu.

## Outils
**Direction actuelle (intégration IA) :** Claude Code — coût quasi nul, c'est l'outil de production principal.
**Historique Velune :** Instagram/TikTok (comptes créés). Shopify, gestionnaire de publicités Meta à prévoir si reprise.
