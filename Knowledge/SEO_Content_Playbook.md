# SEO de contenu — Playbook

Méthode complète pour construire un canal d'acquisition SEO : de la compréhension du business jusqu'à la cadence de publication. Référence du skill `traffic` quand le canal retenu est le SEO.

*Distillé d'un thread de méthode publié par Jotaroo SEO (@JotaroSeo). Voir « Réserves » en fin de document pour les points à nuancer.*

**Pourquoi ce canal est un terrain BOS.** Le SEO de contenu est le canal où l'écart entre quelqu'un équipé d'une IA et quelqu'un qui travaille seul est le plus violent : la recherche de mots-clés, l'analyse de SERP, les plans d'articles, le champ lexical et la rédaction sont exactement ce que BOS produit vite et bien. La cadence recommandée (1 article/jour) est irréaliste en solo à la main — elle devient tenable avec BOS. C'est l'argument à donner à l'entrepreneur, explicitement.

---

## Le constat de départ

La plupart des gens croient que le SEO c'est : trouver des mots-clés → écrire un article → attendre. C'est pour ça que la plupart n'ont pas de résultats. Le SEO de contenu est **une architecture**, pas une série d'articles. Une fois le système en place, il génère du trafic en continu, sans budget média.

Horizon réaliste : **6 mois** pour voir apparaître les résultats, **12 mois** pour décoller, **24 mois** pour une machine autonome. Un entrepreneur qui a besoin de cash dans 60 jours ne doit pas choisir ce canal.

## Étape 0 — Comprendre le business avant de chercher un seul mot-clé

L'étape que presque personne ne fait, et où tout se joue.

1. **Quel est le produit ou service exact ?** Pas la catégorie, le produit. Pas « jeux vidéo » mais « console portable retrogaming ». Pas « cosmétiques » mais « crème anti-âge au rétinol 0,5 % ». Pas « formation en ligne » mais « formation Photoshop pour photographes professionnels ». Un site qui ne sait pas exactement ce qu'il vend ne peut pas produire de contenu qui convertit.
2. **Quel est le mot-clé principal ?** Le terme qui résume le mieux ce qu'on vend. Pas forcément celui de la page d'accueil : si la marque est forte et la home brandée, il sera porté par une page de collection, de service ou une page pilier. C'est l'étoile polaire — souvent difficile à ranker, mais tout le contenu gravite autour.
3. **Qui est le persona ?** Profil précis : qui, quel problème principal, **quel vocabulaire il utilise pour chercher sur Google**, phase de découverte ou phase d'achat, quelles objections. Ces réponses déterminent le ton, les sujets, les mots, la longueur.
4. **Quel est l'écosystème concurrentiel ?** Qui ranke déjà sur les mots-clés cibles ? Gros acteurs installés ou petits sites récents ? Quel type de contenu publient-ils ? Pourquoi eux dans le top 3 et pas nous ? On ne combat pas un site à autorité 80 comme un concurrent récent à 15, ni un spécialiste ultra-niche comme un généraliste (Amazon, eBay).

## Étape 0 bis — Valider la demande et benchmarker avant de s'engager

Avant d'écrire le premier mot, deux vérifications évitent de construire une stratégie sur un marché qui n'existe pas ou une bataille déjà perdue.

**Valider la tendance, pas seulement le volume actuel.** Un mot-clé au volume faible aujourd'hui peut être en pleine expansion — le signal précède souvent le volume : un produit qui explose sur les réseaux sociaux voit généralement son volume de recherche suivre avec un décalage. Sur un produit qui semble tendance, regarder la courbe sur quelques mois à un an ; sur un produit installé, remonter à deux ou trois ans pour la situer dans son cycle. Une courbe en expansion change le calcul de risque : viser un mot-clé qui va grossir coûte le même effort qu'un mot-clé stable, pour un potentiel très différent.

**Compléter par le volume et la longue traîne** sur un outil de recherche de mots-clés : le volume du terme principal, et surtout ses variantes proches — souvent moins recherchées individuellement mais nettement moins concurrentielles, donc plus rapides à ranker (`Étape 3`).

**Benchmarker la concurrence réelle sur la SERP** avant de s'engager, pas après :
- **Le nombre de concurrents sérieux.** Une SERP dominée par un seul acteur spécialisé laisse de la place ; une SERP avec dix sites optimisés de longue date n'en laisse pas.
- **Un site généraliste (Amazon, une grande marketplace) en top 3 est un bon signal**, pas un mauvais — ces sites laissent presque toujours des angles exploitables pour un site spécialisé qui traite mieux le sujet.
- **La qualité et le volume des liens entrants** de chaque concurrent, l'ancienneté de son nom de domaine, la présence ou non d'un domaine à correspondance exacte (voir ci-dessous).
- **Ce qui manque chez le premier.** Le contenu qu'il n'a pas traité, la structure qu'il n'a pas soignée, le rythme de publication qu'il a laissé tomber — un site qui a atteint la première place et cesse d'y travailler laisse une ouverture réelle. C'est souvent l'angle d'attaque le plus rentable : ne pas chercher à être différent, chercher à être plus complet sur ce que le premier a négligé.

**Sortie de cette étape :** un tableau de bord des forces et faiblesses du marché (demande, tendance, nombre de concurrents sérieux) croisé avec les forces et faiblesses du site — nombre de produits, présence de collections, état technique (Search Console configurée, sitemap déclaré, structure de titres). C'est ce tableau, pas une intuition, qui doit dicter si la stratégie vise d'abord la longue traîne (cas général) ou peut viser le mot-clé principal directement (uniquement si le catalogue est trop réduit pour alimenter une vraie stratégie de longue traîne).

## Étape 0 ter — L'autorité de domaine : ce qui se passe hors de la page

Tout ce qui précède (Étapes 1 à 8) construit le contenu. Mais Google évalue aussi la **crédibilité** du site indépendamment de chaque page — c'est l'autorité de domaine, et elle se construit par des signaux externes autant qu'internes.

**Le jus de lien (link juice), le mécanisme de base.** Chaque lien transmet une part de l'autorité de la page qui pointe vers une autre. Un lien **dofollow** transmet ce jus ; un lien **nofollow** ne le transmet pas (utilisé par exemple sur des commentaires ouverts, pour ne pas offrir gratuitement de l'autorité à n'importe qui). En interne, l'autorité de la page d'accueil se répartit entre les pages vers lesquelles elle pointe : plus il y a de liens sortants depuis une page, plus le jus transmis à chacun est dilué. **Conséquence pratique pour le maillage :** ne pas multiplier les liens sortants sans discernement sur les pages à forte autorité (accueil, pages piliers) — les réserver aux pages qui ont le plus besoin d'être poussées.

**Les backlinks (liens entrants externes)** sont le levier le plus direct pour augmenter l'autorité globale d'un domaine, mais leur qualité compte plus que leur nombre : un lien depuis un site pertinent et déjà crédible pèse largement plus qu'une dizaine de liens depuis des sites sans rapport ou de faible qualité.

**L'EMD (Exact Match Domain) — un nom de domaine qui contient le mot-clé principal.** Son impact a diminué depuis les années où il suffisait à lui seul à ranker, mais il reste un vrai avantage sur une niche peu concurrentielle : il indique instantanément à Google et au visiteur le sujet du site, et il est plus mémorable. Limites à connaître : deux mots-clés maximum dans le nom, en veillant à sa lisibilité et à sa longueur ; l'EMD ne remplace jamais un contenu de qualité et un maillage soigné — il amplifie une bonne stratégie, il n'en tient pas lieu seul.

### Construire de l'autorité sans backlinks (ou avant d'en avoir)

**Le point de départ à ne pas perdre : les backlinks amplifient une base solide, ils ne la remplacent pas.** Un site avec un contenu mal structuré et aucune stratégie sémantique ne sera pas sauvé par des backlinks — sinon ce serait trop simple. Construire la base (Étapes 1-8) d'abord ; le off-site vient ensuite renforcer, pas compenser.

**Le marketing 360 comme levier SEO indirect.** Google indexe directement des contenus sociaux dans ses résultats (posts LinkedIn, threads X, vidéos YouTube) — chaque publication sur un réseau est donc une surface de visibilité Google en plus, pas seulement une audience sociale. Trois mécanismes derrière ça, aucun ne dépendant d'un lien direct :
- **Le trafic de marque** — les recherches du nom de la marque directement sur Google. Signal fort qu'une audience connaît la marque et la cherche activement, qui se construit par la présence sur les réseaux et le bouche-à-oreille.
- **Les signaux comportementaux depuis la SERP** — le CTR (taux de clic sur le résultat plutôt que sur les concurrents) et le *dwell time* (temps passé sur la page avant de retourner aux résultats). Une notoriété construite ailleurs (réseaux, mentions) améliore mécaniquement ces deux métriques.
- **Les mentions de marque sans lien.** Google détecterait une marque citée sur le web même sans backlink pointant vers le site — une marque mentionnée régulièrement dans des articles, posts et forums est perçue comme une entité reconnue du secteur, un signal de confiance à part entière.

**Le contenu citable — la façon d'obtenir des backlinks sans en demander.** Études avec données propriétaires, statistiques originales sur la niche, guides exhaustifs qui deviennent la référence, outils gratuits utiles : ces formats donnent aux autres sites une raison spontanée de citer et de lier, sans prospection de liens. C'est le même principe que la préférence pour le format « Meilleurs X » en GEO ci-dessous — être la source qu'on a envie de citer plutôt que d'aller chercher la citation.

### Le GEO — être cité par ChatGPT, Claude, Gemini, pas seulement classé par Google

**⚠️ Chiffres cités tels que rapportés dans une étude Ahrefs relayée par un thread (source secondaire, non vérifiée directement par BOS) — à traiter comme des ordres de grandeur indicatifs, pas des constantes garanties.**

**Pourquoi ce n'est pas le même jeu que le SEO classique.** Les Aperçus IA de Google réduiraient déjà les clics vers le 1er résultat organique de ~58 % (contre ~34,5 % dix mois plus tôt) — la tendance s'accélère. Et 28,3 % des pages les plus citées par ChatGPT n'auraient **aucune** visibilité organique sur Google : être 1er sur Google ne garantit pas d'être cité par une IA, et inversement. Autre signal du même ordre : Google AI Mode et les Aperçus IA arriveraient aux mêmes conclusions ~86 % du temps, mais ne citeraient les mêmes sources que dans ~13,7 % des cas — optimiser pour l'un ne couvre pas l'autre.

**Être crawlé ne suffit pas.** Une IA peut récupérer une page sans jamais la citer (ChatGPT ne citerait qu'environ la moitié des pages qu'il récupère par requête) — elle sert parfois de simple contexte silencieux. La question à se poser n'est pas « suis-je crawlable ? » mais « pourquoi l'IA me citerait-elle plutôt que mon concurrent ? ».

**Le mécanisme de confiance des IA — proche de l'E-E-A-T, pas identique.** Là où Google peut déduire l'autorité de signaux externes (backlinks, mentions), une IA lit directement le contenu pour juger si l'auteur maîtrise vraiment son sujet. Les signaux qui comptent : la fréquence à laquelle le contenu est repris ailleurs, la cohérence thématique du site (autorité de niche, pas généraliste), la clarté structurelle (une IA doit pouvoir extraire une réponse facilement), et la diversité des formats de présence (texte, vidéo, plateformes tierces).

**Ce qui se traduit en actions concrètes, par ordre de priorité :**
1. **Autorité thématique réelle** — même principe que le topical SEO déjà posé plus haut (couvrir tous les angles d'un sujet, vocabulaire exact du domaine), mais c'est ici ce qui détermine si une IA associe le site au sujet dans la durée.
2. **Prioriser le format « Meilleurs X » / comparatif.** Ce format représenterait à lui seul 43,8 % des citations ChatGPT — de loin le format le plus cité, parce qu'il correspond structurellement à ce qu'une IA cherche pour répondre à une question comparative. Déclinaisons : « Les X meilleurs [produit] en [année] », « [Option A] vs [Option B] », « Top X de [catégorie] pour [persona] ».
3. **Densité factuelle plutôt que du texte qui « sonne bien ».** Une IA extrait des données précises et vérifiables, pas des généralités. « Le café éthiopien pousse entre 1700 et 2200 m, traitement lavé, notes florales, score cupping >84/100 SCA » est citable ; « le café éthiopien est réputé pour sa qualité » ne l'est pas. **Répondre directement en tête de chaque section (pas seulement dans l'intro de l'article)** — une IA extrait le H2 et les toutes premières phrases qui suivent ; une réponse enfouie au milieu d'un paragraphe de contexte fait passer l'IA à la source suivante.
4. **Présence YouTube.** Signal le plus corrélé à la visibilité de marque dans les IA selon l'étude citée (coefficient rapporté à 0,737) — au-dessus des backlinks et de l'autorité de domaine classiques. Vidéos propres, mais aussi être mentionné dans des reviews/tutoriels tiers sur la thématique.
5. **Fichier `llm.txt`** — équivalent du `robots.txt` pour les crawlers IA, à la racine du domaine (`monsite.fr/llm.txt`) : description de l'entreprise en une phrase, liste des pages les plus importantes, positionnement thématique, sources de données. Impact non documenté de façon certaine, mais coût quasi nul (30 min) — à faire sans en attendre un effet garanti.
6. **Réorienter la production vers l'informationnel.** 99,9 % des Aperçus IA se déclencheraient sur des requêtes informationnelles, contre 3,2 % sur des requêtes transactionnelles pures. Répartition indicative : ~70 % contenu informationnel, ~20 % hybride (comparatif avec offre, guide d'achat), ~10 % transactionnel pur (fiches produit).
7. **E-E-A-T appliqué à l'écriture** : exemples tirés d'une pratique réelle plutôt que génériques, prise de position sur les sujets qui divisent le domaine (une IA cherche un avis construit, pas un contenu neutre qui dit tout et son contraire), auteur identifié avec une page dédiée, sources citées explicitement.
8. **Présences tierces** — forums de niche, podcasts, collaborations : 67 % des citations ChatGPT proviendraient de sources non influençables (Wikipédia, pages d'accueil, stores d'applications) — mais ça laisse ~32 % (pages éducatives, avis, actualités, articles de blog) qui restent influençables, et c'est là-dessus qu'il faut jouer.

**Non prioritaire tant que le site n'a pas encore de contenu SEO de base.** Ce chapitre s'ajoute à la méthode déjà posée (Étapes 1 à 8), il ne la remplace pas — un site sans contenu informationnel construit n'a simplement rien à faire citer par une IA.

⚠️ **Sur l'achat de backlinks et le « ninja linking » (backlinks placés sans l'accord du site hôte, souvent via des failles ou des commentaires).** Les lignes directrices de Google interdisent explicitement les schémas de liens (achat, échange massif, réseaux de sites créés pour se lier entre eux) — la sanction va de la dévaluation des liens concernés à une pénalité manuelle qui peut faire disparaître un site des résultats. Un domaine récent qui accumule d'un coup un grand nombre de liens artificiels envoie un signal anormal facilement détectable. **La voie durable :** obtenir des liens par du contenu qui mérite d'être cité, des partenariats réels, des mentions presse, des collaborations avec d'autres sites de la niche. Le risque d'un lien acheté ou placé sans autorisation n'est pas seulement moral — c'est un risque business direct : la perte du canal SEO entier sur lequel toute la stratégie de contenu vient d'être construite.

## Étape 1 — Recherche de mots-clés, en 3 niveaux

**Niveau 1 — le mot-clé principal (un seul).** Central, souvent concurrentiel. Tout le contenu le renforce indirectement.

**Niveau 2 — les mots-clés secondaires.** Déclinaisons directes : variantes de couleur/matière/usage/genre/taille en e-commerce ; sous-thématiques en blog ; spécialités, zones géographiques et typologies de clients en service. **Chaque secondaire avec un volume suffisant = une page dédiée.**
*Ex. porte-clés :* porte-clé LEGO · mural · crochet · labubu · voiture. *Ex. agence SEO :* audit SEO · SEO local · SEO e-commerce · consultant SEO freelance · formation SEO.

**Niveau 3 — la longue traîne.** Requêtes de 4 à 7 mots, à intention informationnelle. Moins de volume unitaire, intention beaucoup plus précise, conversion souvent excellente. Sur 200-300 articles, le cumul devient massif.
*Ex. :* « quelle console retrogaming choisir pour débuter » · « combien de protéines par jour pour prendre du muscle » · « manger des glucides le soir fait-il grossir ».

### Les 5 sources

**1. Google Suggest.** Gratuit, instantané, ce sont de vraies recherches. **L'astuce de l'alphabet :** taper « [mot-clé] a », « [mot-clé] b »… pour chaque lettre. En 20 minutes, 50 à 100 mots-clés. Les classer par intention : transactionnelle (acheter, prix, livraison, comparatif) → page produit ou collection ; informationnelle (comment, pourquoi, qu'est-ce que, meilleur) → article.

**2. Recherches associées** (bas de page Google) — 6 requêtes supplémentaires, ce sont les étapes logiques suivantes du parcours du persona. Tout noter.

**3. PAA — People Also Ask.** La mine d'or sous-exploitée. Si Google affiche la question, c'est qu'il y a de la demande. Chaque question devient un H2, un H3, ou une entrée de FAQ. **L'astuce de l'infini :** cliquer sur une question en fait apparaître d'autres, et ainsi de suite — un seul mot-clé peut générer 20 à 30 sujets.

**4. Semrush / Ahrefs.** Comparer son URL à 3-5 concurrents directs → liste des mots-clés sur lesquels ils se positionnent et pas nous. Filtres de départ : volume > 100/mois, difficulté (KD) < 40, intention informationnelle pour les articles. Deuxième méthode : entrer le mot-clé principal et ouvrir la section « questions ». Résultat : 50 à 500 articles à créer pour les 6 prochains mois.

**5. Analyse SERP manuelle — la plus importante.** Pour chaque mot-clé, avant d'écrire :
- Taper la requête en navigation privée, regarder les 10 premiers résultats
- **Identifier le TYPE de page qui domine** : collections → créer une collection ; articles → créer un article ; fiches produit → créer une fiche produit ; vidéos → envisager une version vidéo. **Si Google veut des articles et qu'on publie une page produit, on ne rankera jamais** — peu importe la qualité. C'est une erreur de format, pas de contenu.
- Analyser les 3 premiers en détail : leurs H2, les sujets traités, et **surtout ce qu'aucun n'a traité**. C'est là qu'est l'avantage concurrentiel. L'article doit couvrir au minimum tout ce qu'ils couvrent.

**6. Forums et communautés (Reddit, groupes Facebook, Discord de la niche).** Les questions qui s'y posent sont, mot pour mot, ce que la même audience tape ensuite sur Google — une source gratuite de sujets réels, pas déduits.

**7. Avis clients (Google, Trustpilot, avis produit).** Pas pour la recherche de mots-clés au sens strict, mais pour le vocabulaire exact — les mots que les clients utilisent spontanément pour décrire leur problème, à réinjecter dans le champ lexical (Étape 5) plutôt qu'un vocabulaire déduit de l'extérieur.

**Règle de fond sur le volume, avant même les 7 sources : tout volume est bon à prendre.** Un mot-clé à 30 recherches/mois avec la bonne intention vaut souvent plus qu'un mot-clé à 3 000 recherches mal ciblé — éliminer systématiquement les petits volumes revient à écarter la partie la plus qualifiée du trafic potentiel.

## Étape 2 — La règle absolue : 1 mot-clé = 1 page

Chaque page cible **un seul** mot-clé principal. Deux pages sur le même mot-clé se font concurrence, Google reçoit deux signaux contradictoires et finit souvent par n'en montrer aucune. C'est la **cannibalisation**, une des causes les plus fréquentes de stagnation SEO.

**Détection** — comparer les SERP des deux mots-clés suspects (outil cité : 12pages.com) et lire le taux de similarité :
| Similarité | Lecture | Action |
|---|---|---|
| > 80 % | Quasi la même SERP | Une seule page pour les deux, ou garder la meilleure et désindexer l'autre |
| 50-79 % | SERP partiellement proches | Deux pages possibles, mais différenciation très nette exigée |
| < 50 % | SERP vraiment différentes | Deux pages distinctes, sans risque |

*Cas type :* « programme musculation débutant » et « programme fitness débutant » à 82 % → fusion en un article plus complet → positions en progression immédiate.

**Le même réflexe s'applique en amont, avant même d'écrire.** Avant de créer un nouvel article sur un mot-clé, vérifier si une page existante (à soi) est déjà positionnée à proximité du top 3 pour ce même sujet. Si oui, **rafraîchir cette page plutôt que d'en publier une nouvelle** — un nouvel article lui ferait concurrence et freinerait sa progression, avec un coût réel : plusieurs mois perdus le temps que Google redistribue son autorité entre les deux. Le rafraîchissement (mise à jour du contenu, du champ lexical, du maillage) capitalise sur l'autorité déjà acquise par la page au lieu de repartir de zéro. **Repère pratique :** une page déjà en page 2 (positions ~8-15) sur le mot-clé visé est presque toujours un meilleur candidat au rafraîchissement qu'à un nouvel article.

## Étape 3 — La stratégie sémantique (le vrai gisement)

La plupart des sites se battent uniquement sur leurs mots-clés évidents. Le gros gain est ailleurs : **les gens qui ont le même besoin mais le formulent autrement**, et ceux qui ne connaissent pas encore le produit mais en ont besoin.

*Console retrogaming — mot-clé évident : « console retrogaming ». Élargissement :*
« comment jouer aux jeux de son enfance » (article nostalgique qui présente la solution) · « cadeau geek original » (volume énorme, intention cadeau) · « émulateur vs console retrogaming » (comparatif qui capte les hésitants) · « top 5 des meilleurs jeux SNES » (liste nostalgique) · « console pour enfant de 6 ans » (segment parent).
→ Ces gens n'auraient jamais tapé « console retrogaming ». Volume potentiel **×5 à ×10**, sans changer le produit.

*Coaching en reconversion — mot-clé évident faible en volume. Élargissement :* « comment changer de métier à 40 ans » · « suis-je fait pour être entrepreneur » · « burn-out que faire ensuite » · « métiers qui recrutent sans diplôme » · « reconversion développeur web ». Des gens en plein processus de décision → leads qualifiés en continu.

**La question qui débloque les angles : « Quels sont TOUS les problèmes que mon produit résout ? »** Pas le produit — les problèmes. Une console retrogaming ne résout pas « vouloir jouer aux vieux jeux » : elle résout la nostalgie, le manque de jeux simples pour toute la famille, le besoin d'un cadeau original, l'envie de découvrir les classiques sans configurer un émulateur. Chaque problème = un angle = de nouveaux mots-clés = une nouvelle audience.

**Grille en 6 catégories pour cartographier systématiquement les angles d'un seul produit** (avant même la recherche de mots-clés — sauter cette étape, comme le fait la majorité des e-commerçants, produit une stratégie construite sur le seul mot-clé évident) :
1. **Angles produit direct** — toutes les façons dont le produit lui-même se nomme (ex. bijoux personnalisés : « collier prénom », « bracelet gravé », « bague ajustable », « bijou avec message »).
2. **Angles par occasion** — le produit comme cadeau, calé sur un calendrier saisonnier (« cadeau fête des mères pas cher », « idée cadeau demoiselle d'honneur »). Publier l'article avant la saison, pas pendant.
3. **Angles par destinataire** — qui le reçoit change le parcours d'achat même pour le même produit (« bijou personnalisé maman » vs « bracelet prénom ado » : deux profils, deux intentions).
4. **Angles émotionnels et de signification** — le registre le plus délaissé, et le plus qualifié : volume faible, intention d'achat quasi maximale (« bijou pour se souvenir d'une personne disparue », « collier couple longue distance »).
5. **Angles matériaux et technique** — les acheteurs qui filtrent et comparent avant d'acheter, taux de conversion le plus élevé de tous (« argent 925 », « waterproof », « acier inoxydable »).
6. **Angles comparatifs et de décision** — la phase juste avant l'achat (« meilleur site [catégorie] France », « avis [marque] », « livraison rapide »).

**Ce que ça produit sur un seul produit :** des dizaines de mots-clés répartis sur 6 intentions différentes, largement de quoi couvrir plusieurs mois de cadence sans jamais répéter le même angle — et ça, avant même d'avoir ouvert un outil de recherche de mots-clés.

## Étape 4 — Le plan d'article

**H1 — le titre.** Mot-clé principal dans les 5 premiers mots, 65 caractères max (au-delà, tronqué).
❌ « Tout ce qu'il faut savoir sur les consoles retrogaming » → ✅ « Console retrogaming : comment choisir la meilleure en 2026 »

**Introduction — la réponse en 3 lignes maximum.** La règle la plus violée. La réponse à la question du H1 est dans les 3 premières phrases. Pas après un contexte de 10 lignes, pas après « Vous vous posez des questions sur X ? ». Raisons : l'utilisateur veut sa réponse tout de suite ou il repart sur Google ; Google lit les premières lignes pour comprendre la page ; ça démontre la maîtrise du sujet (E-E-A-T) dès la première phrase.

**H2 — les piliers thématiques.** Sources : les PAA collectés, les H2 des top 3 (traités à sa façon, jamais copiés), la connaissance du marché. Règles : 5 à 6 H2 maximum ; chaque H2 apporte une information que l'intro n'a pas donnée ; vocabulaire du champ lexical ; ordre calé sur le parcours du persona.

**H3 — les sous-points.** 3 maximum par H2. Au-delà, le H2 est trop large : le découper en deux.

**H4 — à éviter.** Structure trop profonde. Transformer en paragraphe avec un mot en gras en tête, ou en liste à puces.

**FAQ** — en fin d'article, avant la conclusion. 5 à 9 questions. Titre contenant le sujet précis (« FAQ sur la console retrogaming portable ») : ça dit à Google de quoi parle la section et ça renforce la pertinence sémantique.

**Liens internes** — 1 à 2 par article, pas plus (10 liens diluent la valeur de chacun). Priorité vers la page commerciale la plus pertinente. **Ancre = le mot-clé exact de la page de destination.** Jamais « cliquez ici », « en savoir plus », « voir ici ».

**La structure qui organise tout ça à l'échelle du site : le silo thématique.** Une page pilier centrale traite le sujet principal en profondeur ; des articles satellites couvrent chaque sous-thématique en détail ; chaque satellite pointe vers le pilier, et le pilier pointe vers ses satellites. Ce maillage bidirectionnel concentre le jus SEO sur la structure entière plutôt que de le laisser se disperser entre des articles isolés qui ne se renforcent jamais — c'est ce qui fait qu'un site avec 20 articles organisés en silo dépasse souvent un site avec 40 articles éparpillés sans hiérarchie.

**Optimiser aussi les pages business, pas seulement les articles de blog.** Les pages produit, collection ou service sont ce qui convertit directement — et pourtant elles restent souvent avec un contenu vide ou générique pendant que tout l'effort SEO va aux articles. Même discipline à leur appliquer : un H1 avec le mot-clé exact que les clients tapent, une description qui couvre le champ lexical complet du sujet, une FAQ en bas de page pour lever les objections avant l'achat, des éléments de réassurance (avis, certifications, garanties), et surtout **une page dédiée par produit/collection/service** — une page qui essaie de tout couvrir ne se positionne sur rien. Les articles de blog doivent aussi faire remonter le jus SEO vers ces pages via leurs liens internes (voir ci-dessus) : c'est le blog qui construit l'autorité, mais ce sont les pages commerciales qui doivent en hériter pour que ça se traduise en chiffre d'affaires.

## Étape 5 — Topical SEO

Ce qui sépare la page 2 de la position 1.

**Ce que ce n'est pas :** répéter le mot-clé 20 fois, « optimiser la densité ». Techniques dépassées, parfois pénalisantes.

**Ce que c'est :** couvrir un sujet avec une profondeur et une richesse sémantique telles que Google reconnaît le site comme référence sur la thématique. Google n'évalue plus une page isolément — il évalue l'expertise globale du site sur un sujet. Un site qui couvre tous les angles d'une thématique se positionne y compris sur des mots-clés pour lesquels il n'a pas encore d'article.

**Le champ lexical sémantique.** Chaque sujet a un vocabulaire que Google attend d'un contenu expert.
*Console retrogaming portable —* contenu faible : « console retrogaming portable », « acheter une console… ». Contenu expert : émulateur, ROMs, BIOS, firmware · Raspberry Pi, Anbernic, Miyoo, Powkiddy · écran IPS/OLED, ratio 4:3 · autonomie (mAh) · RetroArch, EmulationStation · compatibilité NES/SNES/GBA/PS1/N64 · overclocking, latence d'affichage · carte SD, format ROM.
*Café single origin —* terroir, altitude 1200-2000 m, ombre vs soleil · Typica, Bourbon, Geisha, Robusta · lavé, naturel, honey process · acidité, corps, arômes · score cupping SCA · Éthiopie Yirgacheffe, Colombie Huila · torréfaction, réaction de Maillard.

**Trois façons de le construire :** (1) les PAA et Google Suggest rassemblent automatiquement le vocabulaire du domaine — les termes qui reviennent sont les termes importants ; (2) l'analyse des top 3 révèle les termes que Google attend sur ce sujet ; (3) **la connaissance métier**, la plus puissante et introuvable avec un outil — c'est précisément ce que Google récompense sous l'étiquette E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness).

**Rôle de BOS ici :** les méthodes 1 et 2 sont du travail que BOS fait intégralement. La méthode 3 est le seul input irréductiblement humain — c'est ce que BOS doit aller chercher chez l'entrepreneur, par questions ciblées, avant de rédiger.

## Étape 6 — Écrire pour le persona, pas pour l'algorithme

Google observe des signaux comportementaux : temps de lecture, profondeur de scroll, clics sur les liens internes, retour immédiat sur Google. Si les gens fuient en 10 secondes, la position se dégrade ; s'ils lisent jusqu'en bas et cliquent, elle monte. Donc on écrit pour le persona — l'algorithme suit.

**Le ton se calibre :**
| Contexte | Ton |
|---|---|
| Boutique retrogaming | Nostalgique, entre initiés, vocabulaire gamer assumé, références culturelles partagées, humour |
| Coaching reconversion | Empathique, rassurant, exemples vécus, validation des émotions, aucune promesse irréaliste |
| SaaS comptable | Direct, chiffré, bénéfices mesurables (« gagnez 3 h par semaine »), pas d'émotion |
| Blog skincare | Accessible, vulgarisation des termes techniques, zéro jugement, tous types de peau |

Même information, même thématique, mauvais ton pour le persona = pas de résultats.

## Étape 7 — Règles de rédaction

1. **Aérer.** Plus de 50 % du trafic est mobile ; un pavé de 10 lignes fait fuir. 3-4 lignes par paragraphe maximum. Une phrase forte peut être un paragraphe. Listes à puces pour les énumérations.
2. **ALT d'image descriptif** contenant le mot-clé, et nom de fichier parlant (`console-retrogaming-portable.webp`, jamais `IMG_4821.jpg`). Google Images est un canal d'acquisition très sous-coté.
3. **Format WebP.** Même qualité, 2 à 3× plus léger. Cible 100-150 Ko par image ; au-delà de 1 Mo, problème de performance sérieux.
4. **FAQ nommée précisément** (voir étape 4).
5. **Pas de H4.**

## Étape 8 — La cadence

**1 article par jour, minimum.** Pas 3 fois par semaine, pas « quand j'ai le temps ». C'est l'étape que la plupart abandonnent, et celle qui fait la différence sur 12 mois.

- **Le topical SEO se construit sur le volume.** 100 articles sur une thématique = site de référence. 5 articles, même excellents, ne construiront jamais cette autorité.
- **Chaque article est un canal d'acquisition.** 1 article = 1 flux de trafic depuis un mot-clé différent. 300 articles = 300 flux qui s'additionnent.
- **Google aime les sites actifs.** Publication quotidienne = crawl plus fréquent = indexation plus rapide = trafic capté avant les concurrents.

**La cadence se réduit avec la maturité du site, elle ne reste pas fixe indéfiniment :** lancement (mois 1-3) — 1 article/jour si possible, 3/semaine au minimum ; croissance (mois 4-12) — 3 articles/semaine, indexation manuelle systématique ; maturité (12 mois+) — 2 nouveaux articles/semaine + 1 article existant rafraîchi par semaine (cohérent avec la règle « réécrire plutôt que créer » posée plus haut). Le rythme de démarrage sert à construire l'autorité thématique de zéro ; une fois construite, l'entretien pèse plus que la pure création.

**Indexation manuelle :** 10 demandes gratuites par jour dans la Search Console. Les utiliser à chaque publication force le crawl immédiat au lieu d'attendre — ça fait passer le délai d'indexation d'une fourchette de 2 à 6 semaines à environ 24-72 h.

## Résumé opérationnel

1. Comprendre business, persona, marché, concurrence
2. Identifier le mot-clé principal (pas forcément la home)
3. Construire la liste en 3 niveaux
4. Exploiter les 5 sources : Suggest, recherches associées, PAA, SERP manuelle, outils
5. Étendre en sémantique (même besoin, mots différents)
6. Structurer chaque article : H1 optimisé, intro directe, H2/H3 issus des PAA, FAQ précise, 1-2 liens internes à ancre exacte
7. Appliquer le topical SEO : champ lexical riche, tous les angles couverts
8. Écrire pour le persona
9. Publier tous les jours, demander l'indexation systématiquement

## Répartition BOS / entrepreneur

| Étape | Qui |
|---|---|
| Compréhension business et persona | Questions ciblées de BOS, réponses de l'entrepreneur |
| Recherche de mots-clés 3 niveaux, 5 sources | **BOS** |
| Détection de cannibalisation | **BOS** |
| Stratégie sémantique et angles | **BOS** |
| Plans d'articles (H1, intro, H2/H3, FAQ, maillage) | **BOS** |
| Champ lexical | **BOS**, complété par la connaissance métier de l'entrepreneur |
| Rédaction | **BOS**, relecture et validation par l'entrepreneur |
| Publication, images, indexation Search Console | Entrepreneur (~15 min/jour) |

C'est l'argument à lui donner tel quel : *« La cadence d'un article par jour est ce qui fait échouer 95 % des gens sur ce canal. Toi, tu as un copilote qui fait la recherche, le plan et la rédaction — ton job c'est 15 minutes de publication et ta connaissance métier. Les autres font tout ça à la main. »*

**Le dernier maillon (publication + indexation) est automatisable une fois la boutique connectée.** Des outils comme PushRank vendent exactement ça : lire Search Console, prioriser les mots-clés à faible effort, rédiger, publier directement sur le CMS (Shopify, WordPress...) via webhook, sans copier-coller. Ce n'est pas une stratégie différente de celle déjà posée ci-dessus — c'est la même méthode, avec le dernier maillon automatisé. Une fois la boutique Shopify de l'entrepreneur en place et connectée (accès admin API), BOS peut publier directement les pages/articles sans passer par l'entrepreneur, fermant cet écart sans abonnement payant — avec un avantage que ces outils génériques n'ont pas : le contexte business, la voix de marque et la recherche client déjà accumulés dans `Core/` et `Knowledge/`, pas seulement des données Search Console. **Non applicable tant que le SEO n'est pas le canal retenu** (canal actuel : organique social, une chose à la fois) — à activer si/quand `traffic` route vers le SEO.

---

## Réserves — ce que BOS doit nuancer

Le corps de la méthode est solide et applicable tel quel. Trois points méritent une correction avant d'être servis à un entrepreneur :

- **Les H4 ne sont pas « un signal négatif pour Google ».** Google n'a jamais documenté de pénalité liée à la profondeur de titres. Le conseil reste bon comme **règle de lisibilité** — une structure à quatre niveaux signale généralement un plan mal découpé — mais le présenter comme une règle d'algorithme est faux.
- **Le balisage FAQPage ne produit plus de rich results dans la majorité des cas.** Depuis 2023, Google réserve l'affichage des FAQ enrichies dans la SERP à un ensemble restreint de sites institutionnels et de santé. Garder la section FAQ — elle sert la pertinence sémantique, l'expérience de lecture et les PAA — mais ne pas vendre à l'entrepreneur des questions affichées dans la SERP.
- **Un article par jour n'est un objectif valable que si la qualité tient.** Publier 300 articles faibles construit un site que Google traite comme un site faible. La cadence est un multiplicateur de la méthode, pas un substitut : si BOS et l'entrepreneur ne peuvent pas tenir un article par jour au niveau décrit en étapes 4-6, mieux vaut 3 par semaine bien faits. Sortir cette nuance quand un entrepreneur s'engage sur la cadence — c'est le point exact où il va s'épuiser ou saborder le résultat.
