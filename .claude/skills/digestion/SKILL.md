# Skill: Digestion

Gérer le flux actuel quand le goulot est **opérations / qualité / rétention** — pas l'acquisition (Chase), pas le mindset fondateur (Mindset). Déclenché quand `diagnosis` identifie un goulot de type Digestion en phase Scale.

Couvre : recrutement complet (People), systématisation (Process), et boucle qualité/rétention (Product Quality).

## Objectif

1. **Diagnostiquer** le sous-problème : **People**, **Process**, ou **Product Quality** (rétention / satisfaction).
2. **Exécuter** la phase correspondante : recrutement complet (si People), systématisation (si Process), boucle satisfaction (si Product Quality).
3. **Sauvegarder** les livrables dans `Output/` et **mettre à jour** `Core/Actions.md`, `Core/Diagnosis.md`.
4. **Ne pas** scaler l'acquisition sur un produit qui fuit en bas de l'entonnoir.

## Croyances

- **Opérations = Recrutement + Process.** Si ça coince, c'est forcément l'un des deux (ou les deux).
- **Mauvaise personne vs mauvais process.** Tu expliques, reformules, coaches → toujours pas bon = **mauvaise personne**. **Trois** personnes échouent successivement = **mauvais process** (système / brief / management / fondateur).
- **Quand il y a doute, la réponse est non.** Après test / entretiens, un doute persistant = on ne prend pas. Mieux vaut continuer à chercher que regretter un mauvais choix pendant 6 mois.
- **En dessous de 4/5 de satisfaction, rien ne scale.** Le marketing remplit en haut, mais ça fuit en bas.
- **Les bons attirent les bons.** Un premier recrutement solide élève le niveau de toute l'équipe. Baisser la barre parce que c'est dur de trouver = commencer à perdre.
- **Définir le succès avant de chercher.** « Un bon marketing » n'est pas un brief ; « 50 leads qualifiés/semaine par cold email sous 30 jours » l'est. La scorecard précède le sourcing.
- **Une mauvaise embauche coûte beaucoup plus que son salaire.** Temps de management, erreurs, moral de l'équipe, opportunités ratées — le coût réel est souvent 10-20× le salaire mensuel. Chaque étape du process produit un document.
- **Embaucher le goulot, pas la corvée.** Le premier recrutement doit lever la plus grosse contrainte, pas seulement la tâche que le fondateur déteste.
- **Tester petit avant d'engager gros.** VA 10h/semaine avant CDI ; mission freelance avant contrat long ; test rémunéré avant signature.
- **Ne jamais embaucher pour des compétences qu'on ne sait pas juger.** Soit monter en compétence minimale, soit recruter un profil senior autonome.
- **Les clients décrivent des symptômes, pas des causes.** Le client dit « l'interface est pas claire », le vrai besoin c'est « gagner du temps ». Résoudre le besoin profond.
- **Une décision qui n'existe que dans la tête du fondateur n'est plus une décision — c'est une rumeur.** Le symptôme le plus courant du passage à l'échelle : l'informel, qui était une technologie formidable à 5 personnes (tout le monde sait tout, une question se règle en traversant la pièce), devient à 30 ou 50 le mécanisme qui bloque tout. Un manager tranche le mardi, quelqu'un contourne et obtient une autre réponse le mercredi, plus personne ne sait laquelle vaut le jeudi.
  > **Le diagnostic à ne pas rater.** Le fondateur dit alors « personne n'est autonome ici » et croit avoir un problème de recrutement, de management ou de culture. Il a un problème d'**architecture décisionnelle** : il a gardé celle d'une petite structure dans une entreprise qui ne l'est plus. Les équipes ne manquent pas d'autonomie — elles sont devenues parfaitement rationnelles dans un système qui **récompense l'attente**, puisqu'une décision prise sans le fondateur peut être annulée le lendemain. Tant que le système récompense l'attente, recruter des gens plus autonomes ne change rien : ils apprendront la même chose en trois semaines.
  >
  > **Le traitement :** écrire qui décide quoi, et à quel niveau d'engagement une décision remonte. Accepter qu'une décision soit prise autrement qu'on l'aurait prise soi-même est le vrai coût, et c'est le plus dur à payer. Le job du fondateur cesse d'être « prendre les bonnes décisions » et devient « construire une structure capable d'en prendre de bonnes quand il n'est pas dans la pièce ». Sans ça, on n'a pas fait grandir l'entreprise, on a seulement agrandi la pièce.

## Process

### Phase 1 — Diagnostic digestion : quel sous-problème ?

| Sous-problème | Signes | Routage interne |
|---------------|--------|-----------------|
| **People** | Goulot délégation, besoin de bras, surcharge fondateur | → Phase 2 (Recrutement) |
| **Process** | Chaos, pas de SOPs, tout manuel, erreurs répétées | → Phase 3 (Systématisation) |
| **Product Quality** | Satisfaction < 4/5, churn, plaintes, livraison fragile | → Phase 4 (Qualité / Rétention) |

**Ordre de recrutement recommandé** (quand l'entrepreneur scale au-delà de lui-même) :

1. **Bras droit / COO** — opérations quotidiennes ; libère le fondateur pour stratégie et croissance.
2. **Responsable du domaine goulot** — acquisition → marketing ; produit → PM ; etc.
3. **Exécutants** — sous les responsables.

**Piège à nommer :** embaucher des exécutants avant d'avoir un manager → le fondateur manage cinq personnes et n'a plus de temps stratégique.

### Phase 2 — Recrutement

#### 2.1 — Besoins et cadrage (~5 min)

**Questions** (sauter ce qui est déjà dans le contexte) :

1. « C'est quoi le problème que cette personne va résoudre ? En une phrase. »
2. « Qu'est-ce que tu fais toi-même aujourd'hui que cette personne devrait faire ? »
3. « Profil : VA, freelance, temps partiel, temps plein ? »
4. « Budget mensuel pour ce poste ? »
5. « Tu as déjà embauché ? Si oui, qu'est-ce qui a marché / pas marché ? »

**Contrôles BOS :**

- C'est le **bon** recrutement ? (Comparer à `Diagnosis.md` — la délégation est-elle le vrai goulot ?)
- L'entrepreneur est-il prêt à **manager** ? (Sinon réduire le scope — VA d'abord.)
- Le budget est-il **réaliste** pour la qualité visée ?

Si le recrutement ne colle pas au diagnostic : « Avant d'embaucher pour [X], ton vrai bottleneck c'est peut-être [Y]. T'es sûr que c'est la bonne priorité ? »

#### 2.2 — Scorecard

BOS produit le document ; validation entrepreneur avant sourcing.

```markdown
# Scorecard : [Titre du poste]

## Mission
[Une phrase : ce que cette personne existe pour accomplir]

## Résultats attendus (3-5)
1. [Résultat mesurable] — dans les [délai]
2. [Résultat mesurable] — dans les [délai]
3. [Résultat mesurable] — dans les [délai]

## Compétences requises
- [Compétence technique 1]
- [Compétence technique 2]
- [Qualité humaine 1]
- [Qualité humaine 2]

## Red Flags (ne PAS embaucher si)
- [Dealbreaker 1]
- [Dealbreaker 2]

## Conditions
- Type : [VA / Freelance / Temps partiel / Temps plein]
- Heures : [X]h/semaine
- Rémunération : [fourchette]
- Durée : [période test → engagement]
- Remote / sur place
```

#### 2.3 — Annonce

1. **Accroche** — pourquoi ce rôle est intéressant (pas « entreprise dynamique »).
2. **Mission** — ce qu'ils font vraiment (concret).
3. **Succès** — résultats de la scorecard, simplifiés.
4. **Indispensables** — 3-5 compétences non négociables.
5. **Bonus** — 2-3 compétences appréciées.
6. **Le deal** — rémunération, horaires, conditions. Transparence.
7. **Candidature** — **question filtre** anti-masse. Ex. : « Envoie un Loom de 2 min sur comment tu résoudrais [problème précis]. »

#### 2.4 — Stratégie de sourcing

| Type | Plateformes | Approche |
|------|-------------|----------|
| VA | Belay, OnlineJobs.ph, Upwork | Post + outreach direct ~10 profils |
| Freelance spécialisé | Malt, Upwork, LinkedIn, communautés niche | Post + DM meilleurs profils |
| Employé temps plein | LinkedIn, Welcome to the Jungle, réseau | Post + chasse active |
| Freelance créatif | Dribbble, Behance, 99designs, reco | Portfolio + test |

Pour chaque plateforme : instructions de post/recherche, nombre de candidats cibles, calendrier. **Templates d'outreach :** 2-3 messages personnalisés que l'entrepreneur peut envoyer.

**Ne jamais s'en tenir à l'annonce.** Les meilleures recrues viennent rarement d'une candidature spontanée — elles viennent d'une recommandation, d'un message direct, ou de quelqu'un qui suivait le projet depuis des mois. À activer en parallèle systématiquement : post sur le compte personnel du fondateur, communautés du secteur, recommandations internes, approche directe de profils déjà en poste, et **la question aux gens de confiance : « Qui est la meilleure personne que tu connaisses sur ce sujet ? »**

**Tenir une liste permanente de profils intéressants**, alimentée hors période de recrutement. Recruter uniquement dans l'urgence, c'est choisir dans un vivier qu'on n'a pas construit.

**L'attractivité se construit avant le poste** — voir `Knowledge/Recruiting_Playbook.md`. Un candidat qui découvre la boîte par une annonce froide ne ressent rien ; un candidat qui suit le fondateur depuis six mois arrive à moitié convaincu. Si l'entrepreneur produit déjà du contenu, l'orienter pour qu'il documente aussi ce qu'il construit (avancées, coulisses, décisions, équipe) : ça sert l'acquisition **et** le vivier.

#### 2.5 — Entretiens structurés

**Tour 1 — Screening (15 min, async ou call)** — Filtrer les mauvais fit ; 3-4 questions de base ; dispo/conditions ; une question culture.

**Tour 2 — Deep dive (30-45 min, call)** — Scorecard : pour chaque résultat attendu, « Donne-moi un exemple concret où tu as [résultat similaire] — contexte, actions, résultat ? » ; pour chaque compétence, scénario ; « Qu'est-ce qui n'a pas marché avant ? » ; « Pourquoi nous / ce projet ? »

**Tour 3 — Test rémunéré** — Tâche réaliste (2-4h), livrables et deadline clairs, **payé**, évaluation vs scorecard. BOS rédige le test adapté au rôle. Le livrable compte, **la structure du raisonnement compte plus** : est-ce que la personne hiérarchise, simplifie, et apporte ce que l'interne n'avait pas ?

**Tour 4 (postes clés)** — Faire rencontrer un second interlocuteur (associé, manager, personne de confiance). Le fondateur a envie que ça marche ; un deuxième regard corrige ce biais.

**Deux règles de fond :**
- **Ne pas vendre que du rêve.** Exposer la pression, le niveau d'exigence, la vitesse attendue. Le but n'est pas de convaincre tout le monde — c'est de faire fuir vite ceux qui ne colleront pas.
- **La question de clôture, après chaque échange : « Est-ce que cette personne va retirer des problèmes de mon quotidien, ou en ajouter ? »** C'est souvent le meilleur filtre disponible.

#### 2.6 — Matrice d'évaluation

| Critère | Poids | Candidat A | B | C |
|---------|-------|------------|---|---|
| Résultat 1 | 25% | /10 | /10 | /10 |
| Résultat 2 | 25% | /10 | /10 | /10 |
| Compétence clé | 20% | /10 | /10 | /10 |
| Test | 20% | /10 | /10 | /10 |
| Culture fit | 10% | /10 | /10 | /10 |
| **TOTAL** | | **/10** | | |

**Règle :** si le meilleur candidat est **sous 7/10**, ne pas embaucher — continuer la recherche.

#### 2.7 — Onboarding 30 jours

- **Semaine 1** — Orientation + premier livrable : accès outils, première tâche (petit win), check-in quotidien (15 min).
- **Semaines 2-3** — Montée en charge : responsabilité croissante, boucle feedback, 2×/semaine check-ins.
- **Semaine 4** — Test d'autonomie sur le cœur du poste ; check-in hebdo.
- **Décision J+30** — Garder ou séparer vite si la trajectoire n'est pas bonne. Un doute persistant = on ne garde pas. Mieux une erreur rapide qu'une lente.

### Phase 3 — Systématisation (Process)

- **Audit** — Quels process existent ? Lesquels sont manuels ? Lesquels **bloquent** livraison, qualité, ou vente ?
- **SOPs** — Documenter les process **critiques** : livraison, onboarding client, vente (minimum viable : étapes, responsable, outil, critère de done).
- **Automatisation** — Identifier ce qui peut être automatisé (outils, IA, workflows) sans « automatiser le chaos ».
- **Productisation** — Transformer le sur-mesure en **répétable** : packages clairs, limites de scope, 1-to-many quand possible.

**Rappel :** Opérations = recrutement + process — souvent les deux en séquence (scorecard puis SOPs, ou l'inverse selon le goulot).

### Phase 4 — Qualité produit / Rétention

**Cible : note ≥ 4/5 de satisfaction client.** En dessous, l'acquisition = remplir un seau percé.

**Process :**

1. Feedback structuré à **chaque** client : note 1-5 + « qu'est-ce qu'on pourrait améliorer ? »
2. Lister **tous** les retours.
3. Identifier les **patterns** (ce qui revient le plus).
4. Distinguer le **besoin profond** vs le **symptôme exprimé** — le client dit « interface pas claire », le vrai besoin c'est « gagner du temps ».
5. Prioriser par **impact satisfaction** (pas par bruit social).
6. Implémenter **1-3** changements à la fois.
7. Redemander une **note** après les changements.
8. Répéter jusqu'à **≥ 4/5** stable.

*« Un marketing impeccable sur un produit médiocre, c'est le meilleur moyen de tuer ton business. Les clients mécontents parlent — et ils parlent plus fort que ta pub. »*

### Phase 5 — Sauvegarder et exécuter

1. Si **recrutement** : sauvegarder le package complet dans **`Output/Hire_[Poste]_[date].md`** — scorecard, annonce, sourcing + outreach, entretiens + test, matrice, onboarding 30j.
2. **Mettre à jour** `Core/Actions.md` — publier, sourcer, entretiens, décision ; ou SOPs ; ou changements qualité.
3. **Mettre à jour** `Core/Diagnosis.md` — goulot Digestion ; People / Process / Quality ; prochain risque.
4. **Append** `Core/Journal.md` si décision importante.
5. **Lancer tout de suite** la prochaine action concrète : « On publie l'annonce maintenant ? » / « On documente la SOP #1 maintenant ? »

## Output

| Fichier | Quand | Contenu |
|---------|--------|---------|
| `Output/Hire_[Poste]_[date].md` | Recrutement (Phase 2) | Package complet : scorecard, annonce, sourcing, entretiens, test, matrice, onboarding |
| `Core/Diagnosis.md` | Toujours | Sous-type Digestion ; séquence People / Process / Quality |
| `Core/Actions.md` | Toujours | Prochaines étapes ; tâches en **bold** |
| `Core/Journal.md` | Si utile | Embauche, décision qualité, mise en place SOP |

## Garde-fous

- **Ne JAMAIS rédiger une annonce sans scorecard.** La scorecard définit le succès — sans elle, on embauche au feeling.
- **Ne JAMAIS sauter le test rémunéré.** Entretien seul ≠ preuve de compétence. Le test est systématique.
- **Ne JAMAIS embaucher pour « agrandir l'équipe » sans ROI clair.** Lier le poste à un résultat chiffré dans la scorecard.
- **Ne JAMAIS embaucher amis/famille sans le même process.** Les relations ne dispensent pas de la rigueur.
- **Ne JAMAIS sous-payer en attendant du premium.** Budget réaliste ou scope réduit.
- **Ne JAMAIS sur-recruter.** Un recrutement à la fois ; stabiliser avant le suivant.
- **Ne JAMAIS garder quelqu'un par pitié ou par peur de recommencer.** Un doute persistant = on ne garde pas. Le coût de garder un profil médiocre dépasse toujours le coût de recommencer.
- **Ne JAMAIS accuser la personne avant d'auditer le process.** Trois échecs d'affilée = soupçonner le système, pas les gens.
- **Ne JAMAIS scaler l'acquisition sur un produit sous 4/5 de satisfaction.** Boucle qualité d'abord.
- **Ne JAMAIS embaucher des exécutants avant d'avoir un manager** quand le scale l'exige. Voir l'ordre de recrutement recommandé.
