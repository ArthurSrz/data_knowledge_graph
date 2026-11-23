
Moscou, mai 1928. Un jeune journaliste, dit S., passe la porte d'un célèbre neurologue russe, A.R. Luria et demande à ce que sa mémoire soit testée. Il explique avoir été envoyé par le rédacteur en chef de son journal après un rude échange avec lui le matin même. Interloquée, la neurologue demande par quelles manifestations soudaines ses pathologies se sont déclarées, et la journaliste S de répondre qu'il n'est pas question de pathologie, bien au contraire. 

Il raconte son histoire. Il vient d'intégrer la rédaction de son journal, et chaque matin il assiste au briefing de son rédacteur en chef, au cours duquel ce dernier liste tous les faits, les scoops et les histoires à creuser pour les prochaines éditions Il explique également que tous les journalistes autour de lui prennent des notes, mais pas lui. 

Après avoir laissé le jeune reporter sans prendre de notes pendant 1 semaine, ce matin là, le rédacteur, furieux du manque de professionnalisme affiché, s'est permis de lui dire ses 4 vérités, la plus claire d'entre elle étant qu'il est inadmissible d'ignorer toutes les informations transmises au cours du brief. 

Le journaliste S. aurait du s'excuser, mais il ne le fit pas. Car il était sous le choc et à raison : il était tout sauf naturel de se rappeler du moindre fait, de la moindre anecdote comme il le faisait depuis sa plus tendre enfance ! Ce qu'il prenait pour une faculté naturelle était en fait une anomalie physiologique. 

A.R Luria, émerveillée par cette histoire s'est évidement mise à étudier le cerveau de ce journaliste, allant jusqu'à y dédier un ouvrage : *The Mind of a Mnemonist: A little Book About a Vast [[memory]]*. Elle y raconte que la mémoire exceptionnelle de S. lui vient d'une désordre perceptif extrêmement rare : la synesthésie (un des plus beau mot de la langue française selon moi en passant). Cette anomalie fait que chaque mot, chaque phrase prononcée et entendue de S. est traitée par l'ensemble de ses capacités perceptives. Son cerveau fait la synthèse (synesth-) de tous les sens (-ésie), tant et si bien que pour lui, certains mots ont des couleurs, des concepts ont une odeurs, les phrases une signature tactile. 

En clair : son cerveau lui offre des capacités de représentation de la connaissance qui lui donne la possibilité d'avoir accès tout le temps à l'intégralité de ce qu'il a jamais vu ou entendu au cours de sa vie. Par exemple, il explique : 

> [!quote] Citation
> Prenez le chiffre 1. C'est un homme fier, bien bâti ; le 2 est une femme pleine d'entrain ; le 3 une personne sombre (pourquoi, je l'ignore) ; le 6 un homme au pied enflé ; le 7 un homme à moustache ; le 8 une femme très corpulente — un sac dans un sac. Quant au nombre 87, ce que je vois, c'est une grosse femme et un homme qui tortille sa moustache
> 
> Extrait de *Moonwalking with Einstein*, Joshua Foer

La morale à tirer du journaliste S., c'est que quand il est question de capacités de connaissance supérieures, à l'ombre desquelles siège l'intelligence, c'est du côté du mode de représentation qu'il faut chercher plutôt que de celui de la force brute. Appliqué à l'intelligence artificielle, cette histoire nous dit que sans maitrise de la représentation de la connaissance, la puissance de calcul n'est rien. 

Dans le 17ème numéro du Bateau ivre, j'explore en quoi à représenter la connaissance sous la forme de circuits d'activation de neurones, on gagne de nouveaux super-pouvoirs. 
***


J’ai établi que la connaissance laissait des traces plus profondes que le prompt dans la tête des modèles de langage.

Qu’est ce qui me permet d’établir une telle chose ?

Principalement l’observation de cartes d’activation des neurones (features) de modèles de langage dans différentes configurations. Il me semble, à la lecture de dizaines et dizaines d’entre elles, que les modèles avaient tendance à délaisser les neurones liés au prompt pour solliciter ceux liés à la connaissance quand elle est disponible.

De fil en aiguille, je me suis laissé aller à établir deux hypothèses, aussi fragiles que spéculatives :
1. Plus la connaissance est importante, moins le modèle sollicite ses capacités de complétion généraliste
2. En tirant le fil de la première hypothèse : si la connaissance établie est complète (relativement à un domaine de connaissance), un ensemble suffisamment grand de [[prompts]] doit aboutir uniquement à une reconstruction de la connaissance initiale (0% d’activations liées au prompt, 100% liées à la connaissance)

La fragilité des deux hypothèses tient ici à la facilité de leur falsification. Concernant la première hypothèse, on peut aisément imaginer une configuration avec un corpus de connaissances en croissance et une plus forte sollicitation des capacités de complétion généraliste. À propos de la deuxième, rien de plus facile que de trouver un cas où malgré un corpus de connaissance complet, 15% (ou 30 % ou 45%) des activations restent liées au prompt.

Dans ce cadre, pourquoi continuer à explorer la société de connaissances si les hypothèses établies sont si fragiles ?

Parce qu’en les écrivant et en les publiant, j’augmente la probabilité de les voir réfutées par l’un d’entre vous (chers lecteurs), ce qui ne pourra qu’aider à une meilleure compréhension collective du sujet. Plus spécifiquement :

1. Je saurai en quoi mes hypothèses sont fausses et j’arrêterai de les diffuser
2. Quelqu’un pourra me contredire et faire rayonner des hypothèses mieux soutenues
3. Tout observateur de la controverse pourra à son tour se forger une opinion critique de la chose

En tout état de cause, et en gardant en tête la fragilité de mes hypothèses, j’ai le privilège de poser d’autres questions encore plus aventureuse (un salaire bien suffisant pour toute entreprise intellectuelle). En l’occurrence
  
> [!info] Question 1
> Comment se forment ces chaînes d’activation dans la tête des modèles de langage quand ils parcourent le corpus de connaissance ?

  

> [!info] Question 2
> L’intérêt de ces chaînes d’activation ne dépasserait-il pas le cadre de la technologie ? N’y a t’il pas un effet au niveau de la relation homme-machine, j’entends par là : la creation d’un [[pattern]] vertueux ?

  
Savoir qu’une chaîne d’activation de neurones a lieu dans un corpus de connaissance amène un bouleversement de notre représentation de ce que fait un modèle de langage. Or, à représenter autrement un phénomène, on déclenche très souvent d’autres comportements, d’autres interactions avec ce même phénomène.

Pour illustrer le propos : si les boutons d’alarmes incendie dans un bâtiment étaient gris, nous serions naturellement beaucoup enclins à appuyer dessus (et c’est pourquoi ils sont rouges). Autre représentation, autre comportement. En chimie, en représentant les molécules sous la forme de graphes, on a pu comprendre comment un ensemble de mêmes atomes pouvait constituer deux molécules différentes (les isomères) et alors imaginer des molécules encore jamais observées mais possibles par représentation (par construction). La cause étant qu’un même ensemble de noeuds peut être reliée par différentes configurations de relations. Autre représentation, autre comportement.

Sachant que dans la tête du modèle se forme des chaînes d’activation et sachant également que nous sommes plus à même de maîtriser finement une technologie si l’on peut lui donner des [[instructions]] sous la forme même de son fonctionnement profond (loi des abstractions), il y a un intérêt certain à décrire des chaînes d’activation pour maîtriser un modèle de langage.

Incidemment, on peut dire que cette autre représentation permet d’exercer de l’intelligence sur l’intelligence (artificielle). Elle nous redonne une capacité qui semble avoir été battue en brèche depuis 2022 : re-faire la bascule vers l’imagination, qui est nécessaire avant tout exercice de l’intelligence (sur l’intelligence, à nouveau).

Je vais devoir ici faire un détour philosophique, et je m’en excuse mais il est ici plus que necessaire. À décrire des [[instructions]] sous la même forme que le fonctionnement profond des IAs, je dis que l’on redonne à tout travail intellectuel le souffle et la noblesse qu’il a perdu progressivement depuis 2022. Pourquoi est-ce que je dis cela et qu’est ce qui me permet de dire cela ?

Gregory Chatonsky rappelle dans [un de ses articles](https://chatonsky.net/mimetisme-ia/) que l’imagination est la pierre angulaire de l’intelligence :

> « En effet, la phiophie classique a fixé comme objectif à l’intelligence de donner accès à la réalité et d’unifier la diversité chaotique des perceptions en une forme compréhensible(…). Or, dans la première édition de la *Critique de la raison pure,* Kant trouve le principe de cette unification dans l’imagination transcendantale. Le déplacement de l’intelligence vers l’imagination est un mouvement fondamental, car si l’unité des concepts de l’intelligence provient de la faculté à produire des images et des symboles c’est parce que l’imagination est l’autoaffection de l’unité se prenant pour son propre objet »


J’en conviens : la formule est indigeste. Pourtant ce qu’elle est exprime d’une simplicité enfantine. Elle dit tout bonnement qu’avant de pouvoir exercer notre intelligence, nous formons une image de ce sur quoi nous allons l’appliquer. Mettons que je veuille écrire un article. Avant de mettre mon intelligence au service de l’écriture de cet article, il me faut nécessairement une image de ce qu’est un article, sans quoi par où pourrai-je commencer ? 

Dans la même veine, quand on apprend à un enfant à compter, on commence par lui montrer des pommes, des bananes, c’est à dire des images qu’il va pouvoir internaliser avant de pouvoir appliquer une intelligence mathématique sur ces images. Vous pouvez chercher des contre-exemples, mais il me semble qu'il n'en existe aucun. Autrement dit : aucune forme d’intelligence n’est possible sans cette image, pur produit de l’imagination.

(Suite à rédiger autour des idées suivantes : 1. en instruisant selon une chaine d'activation, on peut développer une forme d'intelligence sur l'intelligence ; 2. Mode d'emploi sur le développement d'une chaine d'activation à partir du [[concept]] de *[[Knowledge]] Lines* de Minksy (anecdote : on distingue rarement une connaissance du contexte dans lequel on l'a sollicité avec succès, refaite l'histoire d'une tâche accomplie, notez sur une carte les artefacts qui vous ont accompagné tout au long de la tâche, et qui sont dans votre esprit très très proche voir indistinguible de la connaissance, puis donnez cette [[knowledge]] line au modèle : vous lui donnez alors la création qu'il va pouvoir reconnaitre avant de pouvoir générer ; 3. Développer aussi l'idée selon laquelle les modèles de langage ont été développé de manière mimétique par rapport à l'intelligence humaine, et que donc reconnaissance et génération sont les deux piliers d'un même édifice pour générer il faut reconnaitre et pour reconnaitre il faut générer, lire plus en détail : https://chatonsky.net/mimetisme-ia/))