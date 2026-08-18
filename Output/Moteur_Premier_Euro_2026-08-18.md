# Moteur « problème prouvé → premier euro »
*18/08/2026 — méthode conçue pour atteindre 5 € réels, puis se répéter.*

## Le principe

On ne cherche pas une idée. On cherche **un problème que des gens tapent déjà dans Google**, pour lequel **quelqu'un paie déjà quelque chose**, et dont **BOS peut produire la solution en une session**.

Trois filtres dans cet ordre. Une piste qui saute le premier est une intuition, pas une piste.

---

## Étape 1 — Générer les hypothèses (BOS)

Une hypothèse de problème n'est pas une idée de produit. Format imposé :

> « **[Qui]** n'arrive pas à **[faire quoi]**, et se débrouille aujourd'hui avec **[quel contournement]**. »

Le contournement est obligatoire : sans lui, la douleur n'est pas prouvée (`.claude/skills/find/SKILL.md` Phase 4 — la chaîne énervement → contournement → dépense).

**Les trois gisements exploitables ici, par ordre de force :**

1. **Le monde qu'il va habiter — le transport routier.** ADR, citernes, FIMO/FCO. Avantage décisif : il sera **dedans**, donc il verra les vrais irritants et parlera la langue. C'est l'avantage que `Ecom_Meta_Ads_Playbook.md` appelle « connaître sa niche de l'intérieur — celui qui ne s'achète pas », et c'est exactement ce qui manquait à Velune (territoire identifié, pas habité).
2. **Le monde qu'il vient de disséquer — l'e-commerce débutant.** Trois semaines de recherche réelle : sourcing 1688, message mining, verbatims Trustpilot, calcul de marge. Il connaît maintenant les pièges que 90 % des débutants ignorent.
3. **Les problèmes administratifs français.** Volume énorme, douleur chronique, solutions publiques peu lisibles. Terrain à traiter avec prudence : jamais de conseil juridique ou fiscal personnalisé.

---

## Étape 2 — Prouver la demande (sur TON poste)

**Google Trends est inaccessible depuis l'environnement de BOS, définitivement.** `trends.google.com` renvoie **403 au niveau du CONNECT** : le proxy refuse d'ouvrir le tunnel avant même le handshake TLS. C'est un blocage de politique réseau, pas une détection de robot.

**Conséquence importante pour le choix de l'outil :** un navigateur furtif n'y change rien. La furtivité (empreinte TLS, cookies, résolution de Turnstile) opère *à l'intérieur* d'une connexion établie — elle ne peut pas en ouvrir une que la politique refuse. Aucun outil ne contournera ça depuis ici.

### La bonne solution : `trends-surfer`, sur ta machine

[`pi-infected/trends-surfer`](https://github.com/pi-infected/trends-surfer) est un **plugin Claude Code** qui interroge Google Trends en langage naturel via une session Chrome furtive. Il remplace intégralement le protocole manuel : plus de copier-coller de tableaux, tu poses la question et les données arrivent dans la conversation.

**Ce qu'il renvoie :** intérêt dans le temps · requêtes et sujets associés (dont les « en hausse ») · intérêt par région · tendances du moment. Exactement ce que demande cette étape.

**Signes que l'outil est sérieusement fait :**
- Il réimplémente les endpoints modernes plutôt que d'utiliser `pytrends`, **archivé en avril 2025** et bloqué par Google à cause de l'empreinte TLS de Python.
- Il impose un **délai aléatoire de 30 à 90 secondes entre deux requêtes, non contournable**, persisté sur disque. C'est une contrainte volontaire pour respecter les limites de Google — un outil qui ne l'aurait pas serait un outil qui te fait bannir.
- Il documente honnêtement les pièges (le 429 de Google sur les widgets, le fait que `/trends/explore` consomme le budget avant même ta requête).

### Installation

Le README contient une section **écrite explicitement pour qu'un agent IA la suive**. Le plus simple : donner l'URL du dépôt à ton Claude Code local et lui demander d'installer — il a les instructions pas à pas.

Manuellement, dans l'ordre :

1. `uv --version` — si absent : `python -m pip install --user uv`
2. `uv run patchright install chrome` depuis le dossier cloné — **c'est l'étape qu'on rate**, elle ne se fait pas toute seule au démarrage du serveur
3. `/plugin marketplace add <chemin-absolu-du-dossier>` puis `/plugin install trends_surfer@trends-surfer-local` puis `/reload-plugins`
4. Vérifier avec l'outil `trends_health` → attendre `chrome_available: true`

### Le flux de travail qui en découle

BOS tourne ici, le plugin tourne chez toi. Donc : **tu poses les questions Trends à ton Claude Code local, tu me colles les résultats.** C'est le même schéma que les verbatims Trustpilot, qui a bien fonctionné — sauf que là, la collecte est automatisée au lieu d'être manuelle.

### Ce qu'il faut demander, pour chaque hypothèse

France · **12 derniers mois** · le terme du *problème*, pas d'un produit.

1. L'**intérêt dans le temps** — plate, montante, descendante, ou saisonnière (des pics réguliers = fenêtre de vente prévisible).
2. Les **requêtes associées en hausse** — c'est là que sont les vrais mots des gens, et les problèmes qu'on n'avait pas devinés.
3. Une **comparaison avec un terme témoin** dont on sait qu'il a du volume. Google Trends ne donne que du **relatif** — un « 100 » seul ne veut rien dire.

### Ce qui invalide une hypothèse, immédiatement

| Signal | Verdict |
|---|---|
| Courbe plate au ras de zéro sur 12 mois | Personne ne cherche → écarter |
| Courbe en chute continue | Problème en train de disparaître → écarter |
| Aucune requête associée en hausse | Sujet mort ou trop étroit pour Trends |
| Pic unique lié à une actualité | Effet de mode, pas un problème → écarter |

**Un « pas assez de données » n'est pas un échec** — ça veut dire que le terme est trop rare pour l'outil. Élargir d'un cran et recommencer.

## Étape 3 — Vérifier que quelqu'un paie déjà (BOS)

La demande de recherche prouve l'intérêt. **Elle ne prouve pas la volonté de payer.** Ce qui la prouve : une solution payante qui existe et qui vit.

Je cherche, pour chaque hypothèse validée à l'étape 2 :
- Un produit payant sur le même problème, son prix, son ancienneté, ses avis
- Ce que ses avis négatifs reprochent — c'est là qu'est la place à prendre (méthode identique à celle qui a produit la cartographie Celyssia/Leishape)

**Si personne ne vend rien sur ce problème, c'est un signal négatif**, pas une opportunité — sauf motif structurel identifié (`CLAUDE.md`, règle sur la saturation).

**Repères de prix relevés sur le marché français du produit numérique :** templates Notion/Canva/Figma **5-49 €** · guides et eBooks PDF **9-39 €** · packs de presets **15-79 €**. Les ventes de produits numériques par créateurs indépendants français ont progressé de **+40 % entre 2023 et 2025** ([payfacile](https://www.payfacile.com/fr/blog/tools-and-tips/comment-vendre-des-fichiers-numeriques)). Le premier palier à 5 € tombe exactement dans la fourchette basse — c'est atteignable avec **une seule vente**.

---

## Étape 4 — Passer les 6 critères (BOS)

Ceux de `Core/Business.md` : zéro euro d'avance · livraison instantanée · charge opérationnelle marginale nulle · l'IA produit l'essentiel · demande prouvée · vérifiable et honnête.

**Un échec sur un seul critère = piste écartée, motif écrit.** La liste des écartées a de la valeur : elle évite de reposer la question dans trois mois (`MAINTENANCE.md`).

---

## Étape 5 — Produire la plus petite chose vendable (BOS produit, TOI valides)

Pas un produit complet. **Le plus petit objet qui résout entièrement un problème précis.** Un problème résolu à fond bat cinq problèmes effleurés (`.claude/skills/offer/SKILL.md`).

Je produis le contenu, la page de vente, le visuel. Tu valides et tu publies.

---

## Étape 6 — Encaisser 5 € (TOI)

- **Plateforme :** une qui encaisse sans frais fixes ni abonnement — à choisir quand la piste sera connue, le choix dépend du format.
- **Statut :** micro-entrepreneur, gratuit, ~15 min en ligne, zéro cotisation tant que zéro chiffre d'affaires. Pas bloquant pour la première vente, indispensable dès que ça se répète.
- **Le seul objectif de cette étape :** qu'un inconnu paie. Pas dix. Un.

---

## Étape 7 — Mesurer, puis décider (BOS + TOI)

C'est l'étape que la plupart sautent, et c'est celle qui rend le reste cumulatif. À enregistrer **avant** de publier : combien de visiteurs attendus, quel taux de conversion espéré, à quelle date on regarde.

Puis la seule question qui compte : **répéter sur un autre problème, ou approfondir celui-ci ?** La réponse vient des chiffres, pas d'un plan décidé à l'avance.

---

## Où on en est maintenant

**Fait :** le moteur est posé, les repères de prix sont sourcés, les trois gisements d'hypothèses sont identifiés.

**Première hypothèse à tester — la plus forte, et elle vient de ton profil :**

> Les candidats à la **FIMO / FCO** doivent réussir un QCM de **60 questions, 36 bonnes réponses minimum**, pour obtenir leur carte de qualification. La **FCO se repasse tous les 5 ans**, ce qui crée un flux continu de candidats. Des supports d'entraînement gratuits existent déjà — donc la demande d'entraînement est réelle et documentée.

Ce qui reste à prouver avant d'y toucher : le **volume de recherche** (étape 2, ton navigateur) et l'existence d'une **offre payante vivante** (étape 3, moi).

**Réserve honnête sur cette piste :** tu n'as pas encore passé ces formations. Tant que ce n'est pas fait, tu n'as pas l'avantage du terrain qui rend cette hypothèse forte — tu aurais le même handicap qu'avec Velune. À arbitrer selon ton calendrier d'entrée en poste.
