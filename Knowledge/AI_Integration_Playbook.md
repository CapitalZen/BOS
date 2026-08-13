# Intégrer l'IA dans une entreprise — Playbook

Méthode d'intégration de l'IA en PME, utilisable dans les deux sens : pour le business de l'entrepreneur lui-même, ou comme **offre de service** vendue à ses clients (intégrateur / consultant IA).

*Distillé de : « Intégrer l'IA dans une entreprise — guide de terrain » (état du droit au 28 juillet 2026) ; « Comment Automatiser un Business avec l'IA » (Yassine Sdiri / ChatflowAI) ; classeur d'évaluation CHECKLISTIA (portes de phase et seuils).*

> **Attention aux dates.** La partie légale ci-dessous reflète l'état du droit au 28 juillet 2026. Vérifier les échéances avant de la réutiliser avec un client. Ce n'est pas un conseil juridique — les arbitrages relèvent d'un juriste.

---

## 0. Posture — deux sources qui se contredisent, et laquelle suit BOS

Les deux guides décrivent la même séquence (diagnostic → formation → sur-mesure) mais s'opposent sur le ton :

| | Argumentaire de survie | Argumentaire de mesure |
|---|---|---|
| Accroche | « Adaptez-vous ou disparaissez, comme Kodak » | « L'IA est déjà entrée chez vous sans cadre. La question est de l'encadrer. » |
| Chiffres | « +70 % de productivité », « −40 % de tickets » | Aucun chiffre non mesuré sur le périmètre du client |
| Effet | Décisions précipitées → projets abandonnés à 6 mois | Vente plus lente, projets qui tiennent |

**BOS suit le second.** Un chiffre annoncé qu'on n'a pas mesuré soi-même devient une dette : le client le retient, et il sert de référence à l'arrivée. Le vrai déclencheur commercial est plus solide que la peur : *des salariés utilisent déjà des outils d'IA grand public avec les données de l'entreprise, sans cadre, sans formation, sans que la direction le sache.* Ce n'est plus un pari sur l'avenir, c'est un problème présent.

Repères de contexte utilisables (sourcés) : le Future of Jobs Report 2025 du WEF projette 92 M d'emplois supprimés et 170 M créés d'ici 2030 (solde net +78 M) — une recomposition des compétences, pas un effondrement ; McKinsey estime jusqu'à 30 % des **heures travaillées** automatisables d'ici 2030 — un plafond de scénario, qui déplace des tâches à l'intérieur d'un poste plus qu'il ne supprime le poste.

## 1. Le cadre légal — avant tout choix d'outil

Cette étape passe avant le diagnostic parce que ses conclusions conditionnent les outils retenus.

**Calendrier AI Act :**
| Date | Ce qui s'applique |
|------|-------------------|
| Février 2025 | Interdictions (art. 5) — en vigueur |
| Août 2025 | Obligations modèles à usage général — en vigueur |
| **2 août 2026** | Application générale, **articles 4 et 50**, pouvoirs de sanction |
| 2 décembre 2027 | Systèmes à haut risque, annexe III — reporté |
| 2 août 2028 | Systèmes à haut risque, annexe I — reporté |

**Le contresens à corriger dès le premier rendez-vous :** le paquet Digital Omnibus a décalé les obligations *haut risque*, et la presse a retenu « l'AI Act est reporté ». **Le report ne couvre ni l'article 4 ni l'article 50.** À dire par écrit.

- **Article 4 — compétence IA obligatoire.** L'entreprise qui déploie des systèmes d'IA doit garantir un niveau de compétence suffisant chez ceux qui les utilisent pour son compte. Ça vise le déployeur, pas seulement l'éditeur. À produire **et conserver** : inventaire des systèmes et des populations concernées, programme de formation adapté aux rôles, preuve (dates, contenus, présences, évaluations). Sans traçabilité, la formation a eu lieu mais ne se démontre pas.
- **Article 50 — transparence.** Informer les personnes qu'elles interagissent avec une IA ; signaler les contenus générés ou manipulés diffusés à l'extérieur.
- **Sanctions** — jusqu'à 35 M€ ou 7 % du CA mondial pour les manquements les plus graves ; plafonds inférieurs pour les autres catégories. Pouvoirs activés depuis le 2 août 2026.

**Qualification « haut risque » — à faire maintenant même si les obligations sont reportées** (elle détermine la trajectoire et le coût réel) : recrutement (tri de CV, présélection, évaluation), crédit, gestion des salariés (attribution de tâches, évaluation, promotion, rupture), éducation, santé, sécurité, infrastructures critiques.
→ **Le tri de CV est le piège classique** : c'est le « quick win » que réclament les DRH, et c'est un système à haut risque. Le dire avant la mise en production, pas après.

**RGPD, qui reste applicable par-dessus :** base légale du traitement, localisation et transferts hors UE, réutilisation pour entraînement (**à lire au contrat, jamais à supposer** — beaucoup d'offres grand public s'autorisent l'entraînement, les offres pro généralement non), données sensibles et secrets d'affaires, décision automatisée (art. 22).

## 2. Diagnostic — mesurer avant de changer

Étape la plus souvent sautée ; son omission rend tout le reste indémontrable.
**Règle : ne nommer aucun outil pendant cette phase.** Un diagnostic qui aboutit à une liste de logiciels a échoué — il doit aboutir à une liste de processus chiffrés.

**Les 5 mesures de référence, par processus candidat :** volume hebdomadaire · durée unitaire · personnes impliquées (le comptage nominatif révèle les validations invisibles) · taux de reprise · coût horaire chargé.

**Chronométrer, ne pas demander.** « Combien de temps ça vous prend ? » se trompe dans les deux sens — tâches pénibles surestimées, tâches routinières sous-estimées. L'écart atteint couramment 30 à 50 %.

**Cartographier le flux réel, pas le flux officiel.** L'écart entre les deux est en général l'endroit exact où se trouve le gain. Pour chaque processus : déclencheur, étapes, points d'attente, sortie, **traitement des exceptions** (systématiquement omis, et déterminant).
→ **Un processus dont plus de ~30 % des cas sont des exceptions n'est pas automatisable en l'état** : il est à redéfinir d'abord. Automatiser un processus instable, c'est industrialiser le désordre.

**Prioriser :**
- **Impact** = volume hebdo × durée unitaire × coût horaire × 52 → **une valeur en euros par an**, pas une appréciation.
- **Effort** = intégration technique + accompagnement du changement + maintenance annuelle. Le deuxième terme est presque toujours sous-estimé : compter **au moins autant** que le premier (coefficient 1,0).

| | Impact faible | Impact fort |
|---|---|---|
| **Effort faible** | Si le temps le permet | **Commencer ici** |
| **Effort élevé** | Écarter | Après un premier succès |

Ne jamais attaquer « effort élevé / impact fort » en premier, même si c'est le sujet qui intéresse la direction. Un premier succès mesuré achète la crédibilité des chantiers lourds ; un premier échec sur un gros sujet ferme le budget pour deux ans.

**Livrable du diagnostic** — un document court : 3 à 5 processus prioritaires chiffrés en €/an ; pour chacun mesure de référence, gain estimé, effort estimé, risque principal ; les contraintes de données ; **et ce qui a été écarté, avec la raison.** Un diagnostic qui ne dit non à rien n'a pas arbitré.

## 3. Encadrer l'usage existant (rapide, gratuit, réduit le risque immédiat)

1. Recenser les outils d'IA réellement utilisés. Poser la question **sans sanction annoncée**, sinon les réponses sont fausses.
2. Classer les données en trois niveaux : librement transmissibles / transmissibles à un fournisseur sous contrat / jamais transmissibles.
3. Publier **une règle d'une page** : ce qui est autorisé, ce qui ne l'est pas, vers qui remonter un doute. Une page lue vaut mieux qu'une charte de vingt pages ignorée.
4. Basculer les usages sur des **comptes professionnels**, dont les conditions excluent généralement l'entraînement sur les données. Cette seule étape résout une large part de l'exposition, pour un coût d'abonnement modeste.

## 4. Former — dirigeants d'abord

L'ordre est contre-intuitif et déterminant.

- **Dirigeants en premier.** Une direction qui ne comprend pas les limites de la technologie prend de mauvaises décisions d'investissement, puis lit le premier résultat décevant comme un échec de la technologie plutôt que du cadrage. Objectif : pas en faire des experts, leur donner de quoi arbitrer — ce que l'IA fait mal, ce qu'un projet coûte en maintenance, comment se juge un résultat.
- **Équipes ensuite**, par niveau d'usage réel plutôt que par service ou ancienneté.
- **Référents enfin** : une personne par service, formée un cran au-dessus, qui absorbe les questions du quotidien. Sans ce relais, tout remonte au prestataire et l'adoption plafonne.

**Les 4 objections, et la réponse qui marche :**
| Objection | Réponse |
|-----------|---------|
| « L'IA va me remplacer » | Montrer le déplacement des tâches **dans** le poste, pas la suppression du poste |
| « Je n'ai pas le temps d'apprendre » | Démontrer le gain sur **sa** tâche à elle, chronomètre en main |
| « Les résultats ne sont pas fiables » | **Objection fondée.** Former à la vérification, ne pas nier le problème |
| « Je préfère ma méthode » | Période d'essai bornée, avec droit de revenir en arrière |

La troisième est celle qui décide de la crédibilité : les modèles produisent des erreurs plausibles. Une formation qui ne l'admet pas est démolie au premier incident.

**Traçabilité** : cette formation répond à une obligation légale (art. 4) — dates, contenus, présences, évaluation de fin.

## 5. Premiers gains — un seul processus à la fois

Prendre le premier processus du quadrant « effort faible / impact fort ». **Un seul.**

1. Mesure de référence (déjà faite en phase diagnostic)
2. Déploiement restreint : un service, deux semaines
3. Mesure après, sur les mêmes 5 indicateurs
4. Écart documenté, **en euros**
5. Décision : étendre, ajuster, ou **arrêter**

L'étape 5 doit inclure « arrêter ». Si cette option n'existe pas, les quatre premières ne servent à rien — on étendra de toute façon.

**Privilégier l'existant**, par coût de possession croissant :
| Niveau | Quand | Coût réel |
|--------|-------|-----------|
| SaaS configuré | Le besoin est standard | Abonnement, maintenance faible |
| Automatisation no-code | Enchaînement d'outils existants | Abonnement + fragilité aux changements d'API |
| Développement sur mesure | Besoin spécifique, volume qui le justifie | Développement + maintenance permanente |

Ne passer au niveau suivant qu'après avoir écarté le précédent **pour une raison écrite**.

## 6. Sur-mesure — seulement après une preuve

- **Reformuler la demande en problème.** Une demande arrive toujours en solution (« on veut un chatbot »). Remonter d'un cran : quel problème, quel coût actuel, que se passe-t-il si on ne fait rien.
- **Un critère de succès chiffré et daté.** « Améliorer le support » → « −30 % de tickets niveau 1 en 3 mois, sur le volume mensuel ». « Qualifier les leads » → « 80 % des leads qualifiés en < 5 min, ≤ 5 % de faux positifs ». Écrire aussi **le seuil d'échec** : à partir de quel résultat on arrête. Inconfortable à l'engagement, protecteur pour les deux parties à la fin.
- **Le périmètre dans les deux sens.** Ce qui est traité, ce qui ne l'est pas, avec le chemin de repli. Un système qui couvre 85 % des cas est un succès si les 15 % restants ont une sortie définie ; c'est un litige s'ils n'ont jamais été évoqués. Toujours prévoir l'escalade vers un humain.
- **Évaluer avant de construire** — le point le plus négligé. Un système à base de LLM n'est pas déterministe, il ne se teste pas comme du logiciel classique : constituer 30 à 50 cas **réels** issus de l'activité, inclure les cas limites (ambiguïté, données manquantes, hors-sujet, tentative de détournement), définir ce qu'est une bonne réponse pour chacun, rejouer la mesure à chaque itération. Sans jeu d'évaluation, « ça marche » signifie « j'ai essayé trois fois et j'étais content » — ça ne survit pas à la production.
- **Livrer par incréments.** Quatre livraisons vérifiables se pilotent ; la même charge en une livraison de trois mois, non.

**Types de solutions et outillage** (repères, pas prescriptions) : agents conversationnels (support 24/7, qualification de leads, onboarding) ; automatisations avancées (rapports, prospection multicanale, traitement de documents, base clients) ; applications internes (dashboards, générateurs de propositions commerciales). Côté outils : SaaS génériques d'abord, puis no-code (Make, Zapier, n8n), puis développement. Les outils changent vite — **ne jamais vendre une liste d'outils, vendre des critères** (section 8).

**Ce que « sur-mesure » veut dire concrètement**, au niveau développement : pas un agent générique reconfiguré, mais une configuration propre à l'entreprise cliente — persona (ton, limites de ce que l'agent peut dire), compétences (les tâches qu'il sait vraiment faire, pas plus), scripts et intégrations (connexion aux outils déjà en place, pas un nouvel endroit où aller). À ce niveau, à côté de n8n : des frameworks d'agents auto-hébergés comme **Hermes Agent** (Nous Research) ou **OpenClaw** permettent de construire un agent qui tourne chez le client plutôt que chez un tiers — intéressant sur la réversibilité (section 7), mais tous deux sortis ou renommés en 2026 : appliquer le critère Maturité (section 8) avec une vigilance renforcée avant de les proposer sur une mission facturée.

## 7. Piloter — 4 indicateurs, pas quinze

| Indicateur | Mesure |
|-----------|--------|
| Temps réellement économisé | Écart avant/après, par processus |
| Taux de reprise | Part des sorties nécessitant correction humaine |
| Adoption réelle | Usage effectif, pas comptes créés |
| Incidents | Erreurs ayant eu une conséquence |

Le troisième distingue l'usage de la licence. Le quatrième est celui que personne ne suit et qui détermine si le dispositif tient.

**Réversibilité — trois questions avant chaque engagement, à réexaminer chaque année :** où sont les données et comment les récupère-t-on ? que se passe-t-il si le fournisseur change ses conditions ou disparaît ? le processus fonctionne-t-il encore si l'outil est coupé demain ?

## 8. Choisir un outil — critères, pas liste

Une liste d'outils vieillit en quelques mois ; ces critères non.
- **Données** — où a lieu le traitement, transferts hors UE, entraînement autorisé par le contrat, durée de conservation et procédure de suppression
- **Réversibilité** — export dans un format exploitable, ce qui reste si on part
- **Intégration** — s'insère dans les outils déjà utilisés, ou impose un nouvel endroit où aller ? Un outil qui exige de changer d'habitude sans gain immédiat ne sera pas adopté
- **Coût réel** — par utilisateur, à l'usage, configuration initiale, entretien annuel
- **Maturité** — depuis quand l'éditeur existe, qui le finance. Une part significative des outils IA de 2024 n'existe plus. Exemple concret à surveiller : Hermes Agent et OpenClaw (cités en section 6) sont réels et fonctionnels, mais sortis/renommés en 2026 — aucun historique de continuité éprouvé. Les mentionner à un client, oui ; les recommander sans réserve sur ce critère précis, non
- **Conformité** — l'éditeur documente-t-il sa position AI Act et fournit-il de quoi remplir vos obligations ?

## 9. Modes d'échec (ils se répètent)

1. Commencer par le projet le plus visible — presque toujours le plus difficile ; l'échec initial ferme le budget durablement
2. Ne pas mesurer avant — le gain devient déclaratif, et personne ne renouvelle un budget sur du déclaratif
3. Automatiser un processus instable — l'automatisation industrialise les exceptions
4. Former les équipes sans former la direction — les arbitrages restent mauvais
5. Développer avant d'avoir prouvé — le poste de dépense le plus fréquemment perdu
6. Oublier le coût de maintenance — les API changent, les modèles évoluent, les cas d'usage dérivent. Budget d'entretien annuel dès le premier jour
7. Ignorer l'usage existant — encadrer les nouveaux outils pendant que les anciens usages continuent, c'est traiter la mauvaise exposition

## 10. Le classeur d'évaluation (CHECKLISTIA)

Outil de conduite de mission : un classeur de portes de phase. Structure — *Tableau de bord* (calculé) · *Paramètres* (seuils) · *Processus* (mesure et priorisation) · *1. Diagnostic* · *2. Formation* · *3. Sur-mesure* · *Points bloquants*.

**Principe de fonctionnement :** chaque phase est une liste de points de contrôle, dont certains sont **rédhibitoires**. On ne passe à la phase suivante que si le taux de complétion dépasse le seuil (80 % par défaut) **et** qu'aucun rédhibitoire n'est ouvert. Statut de porte : passage autorisé / à compléter / arrêt.

**Seuils par défaut :** impact fort > 10 000 €/an · effort faible < 20 jours pondérés · taux d'exceptions max 30 % · coefficient d'accompagnement du changement 1,0 (on double l'effort technique) · 52 semaines/an (46 pour une estimation prudente) · coût horaire chargé 45 €.

**Rédhibitoires à connaître par cœur** — phase 1 : inventaire des systèmes d'IA existants, classification des données, 5 mesures de référence relevées, critère d'arrêt défini. Phase 2 : les équipes savent vérifier une sortie et savent quelles données ne sortent pas ; inventaire à jour ; programme de formation par rôle ; traçabilité en place ; dirigeants formés **avant** les équipes ; **au moins un gain mesuré en euros sur outil existant**. Phase 3 : gain déjà mesuré ; SaaS puis no-code écartés par écrit ; seuil d'échec accepté par écrit ; chemin de repli humain ; jeu de 30-50 cas réels ; coût de maintenance annoncé comme engagement pluriannuel.

**Usage BOS :** si l'entrepreneur vend de l'intégration IA, ce classeur *est* une grande partie du livrable de mission — BOS peut le remplir avec lui à partir des données du client, et il justifie à lui seul un diagnostic facturé.

---

## Les 3 règles qui résument tout

1. **Mesurer avant de changer.** Sans référence, aucun gain n'est démontrable.
2. **N'annoncer aucun chiffre qu'on n'a pas mesuré soi-même.** Les pourcentages qui circulent n'ont ni périmètre ni méthode.
3. **Toujours garder un critère d'arrêt.** Un dispositif qu'on ne peut pas arrêter n'est pas un projet, c'est un engagement.
