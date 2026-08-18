# Automatiser un e-commerce avec l'IA — inventaire et architecture

Ce que des opérateurs e-commerce ont réellement mis en production, et **comment** ils l'ont construit. Deux parties : l'inventaire des automatisations qui rapportent, puis l'architecture d'un pipeline créatif — de loin la partie la plus instructive.

*Distillé d'un échange entre praticiens (2026). Complément opérationnel de `AI_Leverage_Method.md`.*

> **Note de calibrage — à lire avant de s'enthousiasmer.** Tout ce qui suit vient d'opérateurs qui ont déjà des marques, du volume et des données. **Rien de tout ça ne doit être construit avant d'avoir un produit qui vend.** Automatiser un business qui n'existe pas est la forme la plus séduisante du travail fake. Ce document sert à savoir *où on va*, et à identifier les deux ou trois briques utiles dès le premier jour (elles sont signalées).

---

## 1. Le socle : le « brain »

Un dossier de connaissances chargé dans **toutes** les conversations : marques, marges, règles, façon de travailler, méthodes de création, formations assimilées.

> **« C'est 90 % du résultat, c'est la base de tout. »**

C'est le point sur lequel tous les praticiens du fil convergent, avant tout outil. Sans mémoire structurée, chaque conversation repart de zéro et produit du générique.

✅ **Utile dès le jour 1** — et c'est exactement ce que sont les fichiers `Core/` et `Knowledge/` de BOS. La différence : ici, le brain est tenu à jour automatiquement au fil des sessions.

## 2. L'inventaire des automatisations qui rapportent

Classées par ce qu'elles font gagner.

### Gagner du temps opérationnel
| Automatisation | Ce que ça remplace |
|---|---|
| **Upload et édition en masse des créatives** avec nomenclature de suivi | Des heures de manipulation manuelle hebdomadaire ⚠️ |
| **Comptabilité auto-alimentée** : CA de la boutique + dépense publicitaire, avec import des factures fournisseurs et **détection d'anomalies de prix** | Le rapprochement manuel — et les erreurs de facturation qui passent inaperçues |
| **SAV semi-automatique** : lecture des mails, contexte récupéré depuis la boutique, réponse rédigée **en brouillon**, envoi après validation humaine — le point de départ sans outil ni API, c'est le document de templates par question-type (§5, étape 3) | 80 % du temps de rédaction, sans perdre le contrôle |
| **Résumé quotidien des appels** enregistrés → points d'action, avec le contexte du business | La reprise de notes |

⚠️ **Avertissement sérieux sur l'automatisation des plateformes publicitaires :** un praticien du fil signale s'être fait bannir pour automatisation. Les plateformes ont des règles strictes sur l'accès programmatique — passer par les API officielles et leurs limites, jamais par de l'automatisation d'interface.

### Gagner de l'argent directement
| Automatisation | Le levier |
|---|---|
| **Health check profit hebdomadaire** — repérer les campagnes qui détruisent du profit, en croisant ROAS, **NC ROAS** et fenêtre d'attribution, avec calcul du profit par pays (TVA et frais de port diffèrent) | Couper au bon moment, sans couper trop tôt |
| **Détection anticipée de fatigue créative** — répétition, CPM, CTR, taux de première interaction | Agir avant la chute, pas après |
| **Cartographie du funnel publicitaire** — chaque publicité classée par **angle, niveau de conscience et persona** ; on voit combien d'annonces existent par angle et ce qui prend réellement | Savoir quel angle est saturé et lequel est vide — la meilleure aide à la décision du lot |
| **Audit mensuel du dispositif email** (campagnes et flux) | Récupérer la marge la moins chère |
| **Analyse continue des avis et questionnaires post-achat** → objections et hooks récurrents | Les angles viennent de la data, pas de l'imagination du modèle |
| **Génération de landing pages** à partir des scripts des meilleures publicités d'un angle | Cohérence entre ce qui a fait cliquer et ce qui doit convertir |

### Les chantiers impossibles à la main
Traduction complète d'un site et de ses créatives dans une deuxième langue · audit de facturation d'un fournisseur ligne par ligne sur dix mois · recréation en masse d'annonces lors d'une migration technique.

**Le principe :** l'IA ne rend pas seulement plus rapide — elle rend **possible** des chantiers qu'on aurait simplement renoncé à faire. C'est là que se trouvent les gains les plus inattendus.

---

## 3. Architecture d'un pipeline créatif — la partie qui vaut le fil

Retour d'expérience détaillé sur la génération de statiques à l'échelle. Les leçons dépassent largement le e-commerce : **c'est une méthode de pilotage d'IA sur une tâche créative.**

### Étape 0 — Ne jamais partir d'une page blanche
Le point de départ est toujours **une créative qui marche déjà** — la sienne ou une référence du marché. **On garde la structure, on change ce qu'il y a dedans.**

### Charger le contexte, dans cet ordre précis
1. **Les règles de la marque en premier.** Raison technique : les idées naissent alors déjà conformes, au lieu d'être filtrées après coup. On ne dépense pas de ressources sur des idées mortes-nées.
2. **La data de ce qui marche sur le compte, triée par dépense — pas par ROAS.** *« Un ROAS de fou sur 500 € de dépense, c'est du bruit. »* Le tri par ROAS fait remonter des accidents statistiques.
3. **Les avis clients minés en citations exploitables, classées par usage** — celle-ci pour un hook, celle-là pour le corps, celle-là pour la preuve sociale.

### Décoder avant de générer
Sur la créative de référence, séparer explicitement **ce qui reste fixe** (structure visuelle, mise en page) de **ce qui peut bouger** (angle, hook, scène). Sans cette séparation, le modèle change tout, y compris ce qui faisait marcher la créative.

### Le sprint de hooks avant les concepts
**20 à 30 hooks bruts** produits d'abord, de types différents (question, chiffre précis, confession, citation client verbatim…), **en notant pour chacun de quelle donnée il vient.**

> **Les concepts se construisent autour des meilleurs hooks — jamais l'inverse.**

### Le problème de convergence, et son vrai remède
Erreur documentée : lancer trois agents en parallèle sur la même créative. Résultat : les trois retombent sur les deux ou trois mêmes idées, déguisées en formulations différentes. **On a payé trois fois la même réponse.**

**Le correctif :** un seul agent qui écrit tout en série, puis se relit.

**Le parallèle ne fonctionne que si chaque agent a un mandat structurellement différent** — l'un doit utiliser des citations clients verbatim, l'autre viser des personas distincts, le troisième employer des mécanismes psychologiques différents. Sans mandats disjoints, le parallélisme ne produit que de la redondance coûteuse.

### Forcer la diversité en comptant, pas en demandant
> **« Aucune instruction du genre "sois créatif" ne marche. Il faut des compteurs. »**

Concrètement :
- Un **nombre minimum de types de hooks différents** exigé sur le lot final
- Des **mécanismes créatifs nommés obligatoires** — sinon tout retombe en « angle + format », générique par nature
- Des **contraintes de scène pré-assignées avant génération** : concept 1 en intérieur, concept 2 en extérieur, etc.

### La passe conformité doit être aveugle
Après la relecture qualité, une passe séparée sur les règles de la marque — confiée à un agent **qui ne voit que le texte et les règles, jamais le contexte créatif.**

**Raison :** celui qui a écrit le concept a un biais de confirmation sur son propre travail. C'est une règle générale de vérification par IA, valable bien au-delà des créatives.

### La génération d'image ne demande aucun raisonnement
Un script appelle directement l'API. Le modèle intervient **avant** (écrire le prompt) et **après** (relire l'image et auditer) — parce qu'un modèle d'image ne respecte jamais le prompt à 100 % et invente des éléments.

### Allocation des ressources
- **Dépenser sur la couche stratégique** : décoder la créative gagnante, sprint de hooks, croisement de data. C'est là que le modèle est réellement bon, et c'est ce qui détermine si ça convertit.
- **Maximum 2 boucles de révision**, jamais 3.
- **Ne jamais faire lire de gros fichiers bruts à l'agent principal** : un sous-agent lit, résume, et seul le résumé remonte.

### La conclusion des praticiens sur la qualité
Deux constats convergents et honnêtes :
- **Les meilleures créatives sortent quand le brief de base est écrit par un humain**, même avec une excellente data en entrée.
- **Les générateurs de statiques produisent du « correct »**, rarement des gagnantes majeures — le consensus est le même chez tous les intervenants. On les utilise **pour le volume**, pas pour le coup de génie.

---

## 4. Ce que BOS en retient pour sa propre méthode

Ces règles ne servent pas qu'à construire des outils — **elles décrivent comment travailler avec BOS efficacement :**

| Règle du pipeline | Traduction pour une session BOS |
|---|---|
| Charger les règles avant de générer | Donner ton contexte, ton ton et tes interdits **avant** de demander un livrable |
| Trier la data par dépense, pas par ratio | Juger sur des volumes significatifs, pas sur un chiffre flatteur |
| Sprint de hooks avant les concepts | Demander 20 hooks d'abord, choisir, puis développer |
| Diversité par compteurs | Exiger « 5 types différents » plutôt que « sois créatif » |
| Vérification aveugle | Faire relire par un regard qui n'a pas écrit |
| 2 boucles de révision max | Au-delà, on tourne en rond : changer d'angle plutôt qu'affiner |
| Le brief humain fait la différence | Ton jugement sur le marché reste l'entrée la plus précieuse |

## 5. L'ordre d'implémentation, pour quelqu'un qui démarre

Ne pas construire l'usine avant d'avoir le produit. L'ordre réaliste :

1. **Le brain** (`Core/` + `Knowledge/`) — jour 1, sans discussion. C'est 90 % du résultat.
2. **L'analyse des avis et commentaires** en objections et hooks — dès la recherche produit, avant même de vendre.
3. **Le SAV assisté** — à la première dizaine de commandes. **Le point de départ concret, avant tout outil ou automatisation :** à chaque question ou problématique traitée par mail ou en commentaire, ajouter la paire question-type / réponse validée dans un document dédié — l'application du principe de mémoire (`AI_Leverage_Method.md`, Technique 1) spécifiquement au SAV. Le document grossit comme sous-produit du travail déjà fait, sans tâche supplémentaire. Double gain : un gain de temps immédiat une fois le document fourni (coller le mail reçu + le document dans Claude suffit à produire une réponse juste dans la majorité des cas récurrents), et surtout une **garantie de qualité au moment de déléguer** — la personne qui reprend le SAV applique un standard déjà validé sur des dizaines de cas réels, au lieu d'improviser un ton et des réponses au feeling. C'est un des rares chantiers d'automatisation utile *avant* d'avoir du volume : il ne coûte rien et se construit tout seul en travaillant.
4. **Le suivi de profit** (par produit, puis par campagne et par pays) — dès les premiers euros de publicité.
5. **La cartographie des angles et la détection de fatigue** — quand il y a assez d'annonces pour que ça ait du sens.
6. **Les pipelines de génération** — en dernier, quand le volume le justifie et qu'on sait déjà ce qui convertit.

**Les étapes 1 et 2 ne coûtent rien et sont les plus rentables. Les autres attendent qu'il y ait un business à automatiser.**

---

**Dernière revue :** 2026-08-02
