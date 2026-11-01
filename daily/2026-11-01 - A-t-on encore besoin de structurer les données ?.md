
Les fenêtres de contexte et les capacités de raisonnement des modèles sont devenues telles que l'on est en droit de se poser la question : a-t-on, oui ou non, encore besoin de structurer les données pour obtenir des réponses précises ou construire des logiciels robustes ? 

Pourquoi ne pas donner à un modèle tous les fichiers dont on dispose, sans structure aucune, et laisser le modèle s'en occuper ? Une proposition apocalyptique pour tous les [[data]] analystes, [[data]] scientists dont c'est en partie le métier de structurer les données. Une proposition volontairement provocatrice mais qui, à l'heure où l'on ne sait plus ce que les modèles ne savent pas faire, me parait légitime. 

En sous-main, cette question en pose une autre, plus intéressante peut être : qu'est-ce qu'apporte la structure des données aux modèles ? Avec une réponse précise, on pourra alors mieux comprendre s'il est préférable ou non de laisser les modèles s'occuper de la structuration des données. 

Un avertissement aux lecteurs : je vais porter ici en priorité l'accent sur la méthodologie qui me permet de répondre à cette question (`A-t-on, oui ou non, encore besoin de structurer les données ?`), que sur la réponse elle-même. Il est plus question pour moi ici de donner aux [[data]] scientists, [[data]] analysts ou experts en [[knowledge graph]] le moyen de démontrer **la valeur de leur expertise**. Car oui, vous l'aurez compris, ma conclusion va être ici que oui, on a toujours besoin de structurer les données. Je dirai même : on en a besoin, **plus que jamais !**

# Laboratoire d'expérimentation : le [canon ball](https://canon-ball-production.up.railway.app/)

Je vais ici utiliser une petite application créée pour comprendre ce qu'un *[[knowledge]] [[layer]]* apporte à un modèle de connaissance, dite canon ball : 

![[canon-ball .png]]

Cette petit application file la métaphore du modèle de langage considéré comme canon qui tirerait des boulets dans un espace (sémantique). Il permet : 
1. de modifier les paramètres du canon (ici par l'adjonction de différents types [[knowledge]] [[layer]], chargés dans le canon de différentes manières, voir tous les détails dans l'application)
2. de faire des tirs selon différents ensembles de paramètres 
3. de récupérer et surtout de **comparer** les positions des différents boulets selon qu'ils aient été tirés par un ensemble de paramètres ou un autre. 

L'expérimentation que j'y ai ai faite est ici toute simple. J'ai posé la même question au même modèle de langage (un gemma-2b) : `Tous les himalayistes sont-ils des alpinistes ?`

J'ai mis ce modèle  dans deux dispositions différentes. D'un côté, le modèle disposait d'un [[system prompt]] écrit sous la forme d'un texte (une chaine de caractère brute) : 

```
L'alpinisme est une pratique sportive de montagne, exercée par des alpinistes et des guides de haute montagne.

Plusieurs pratiques et styles lui sont associés. L'escalade alpine est pratiquée par des alpinistes, des grimpeurs sur rochers et des ice climbers. Le style alpin, le style expédition, l'alpinisme sans guide, le high altitude climbing et le scrambling n'ont pas de pratiquant précisé. L'alpinisme en haute altitude est pratiqué par des alpinistes, et le ski de randonnée par des skieurs alpinistes.

Deux pratiques relèvent du loisir et de la collection de sommets : le recreational mountaineering, pratiqué par des alpinistes, et le peak bagging. On y associe le himalayisme, pratiqué par des himalayistes, le tatranisme, pratiqué par des alpinistes de la Tatra, le mountain hiking in Norway et le Munro-bagging.

Enfin, certaines pratiques sont liées à un lieu : le pyrénéisme, le kunimi, le mountaineering in Russia, l'alpinism in Latvia, le mountaineering in Jordan, la via ferrata sur le mont Ilyas-Kaya et le mountaineering in Mount Fuji. Autour du mont Fuji, on trouve aussi le bullet climbing, le Mount Fuji Ekiden et la course du Mont Fuji.
```

De l'autre, il disposait de ce même texte, mais cette fois-ci mis sous le forme d'un [[knowledge graph]]. Pour le créer, j'ai simplement extrait du texte un ensemble de concepts reliés, comme dans une taxonomie ([[taxonomy]])  traditionnelle, par des relations `estUnSousConceptDe`. J'obtiens ainsi : 

![[kg-canon.png]]


De cette manière, je vais pouvoir comparer la réponse d'un modèle qui a été alimenté par de la connaissance structurée d'un côté et par de la connaissance non-structurée de l'autre. 

Autant vous dire tout de suite que j'ai adoré les résultats de cette expérimentation. 

# Les résultats : sans structure, le modèle fait des erreurs magistrales 

Les résultats se présentent sous cette forme : 


![[results-canon.png]]

Commençons par ce que la structure **n'apporte pas au modèle** : 
1. la structure ne permet pas au modèle d'être plus consistant sémantiquement dans ses réponses. On le voit au fait que la zone d'atterrissage du canon avec le paramétrage de [[test]] n'est pas plus étroite que celle du canon avec le paramétrage de contrôle 
2. la structure ne [[change]] pas non plus fondamentalement le sens des réponses. On le voit à l'overlap important entre les deux zones d'atterrissage. 

Maintenant, sur que la structure apporte au modèle : 
1. **elle lui permet de répondre correctement à la question**. En effet, ici, la bonne réponse est que tous les himalayistes sont des alpinistes. L'alpinisme désigne ici toute pratique qui consiste à gravir des sommets montagneux (comme l'a dit la mère du célèbre alpiniste français Lionel Terray : "L'alpinisme est un sport stupide qui consiste à grimper les rochers avec les mains, les pieds, et les dents !"), et l'himalayisme est une pratique spécifique de l'alpiniste sur la chaîne himalayenne 

2. elle lui donne la bonne manière de raisonner. C'est ici la chose la plus fascinante. Regardez ci-dessous de près la réponse 13 (sans) qui a été générée avec une connaissance non-structurée. Il s'y trouve une **erreur flagrante de logique** : tous les himalayistes ne sont pas des alpinistes MAIS l'alpinisme est une pratique plus large sur l'himalayisme 🤯. La logique formelle exige que si A est un sous-ensemble de B, alors tout élément de A fait nécessairement partie de B. Un enfant de 5 ans comprend cela aisément (peut être pas expliqué sous cette forme, certes). Le modèle, sans connaissance structurée, fait cette erreur **alors qu'avec la connaissance structurée, il applique correctement la logique**

![[error-canon.png|378]]


# Interprétation : on a, plus que jamais, besoin de structurer les données

Tout simplement. Ce que cette petite démonstration montre c'est qu'à ne pas se soucier de la structure des données que l'on donne aux modèles, ou à laisser le modèle définir lui-même la structure (AI-generated ontologies), on perd toute maitrise du **sens à donner aux données**. J'ai ici développé un exemple extrême où un petit modèle a fait une énorme erreur de logique dans son raisonnement, mais il est fort probable que les plus grands modèles font également des erreurs d'interprétation, évidemment plus subtiles, mais qui peuvent valoir très chers dans des domaines ou industries de pointes. 