Dans le numéro précédent, il a été avancé qu’à représenter la connaissance sous la forme de chaînes d’activation on développait une intelligence sur l’intelligence. Soit une intelligence au carré. 

Je ne m’étendrai pas ici sur les moyens de développer ces chaînes d’activation à grande échelle. Si vous êtes curieux, je vous renvoie plutôt vers une [chouette](clarifeye.ai) née pour remplir cette fonction. À la place, je vais plutôt m’intéresser à démontrer que l’on peut effectivement conduire (steer) un modèle de langage avec une chaîne d’activation. 

> [!info] Chaîne d’activation et *[[Knowledge]] line*
> 
> J’ai utilisé jusqu’à présent les termes de chaînes d’activation et de *[[Knowledge]] line* indistinctement. C’est une erreur que je corrige. 
> Une [[knowledge]] line désigne le chemin que l’on dessine dans notre esprit pour exercer notre savoir faire, sur lequel sont positionnés des points intermédiaires : les artefacts. La chaîne d’activation, pour sa part, désigne la suite d’opérations déclenchée par la *[[knowledge]] line* (un graphe en réalité) **en dehors de notre esprit** : les outils auxquels nous faisons appels, les personnes avec lesquelles nous collaborons, etc. 

## Ce que veut dire conduire un modèle de langage 

Conduire un modèle de langage se distingue de toute technique de [[retrieval augmented generation]] ou d'ingénierie de contexte. Il s'agit de littéralement influer sur ce qui se trouve **à l'intérieur du modèle** pour le mener avec une quasi-certitude d'un point A à un point B. Un RAG ou toute ingénierie de contexte influe sur ce qui se passe **à l'extérieur du modèle**, c'est-à-dire au niveau de la complétion. 

Alors, comment est-ce qu'on conduit un LLM ?

Je vais prendre ici comme cadre de démonstration un prompt très simple, choisi parce qu'il va permettre de vérifier facilement si quand "je tourne les roues du modèle", il change bien de "direction" (le langage choisi ici est bien évidemment illustratif) : 

> [!example] Prompt 
> A round square is made of

Le prompt comporte deux éléments contradictoires : un carré et un rond. Si mes hypothèses ont du sens, je vais pouvoir trouver dans la chaine d'activation du langage des neurones relatifs au rond et des neurones relatifs au carré. Et si je peux effectivement conduire le modèle, je devrai pouvoir stimuler ou inhiber les parties relatives au carré ou au cercle
