# Limites connues de BOS

*Repris du `docs/methodology/known-limitations.md` de `CapitalZen/dashboard_monde`. Format d'origine conservé : chaque entrée nomme **ce qui est touché**, **la cause**, **le signe observable**, et **la voie de correction ou la raison de ne pas corriger**. Ce ne sont pas des bugs — ce sont des choses à savoir avant d'interpréter une sortie de BOS.*

---

## 1. Accès web restreint à la recherche

**Ce qui est touché.** Toute collecte de données primaires : avis clients, pages concurrentes, forums, réseaux sociaux.

**Cause.** La politique réseau de l'environnement d'exécution bloque l'accès direct aux pages. Vérifié le 17/08/2026 : `trustpilot.com`, `amazon.fr`, `reddit.com`, `google.com` et les blogs sectoriels répondent tous 000/403 au CONNECT. Seule la recherche fonctionne, et elle restitue des synthèses, pas du texte brut.

**Signe observable.** BOS rapporte des « thèmes » et des formulations « rapportées » au lieu de citations avec note et date. Aucun comptage par occurrence.

**Correction.** Déléguer la collecte à un outil hors environnement (Perplexity), avec les prompts de `Output/Prompts_Perplexity_Message_Mining_2026-08-17.md` — dénominateur exigé, extrapolation interdite. **Ce n'est pas contournable depuis la session** ; la levée se fait dans la configuration réseau de l'environnement.

---

## 2. Aucune génération d'image

**Ce qui est touché.** Les skills `brandkit`, `imagegen-frontend-web`, `imagegen-frontend-mobile`, `image-to-code` — 4 des 13 skills de design installés.

**Cause.** Aucun outil de génération d'image n'est exposé, et tous les hôtes de poids de modèles sont bloqués (`huggingface.co`, `cdn-lfs.huggingface.co`, `civitai.com`, `download.pytorch.org` — 403 au CONNECT). PyPI est joignable, mais installer les bibliothèques sans pouvoir charger de modèle ne sert à rien.

**Signe observable.** Les visuels sont rendus en PIL/Python de façon déterministe. Pour un livrable typographique (charte, visuel de post) c'est **supérieur** — le texte est net et les couleurs exactes. Pour de l'imagerie d'ambiance (matière, peau, lumière), c'est une vraie limite : voir le panneau 08 de `Output/Velune_Content_System/velune_brand_board.png`, traité en abstraction faute de mieux.

**Correction.** Autoriser `huggingface.co` dans la politique réseau, ou fournir une clé d'API d'un service hébergé. Réserve : sans GPU (4 cœurs CPU), un modèle local mettrait plusieurs minutes par image.

---

## 3. Sensibilité aux sources intéressées

**Ce qui est touché.** Toute donnée chiffrée sur un concurrent ou un marché.

**Cause.** Jusqu'au 17/08/2026, BOS n'avait pas de hiérarchie de sources. Les blogs de comparaison rémunérés à la commission remontent en tête des recherches et se présentent comme des tests neutres.

**Signe observable — cas réel.** « Celyssia 4,3/5 sur 90+ avis » et « faiblesse sur le maintien au-delà du bonnet D » ont été inscrits comme faits. Le relevé Trustpilot a donné **4,1/5 sur 2 190 avis** et le maintien s'est révélé être le thème **le plus loué** de la marque. Facteur 24 sur le volume, inversion complète sur le fond.

**Correction.** `Knowledge/Source_Tiers.md` + la règle correspondante dans `CLAUDE.md`. Le défaut résiduel : la classification est manuelle, donc elle dépend de la vigilance de BOS à chaque usage.

---

## 4. Les chiffres des praticiens ne sont pas vérifiables

**Ce qui est touché.** Les enseignements tirés de transcripts vidéo et de posts d'opérateurs, qui constituent une part importante de `Knowledge/`.

**Cause.** Un praticien qui raconte son résultat n'a ni méthode publiée, ni dénominateur, ni contradicteur. Et une part de ces contenus sert à vendre une formation.

**Signe observable.** Cas du 17/08 : un pouvoir d'achat annoncé à 3 000 Md$ contredit par la vidéo elle-même ; un « 0 à 5 000 €/jour en 8 jours » qui décrivait un pic isolé sur 10 jours calendaires, sans jamais mentionner le profit ni le spend publicitaire.

**Correction.** Aucune, structurellement — et c'est assumé. Ces sources restent précieuses **pour les mécanismes**. La règle est de prendre le raisonnement et de laisser les chiffres (`Source_Tiers.md`, tier 3).

---

## 5. BOS ne mesure rien de ce qu'il produit

**Ce qui est touché.** L'ensemble des livrables : copy, visuels, analyses, plans.

**Cause.** Aucun livrable n'a encore rencontré le marché. Les vérifications se font contre des sources secondaires et contre le jugement de BOS lui-même — ce qui est un miroir, pas une boucle.

**Signe observable.** BOS peut produire un volume important de travail cohérent sans qu'aucune donnée externe ne vienne le valider ou l'infirmer. Le 17/08 : une cartographie de chaîne de valeur, un skill, une planche d'identité, quatre visuels, un message mining, dix prompts, six ajouts de playbook — zéro point de mesure extérieur.

**Correction.** La Phase 6 du skill `teardown` (enregistrer la prédiction avant de déployer, vérifier à l'échéance) et la boucle de vérification de `AI_Leverage_Method.md`. **Les deux restent inertes tant qu'aucun livrable n'est publié.**

---

## 6. La mémoire de BOS est ce qui est écrit, pas ce qui a été dit

**Ce qui est touché.** La continuité entre sessions.

**Cause.** Le contexte de conversation est résumé ou perdu ; seuls `Core/`, `Knowledge/` et `Output/` persistent. Une décision prise en conversation et non écrite disparaît.

**Signe observable.** Une piste écartée sans motif écrit revient sur la table quelques semaines plus tard (cas des étiquettes personnalisées, réévaluées le 13/08 alors que le raisonnement existait).

**Correction.** Écrire le **motif** et pas seulement la conclusion — appliqué depuis le 13/08 sur les segments écartés. C'est la raison d'être du protocole de mise à jour des fichiers `Core/`.

---

## 7. Contradiction possible entre documents de `Knowledge/`

**Ce qui est touché.** Les playbooks qui se sont enrichis de sources différentes au fil du temps.

**Cause.** Chaque source apporte sa nuance ; rien ne garantit qu'un ajout ne contredise pas un passage antérieur d'un autre document.

**Signe observable.** Cas du 17/08 : « le marché français du sans-armature est au stade 3-4 » écrit le matin, corrigé l'après-midi en « le marché est stratifié par gamme de prix, dropship au stade 2-3 et DTC installées au stade 5 ». La première formulation n'était pas fausse, elle était incomplète.

**Correction.** `scripts/check_refs.py` vérifie les liens, pas la cohérence de fond — celle-ci reste à la charge de BOS au moment de l'usage. Quand une contradiction est détectée, la règle est de **corriger explicitement en gardant la trace**, jamais de remplacer en silence.

---

## 8. Google Trends inaccessible — et aucun outil ne le contourne depuis ici

**Ce qui est touché.** Toute validation de demande par volume de recherche : le cœur de l'étape 2 du moteur « premier euro ».

**Cause.** `trends.google.com` renvoie **403 au niveau du CONNECT** — le proxy refuse d'ouvrir le tunnel avant tout handshake TLS. L'API officielle Google Trends existe mais est en **alpha sur liste d'attente depuis juillet 2025**, et les retours convergent : quasiment personne n'y entre.

**Signe observable.** Un outil de contournement par navigateur furtif (`pi-infected/trends-surfer`, testé le 18/08/2026) échouera exactement de la même façon. **La furtivité résout la détection de robot, pas le blocage réseau** : empreinte TLS, cookies et résolution de Turnstile opèrent *à l'intérieur* d'une connexion établie. Distinction à retenir pour tout futur outil proposé sur ce type de blocage.

**Correction.** Exécuter l'outil sur une machine sans proxy — `trends-surfer` est un plugin Claude Code fait pour ça, et il remplace avantageusement toute collecte manuelle. Les résultats se collent ensuite dans BOS, comme pour les verbatims Trustpilot.

---

**Dernière revue :** 2026-08-17
