# Système de contenu Velune — auto-évolutif

**Statut (06/08/2026) :** système de base construit, zéro donnée réelle encore. Normal — les 3 premiers posts n'ont pas été publiés. Ne pas modifier le template sur une intuition avant d'avoir des résultats réels : voir `Core/Diagnosis.md` (problème n°3, root cause perfectionnisme/collecte).

## Ce que contient ce dossier

- `velune_brand.py` — le système de marque partagé (couleurs, polices, cartes, icône lune, en-tête). Toute nouvelle créative doit importer ce module plutôt que redéfinir son propre style, sinon la cohérence de marque se perd post après post.
- `logo.py` → `velune_logo.png` — photo de profil.
- `post_j1_debat.py`, `post_j2_avant_apres.py`, `post_j3_savais_tu.py` — les 3 formats déjà produits, chacun un exemple réutilisable pour le suivant du même type.

## La boucle d'auto-évolution

Le mécanisme n'est pas dans ce dossier — il est dans `Core/Journal_Creatives.md`, exactement comme pour les créatives publicitaires (`Knowledge/AI_Ecom_Ops_Stack.md`). Le principe est identique, juste appliqué à l'organique :

1. **Après chaque post**, loguer dans `Core/Journal_Creatives.md` : le format utilisé (débat / avant-après / savais-tu / nouveau format), le résultat réel (vues, commentaires, partages, saves — pas une impression), et un enseignement.
2. **Ne rien changer au template avant 5-10 posts.** Une seule créative qui rate ou qui cartonne est du bruit, pas un signal — le principe déjà posé pour les Ads Meta s'applique à l'identique ici.
3. **Une fois le pattern net** (ex. les formats à choix multiples génèrent 3x plus de commentaires que les formats stat), mettre à jour `velune_brand.py` et/ou créer un nouveau `post_jX_<format>.py` qui capitalise dessus — et le dire explicitement dans le journal, avec la donnée qui justifie le changement.
4. **Ce qui ne doit jamais déclencher un changement de template :** une impression, une comparaison avec un autre compte, une envie de nouveauté. Seule une donnée répétée compte.

BOS applique cette boucle de lui-même dès qu'il y a assez de lignes dans `Core/Journal_Creatives.md` — pas besoin de le redemander à chaque fois.
