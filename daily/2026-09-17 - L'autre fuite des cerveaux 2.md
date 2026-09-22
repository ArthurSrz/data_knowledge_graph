
Plus vous investissez de temps dans votre contexte, moins vous dépensez de tokens. Moins vous investissez de temps dans votre contexte, plus vous dépensez de tokens.

Il devient évident que plus nous passons de temps à réfléchir aux [[instructions]] et surtout au contexte que nous donnons aux modèles d'IA générative, moins nous dépensons de tokens ([[context engineering]], comme dirait @Maxime Jousset, qui a ces deux mots, [[context engineering]] et mémoire, dans sa fiche de poste). Un contexte imprécis et un prompt rédigé trop vite suscitent une réponse moyennement satisfaisante au premier abord, donc une suite d'itérations avec le modèle, donc une consommation de tokens plus importante.

Ce sont deux vases communicants.

## Le budget temps-[[token]]

Schématisons. Imaginons un budget de 100 pour effectuer une tâche. Chacun de nous en alloue une part en temps, et une autre en [[token]].

Parfois (souvent ?) nous passons peu de temps à donner du [[context|contexte]] à notre [[Claude]] ou à chatGPT. De fait, la conversation s'allonge, car il faut itérer avant d'arriver au résultat. Mettons que nous passons 30 unités de temps et dépensons 70 unités de tokens. D'autres fois c'est l'inverse. Nous prenons le temps de poser le contexte et nous arrivons mécaniquement plus vite au but. La conversation est plus courte et nous dépensons moins de tokens. Schématiquement, le rapport s'inverse, nous passons 70 unités de temps pour une dépense de 30 unités de tokens. (@Anis Zakari et @Roger Eggebrecht, qui voient ce budget depuis la facture, corrigeront mes proportions.)

Dans tous les cas il y a un [[trade-off]] entre l'un et l'autre, et ce [[trade-off]] décide en grande partie de ce que nous allons faire de cette conversation.

Car plus nous avons passé de temps, plus nous avons tendance à vouloir en parler autour de nous. Nous voulons faire fructifier le temps investi dans la tâche. On en parle autour de soi. On transmet ce que l'on a fait. En revanche, lorsqu'on a plutôt misé sur l'IA Gen, on va plutôt partager la conversation ou l'artefact issu de celle-ci. Deux modes de transmission, tous les deux imparfaits. @Anne-Solène Loiseau les a tous les deux sous les yeux : cent vingt contributeurs d'un côté, un RAG de l'autre. 

Aucune transmission orale n'est parfaite. On n'arrive jamais à faire passer la totalité de ce que l'on sait à autrui. Car autrui oublie, sa mémoire lui fait défaut, et avec le temps, le capital de connaissance s'érode. @Sandrine Vigner, qui installe la fonction KM là où elle n'existait pas depuis plus de vingt ans, a vu passer toutes les vagues d'outils censées régler cela. La transmission de conversation ou d'artefacts est-elle aussi imparfaite. Regardez les contenus générés qu'on vous a transmis : les avez-vous lus ? Peut-être que oui, mais avec moins d'attention que s'ils avaient été faits à la main. Un problème d'adoption plus que d'outil, dirait @Btissam Boughazouali, et elle n'aurait pas tort. La raison profonde est je pense que sans connaitre la motivation ou le contexte sous-jacent à cette conversation, on comprend peu ou pas ce qui s'y trouvent. On manque...de contexte ! 

Dans les deux cas, c'est en chemin que la perte se produit.

Comme si nous jouions tous à être des chimistes et que nous préparions, dans un tube percé, nos superbes solutions, avant d'aller les montrer à d'autres et de réaliser, ô stupeur, que la solution s'était répandue à même le sol. Un peu ridicules sur le moment, nous n'en sommes pas pour autant inquiets : d'un coup de prompt nous pouvons en créer une nouvelle. Ce que nous refaisons d'ailleurs, et dans le même tube percé. À la fin de la journée, le sol est jonché de solutions, perdues pour tous.

## Le tube a un nom

Le tube ici, c'est une [[session]]. C'est à dire du contexte temporaire fait pour échanger des informations.

Une [[session]] possède deux propriétés qui ne vont pas très bien ensemble. Elle est *[[stateful]]* ([[Statefulness]]), c'est-à-dire qu'elle garde un état. Chaque message s'ajoute au précédent, le modèle se souvient de ce que vous avez dit dix échanges plus tôt, la conversation se remplit. Mais elle est aussi impermanente ([[Impermanence]]) : cet état ne dure que le temps de la conversation. Fermez l'onglet, ouvrez-en un autre, et tout est à refaire.

Un récipient qui se remplit et qui ne retient pas : voilà ce qu'est une conversation avec [[Claude]] ou chatGPT.  

Mais cela n'explique que la moitié de notre problème. L'[[impermanence]] explique que *je* perde mon contexte. Elle n'explique pas qu'une autre personne ne puisse pas le recevoir quand je transmets la conversation. Pour comprendre cela, il faut regarder de quoi un contexte est fait.

Un contexte, c'est d'abord du [[text]]e : ce qui est écrit. Mais c'est aussi une identité (qui parle), un statut social (depuis quelle position), un [[environment]] (dans quelles circonstances) et un discours (de quoi on parle). Il est fait de cinq parties, dont une seule concerne la tâche. Les quatre autres concernent la [[situation]], et trois d'entre elles concernent directement la personne. Cette différence entre le texte et le reste est la matière première de @Kamelia Mehenni, linguiste computationnelle devenue ontologiste. 

C'est la deuxième propriété de notre tube. Il n'a pas seulement un trou au fond, il porte une étiquette avec des noms. Il fuit donc parce qu'il est impermanent, et il ne se transmet pas parce qu'il est, d'une certaine façon, unique.

Reprenons alors le calcul du début. Les 70 unités de temps que nous avions investies dans le contexte, où sont-elles allées ? Pas dans la tâche mais dans le récipient ! Un récipient ni durable, ni partageable.

## Ce qui coule n'est pas la solution

Nous avons dit que nous manquions de contexte pour pouvoir transmettre la connaissance présente dans une conversation. Précisons maintenant ce qui fuit.

Faites l'expérience. Un collègue (disons @Louis Brulé Naudet) vous transmet une conversation qu'il a eue avec [[Claude]] à propos d'une [[clause]] de contrat. Vous l'ouvrez. Qu'y trouvez-vous ? Le texte, intégralement : ses questions, les réponses, la [[clause]] réécrite. Cette partie-là du contexte a parfaitement voyagé. Ce que vous ne trouvez pas, c'est le reste. Pourquoi cette [[clause]] ? Pour quel client ? Qu'est-ce qui l'inquiétait ? Que savait-il déjà, que [[Claude]] n'a pas eu besoin de lui redire ? L'identité, la position, les circonstances, le sujet réel de la discussion sont restés dans sa [[session]]. Ils n'ont pas de forme écrite, donc ils ne peuvent pas être copiés. C'est le cas limite que @Julien Ntumba rencontre à chaque transition d'infogérance : tout le contexte est chez le prestataire sortant.

Or un contexte n'a qu'un seul usage : l'[[Interpretation]]. Il ne sert pas à ajouter de l'information, il sert à rendre l'information interprétable. @Bilal Koteich a consacré une thèse à recommander de la connaissance selon le contexte, ce qui est la version technique de cette phrase. Sans lui, le texte est là, mais il ne veut rien dire, et @Anna Gombin, qui a enseigné la littérature avant de faire du KM, sait mieux que personne ce qu'est un texte sans contexte.

Pour reprendre l'image du chimiste : le résultat est le précipité, le contexte est le solvant. Nous transmettons le précipité, sec, au fond du flacon, et nous nous étonnons que personne ne sache quoi en faire.

Ce qui réhabilite au passage votre lecteur distrait. Il n'est pas paresseux. Il a reçu un flacon sans étiquette, et il fait ce que ferait n'importe quel chimiste devant un flacon sans étiquette : il le repose.

# Deux fuites, un seul trou

Reste l'autre mode de transmission, l'oral, dont nous disions qu'il était imparfait lui aussi. Il l'est, mais la fuite n'est pas la même, et il vaut la peine de voir en quoi.

La mémoire humaine est une [[infrastructure]] de conservation, au même titre qu'une base de données, mais une [[infrastructure]] dont chacun sait qu'elle se dégrade. Pour dire cela plus précisément, empruntons une distinction que l'on fait d'ordinaire pour les modèles de langage. On appelle "connaissances paramétriques" le savoir qu'un modèle a appris pendant son entraînement : il est logé dans ses poids, on ne peut ni le lire ni le vérifier directement, on ne peut que constater ce qu'il en fait. On appelle "connaissance non-paramétriques" le savoir tenu à l'extérieur du modèle, dans un document ou une base, et consulté au moment de répondre. Il est lisible, vérifiable, et surtout il ne bouge pas.

Cette distinction s'applique très bien ici. Quand je vous explique de vive voix ce que j'ai fait, je réécris mon savoir dans vos poids. Vous en gardez une version, qui n'est pas la mienne, et qui s'érode. C'est exactement ce que nous disions plus haut : autrui oublie.

Mettons maintenant les deux fuites côte à côte. L'oral transporte l'[[intention]] (vous comprenez pourquoi j'ai fait cela) mais abîme le détail (vous ne retenez pas la [[clause]] exacte). L'artefact transporte le détail exact (la [[clause]] est là, mot pour mot) mais laisse l'[[intention]] derrière lui. Chacun perd la moitié que l'autre conserve. Choisir le moins mauvais des deux n'est donc pas une solution : il nous faudrait les deux moitiés. (@Cesar Miguel, qui a piloté le produit de 42, une école qui transmet sans professeurs, a sûrement une objection ici. Je la prends.)

> [!summary] Interlude
> Il y a deux façons de transmettre, et deux façons de perdre. Par oral, le savoir est réécrit dans la mémoire d'autrui, comme un savoir paramétrique : l'[[intention]] passe, le détail s'érode. Par artefact, le texte passe exactement, mais les quatre autres parties du contexte restent dans la [[session]] : le détail est là, l'[[intention]] manque. Les deux fuites sont complémentaires, ce qui veut dire qu'aucune des deux ne suffit.

## Aucun dosage ne rattrape une fuite

Le réflexe naturel, à ce stade, est de mieux doser. Un peu plus de contexte au départ, un peu moins d'itérations, et le problème sera réglé. Mais **cela ne marche pas**. Voyons pourquoi.

Un [[trade-off]] est une forme de dilemme, que l'on peut aussi décrire comme un problème d'optimisation dont on ne sort pas sans renoncer à quelque chose. Les économistes ont un mot pour cela : l'efficience au sens de Pareto. Une allocation est efficiente au sens de Pareto lorsqu'on ne peut plus améliorer la [[situation]] de l'un sans dégrader celle de l'autre. Ici, les deux « parties » sont le temps et les tokens. Quand nous passons de 30/70 à 70/30, nous améliorons les tokens en dégradant le temps. Nous nous déplaçons le long de la frontière. Nous ne la déplaçons pas.

Et il y a plus gênant. Notre budget de 100 a été calculé pour une personne et une conversation. Dès qu'un collègue doit réutiliser le résultat, il refait sa propre conversation, avec son propre budget de 100. Le compte n'était pas incomplet, il était faux : nous mesurions le coût d'une tâche qui, en réalité, sera refaite autant de fois qu'il y a de personnes. Un audit KM comme ceux de @Arnaud Goutagneux, ou un audit de maturité IA comme ceux de @Damien Aubail, n'est pas autre chose qu'une mesure de cette fuite.

Tant que le tube fuit, aucun dosage ne nous sauve. Il faut changer de tube.

## Le vase clos

La sortie est plus proche qu'on ne le croit.

Il existe une autre forme de contexte que la [[session]], et elle tient dans un fichier. Un [[agents.md]], par exemple, est un simple fichier [[Markdown]] posé dans un projet, qui donne ses [[instructions]] à un [[agent]] avant qu'il ne commence à travailler. Une [[session]] et un fichier [[agents.md]] sont deux formes du même contexte, mais de propriétés inverses. La [[session]] est impermanente, le fichier persiste. La [[session]] est attachée à moi, le fichier est lisible par n'importe qui. L'un fuit, l'autre tient. (@Hervé Klein, dont les programmes durent plus longtemps que les équipes et où la doctrine écrite est obligatoire, me dira si un fichier suffit vraiment à tenir.)

À partir de là, tout n'est qu'affaire de degré de formalisation. Un [[agents.md]] ou un [[system prompt]] gardent le contexte sous forme de prose : c'est le premier degré, lisible par tous, mais qu'il faut lire en entier. Un [[Knowledge graph]], ou plus précisément un [[context graph]], garde le contexte sous forme de relations : c'est le deuxième degré, et il [[change]] la façon dont on le reçoit, nous y revenons dans un instant. C'est le métier de @karim ounnoughi, @Akash Basia, @Laetitia Rémy et @Milena Jael Silva Morales, chacun dans une industrie différente, et chacun avec la même question : comment faire pour que le graphe survive à la mission. Le [[Model Context Protocol (MCP)]] garde le canal lui-même : sa définition tient en une phrase, fournir du contexte structuré à un modèle. Les outils MCP scopés de @Soufiane Aazizi en sont l'exemple le plus concret que je connaisse.

Dans les trois cas, le geste est le même : sortir le contexte de la conversation, où il meurt avec elle, pour le poser à l'extérieur, où il lui survit. Persister son contexte cesse d'être une bonne habitude personnelle pour devenir une [[infrastructure]]. Mettre l'IA dans le pipeline plutôt que dans le chat, comme le fait @Fares Daoud, c'est poser la question « où vit le contexte ? » avant même la première conversation.

Et voici ce qui [[change]] pour la transmission. Un contexte gardé sous forme de relations n'a pas besoin d'être lu du début à la fin. Celui qui le reçoit l'interroge. Reprenez l'exemple de la [[clause]] : au lieu de relire toute la conversation de votre collègue en devinant ce qu'il avait en tête, vous demandez au graphe pourquoi cette [[clause]], pour quel client, et vous obtenez la réponse. Recevoir une conversation, c'est hériter d'un monologue. Recevoir un graphe, c'est pouvoir poser sa propre question.

## Ce que coûte la deuxième fois

Refaisons le calcul, cette fois sur plusieurs usages.

Première exécution : 70 unités de temps, 30 de tokens, et le contexte est écrit quelque part au lieu d'être seulement prononcé. Deuxième exécution : 0 de temps, puisque le contexte existe déjà, et 30 de tokens. Troisième, identique. Sur *n* usages, le coût moyen est de 70/n + 30. Pour n = 1, cela fait 100. Pour n = 2, 65. Pour n = 10, 37. Et la courbe tend vers 30.

Ce *n* ne compte plus seulement mes propres reprises. Il compte les collègues. Chaque personne qui interroge le contexte au lieu de le reconstituer fait baisser la moyenne. Et le [[trade-off]] cesse d'en être un : au sens de Pareto, c'est cette fois une amélioration, puisque quelqu'un y gagne et que personne n'y perd. Le temps avait de toute façon été dépensé. La seule chose qui a changé, c'est que nous avons cessé de le jeter.

Nous pouvons donc réécrire la formule d'ouverture, qui était vraie mais solitaire. À l'échelle d'une [[session]] : plus vous investissez de temps dans votre contexte, moins vous dépensez de tokens. À l'échelle d'une organisation : plus vous persistez votre contexte, moins les autres ont à le redécouvrir.

Nous l'avions d'ailleurs déjà mesuré le [[2026-07-02 - Proving knowledge drives token efficiency|2 juillet]]. À modèle constant, la même tâche passait de 64 minutes de prompting à 10 minutes, avec une fidélité sémantique de 89 %. La variable n'était ni le modèle, ni l'effort de rédaction. C'était l'accès à un contexte déjà structuré, déjà là, déjà payé par quelqu'un d'autre. @Soufiane Aazizi a le même chiffre dans l'autre sens, un à deux jours ramenés à cinq minutes. Et @Lazlo Guiol, qui évalue des RAG en production avec des jurys de modèles, a la méthode pour contester mes 89 %. Qu'il le fasse.

> [!summary] Interlude
> Sur n usages, le coût moyen tombe à 70/n + 30 et tend vers 30. Comme n compte aussi les collègues, chaque personne qui interroge le contexte au lieu de le refaire fait baisser la moyenne. Le [[trade-off]] devient un gain de Pareto, et la formule d'ouverture [[change]] d'échelle : plus vous persistez votre contexte, moins les autres ont à le redécouvrir.

## Le cahier de laboratoire

Revenons une dernière fois à notre chimiste.

Ce qui l'a fait sortir du ridicule, historiquement, ce n'est pas une meilleure paillasse ni une main plus sûre. C'est le cahier de laboratoire. Un objet d'une banalité absolue, dans lequel on ne note pas la solution mais le protocole : ce qu'on a mis, dans quel ordre, pourquoi, et ce qu'on attendait. Sa seule fonction est de faire survivre ce protocole à l'expérience. Il ne rend pas la manipulation plus brillante. Il la rend refaisable, par un autre, plus tard, sans le chimiste. @Wissame Laddada, qui a modélisé de la connaissance de laboratoire pour de vrai avant d'en faire pour l'industrie, sait que ce n'est pas une métaphore. Et @Pierre Delort, qui a construit les cours [[data]] du Corps des Mines, sait ce que coûte de formaliser un savoir pour qu'il tienne sans son auteur.

Le protocole, c'est le contexte. Et un [[Knowledge graph]] ou tout autre forme de contexte, n'est rien d'autre qu'un cahier de laboratoire pour nos conversations.

Sinon nous continuerons à produire chaque jour de très belles solutions, à les porter fièrement jusqu'à nos collègues, et à les retrouver chaque soir répandues sur le sol de notre laboratoire. 

A toutes fins utiles, 
