# Prompts Perplexity — message mining complet, sources bloquées ici
*17/08/2026 — à exécuter depuis un navigateur normal. Trois prompts, dans l'ordre.*

## Pourquoi trois prompts et pas un

Un prompt unique couvrant 15 sources produira une synthèse superficielle et **des pourcentages inventés**. Le comptage par occurrence est précisément ce qu'un modèle fabrique quand il ne peut pas lire le volume réel. Les prompts ci-dessous sont construits contre ce risque : dénominateur exigé **avant** tout pourcentage, verbatim obligatoire, interdiction explicite d'extrapoler.

**Ordre :** Prompt A une fois par concurrent (7 fois) → Prompt B une fois → Prompt C en dernier, en lui collant les sorties de A et B.

---

## PROMPT A — À exécuter 7 fois, une par concurrent

> Remplacer `[MARQUE]` et `[URL]` à chaque passage. Liste en bas de document.

```
Tu es analyste en recherche client. Ta mission : extraire les VERBATIMS EXACTS des avis
clients de la marque [MARQUE] et les compter par thème.

SOURCE À LIRE : [URL]
Lis aussi les pages suivantes du même avis si elles existent (page 2, 3, 4...).

RÈGLES ABSOLUES — leur non-respect rend ta réponse inutilisable :
1. Tu ne cites QUE des phrases réellement présentes dans les avis, mot pour mot, en français.
   Aucune reformulation, aucune paraphrase, aucun résumé présenté comme une citation.
2. AVANT tout pourcentage, tu indiques le DÉNOMINATEUR : "J'ai lu N avis sur M au total."
   Si tu ne peux pas lire les avis, tu écris "AVIS NON ACCESSIBLES" et tu t'arrêtes.
   Ne devine jamais un chiffre.
3. Tu n'extrapoles pas. Si tu as lu 40 avis sur 300, tes pourcentages portent sur 40,
   et tu l'écris explicitement.
4. Chaque citation est suivie de : (note attribuée /5 — date de l'avis).
5. Si un thème n'apparaît pas, tu écris "0 occurrence". Tu n'inventes pas de thème absent.

CE QUE TU PRODUIS :

### Volume lu
- Nombre d'avis lus : X sur Y au total
- Répartition des notes : 5★ = ..., 4★ = ..., 3★ = ..., 2★ = ..., 1★ = ...

### Comptage par thème
Pour chacun des thèmes ci-dessous, donne le nombre d'occurrences sur les X avis lus,
puis 2 à 4 citations exactes :

- TAILLE (bonnet trop petit/grand, écart avec la taille habituelle, guide de taille faux)
- MAINTIEN (ne tient pas, s'affaisse, remonte, bretelles qui glissent)
- CONFORT / DOULEUR (marques rouges, compression, irritation, oubli du vêtement)
- QUALITÉ MATIÈRE (tissu, coutures, tenue au lavage, durabilité)
- LIVRAISON (délais, origine du colis, suivi)
- RETOUR / REMBOURSEMENT (délais, frais déduits, refus, conditions)
- SERVICE CLIENT (réactivité, absence de réponse, ton)
- PRIX / RAPPORT QUALITÉ-PRIX

### Verbatims les plus violents
Les 5 citations négatives les plus fortes émotionnellement, mot pour mot.

### Verbatims les plus enthousiastes
Les 5 citations positives les plus fortes, mot pour mot. Je veux les mots exacts
qu'emploient les clientes satisfaites pour décrire ce qui a changé pour elles.

### Vocabulaire récurrent
Liste les mots et expressions qui reviennent le plus souvent dans les avis, avec leur
nombre d'occurrences. Exemple attendu : "confortable (12)", "je l'oublie (5)".
```

---

## PROMPT B — Une seule fois, pour les forums et le vécu

```
Tu es analyste en recherche client. Ta mission : collecter les VERBATIMS EXACTS de femmes
françaises parlant de leur inconfort avec les soutiens-gorge, et de leur abandon éventuel.

SOURCES À EXPLORER (lis-les réellement, ne te contente pas de les citer) :
- Reddit : r/france, r/AskFrance, r/Feminisme, r/rance — recherche "soutien-gorge",
  "no bra", "sans armature", "brassière"
- Forums : Doctissimo, aufeminin, jeuxvideo.com (forum blabla), Madmoizelle
- Blogs : minastorm.com, lingerie-claire.fr, celisette.fr, naturafeel.fr, echosverts.com,
  ohlesfemmes.com, leculdepoule.co, 88boutique.com, twinswomen.fr
- Commentaires sous les articles de ces blogs (souvent plus riches que les articles)
- TikTok et Instagram : commentaires sous les vidéos "no bra" et "soutien-gorge confortable"

RÈGLES ABSOLUES :
1. Citations mot pour mot, en français, jamais reformulées.
2. Chaque citation porte sa source (nom du site ou du subreddit) et sa date si disponible.
3. Si tu ne peux pas accéder à une source, tu écris "NON ACCESSIBLE" pour celle-ci.
   Tu n'inventes aucun témoignage.
4. Tu ne comptes que ce que tu as lu, et tu indiques combien de témoignages tu as lus.

CE QUE TU PRODUIS :

### Le moment de bascule
Les citations exactes où une femme décrit LE moment précis où elle a décidé que ça
suffisait. Je cherche des scènes concrètes, pas des généralités.

### Le geste du soir
Toutes les citations décrivant le fait de retirer son soutien-gorge en rentrant.
Mots exacts.

### Ce qu'elles ont essayé avant
Citations sur les produits testés et pourquoi ils ont échoué.

### La croyance de normalité
Citations où une femme dit avoir cru pendant des années que la douleur était normale,
avant de découvrir que non. C'est le thème le plus important de cette recherche.

### Celles qui ont abandonné
Citations de femmes qui ne portent plus de soutien-gorge du tout. Pourquoi ont-elles
arrêté ? Qu'est-ce qui les ferait revenir ? Mots exacts.

### Vocabulaire
Les 30 mots et expressions les plus fréquents employés pour décrire l'inconfort,
avec le nombre d'occurrences relevées.
```

---

## PROMPT C — En dernier, avec les sorties de A et B collées

```
Voici les données brutes de message mining que j'ai collectées sur le marché français
du soutien-gorge sans armature. [COLLER ICI TOUTES LES SORTIES DES PROMPTS A ET B]

Ta mission : les analyser selon la formule MECLabs, sans rien inventer.

RÈGLES :
1. Tu ne travailles QUE sur les données ci-dessus. Tu n'ajoutes aucune donnée externe.
2. Si une conclusion n'est pas soutenue par au moins 3 verbatims, tu la marques
   "SIGNAL FAIBLE".
3. Tu conserves les citations exactes dans ton analyse.

CE QUE TU PRODUIS :

### 1. Classement MECLabs
Range chaque thème dans un des 4 leviers, avec ses verbatims et son comptage :
- MOTIVATION : quels problèmes, quels désirs, que doit-elle croire pour acheter ?
- VALEUR PERÇUE : attrait, crédibilité, clarté de l'offre
- FRICTION : ce qui rend l'achat pénible
- ANXIÉTÉ : les objections avant l'achat, et d'où elles viennent

### 2. Classement des douleurs par fréquence
Tableau : douleur / nombre d'occurrences / % du corpus lu / citation représentative.
Trié par fréquence décroissante.

### 3. Les 3 promesses que le marché ne tient pas
Les défauts qui reviennent chez TOUS les concurrents analysés, avec les preuves.

### 4. Propositions de valeur candidates
Écris 5 propositions de valeur construites UNIQUEMENT avec les mots exacts relevés
dans les verbatims. Pas de vocabulaire marketing inventé. Chaque proposition doit
citer les verbatims dont elle est tirée.

### 5. Ce qui manque
Quels angles morts subsistent dans cette recherche ? Que faudrait-il aller chercher
et où ?
```

---

## Les 7 URL du Prompt A

| # | Marque | URL |
|---|---|---|
| 1 | **Celyssia** — prioritaire, concurrent viable | `fr.trustpilot.com/review/celyssia.com` |
| 2 | Leishape — contre-exemple, marque en déclin | `fr.trustpilot.com/review/leishape.com` |
| 3 | Mon Soutien Gorge | `fr-be.trustpilot.com/review/mon-soutien-gorge.com` |
| 4 | Maison Soutiens Gorge | `fr.trustpilot.com/review/maison-soutiens-gorge.com` |
| 5 | Sans Complexe | `fr.trustpilot.com/review/sanscomplexe.com` |
| 6 | Naked Underwear | `fr.trustpilot.com/review/naked-underwear.com` |
| 7 | Yade Paris | `fr.trustpilot.com/review/yade-paris.fr` |

**Bonus si le temps le permet** — les acteurs installés, pour comparer les attentes d'un segment premium : Ysé, Nénés Paris, Playtex, Darjeeling, RougeGorge, Blancheporte, Daxon, ToutesLesPoitrines.

**Amazon.fr** — à traiter avec le Prompt A en remplaçant l'URL par une recherche `amazon.fr` sur « soutien-gorge sans armature ». Prendre les 3 produits les mieux vendus et lire **les avis 1 et 2 étoiles en priorité** : c'est là que se trouvent les mots les plus utiles.

---

## Ce qu'il faut vérifier en recevant les réponses

Avant d'intégrer quoi que ce soit :

1. **Le dénominateur est-il donné ?** Pas de dénominateur = pourcentages inventés, à jeter.
2. **Les citations sonnent-elles comme du français parlé ?** Une citation trop propre, trop bien construite, est probablement fabriquée. Les vrais avis ont des fautes, des majuscules erratiques, des phrases qui s'arrêtent.
3. **Recouper deux ou trois citations** en les cherchant directement sur la page source. Si elles n'y sont pas, tout le lot est suspect.
4. **Les blogs « avis » sont souvent des sites affiliés** (glowchicparis, glowupbyparis, amazing-beauty, allure-mag, mamandeteste) : ils touchent une commission sur les ventes Celyssia. Leurs « avis » ne sont pas neutres — utiles pour repérer les objections traitées, pas comme preuve de satisfaction.

Les sorties se rangent ensuite dans `Output/Message_Mining_Sans_Armature_2026-08-17.md`, qui contient déjà le cadre chiffré IFOP et le relevé thématique. Ce sont les mots exacts et le comptage qui manquent — c'est exactement ce que ces trois prompts vont chercher.
