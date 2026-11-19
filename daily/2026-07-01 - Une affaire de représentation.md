Quelle est la meilleure manière de représenter un réseau d'expert ? 

Je connais les graphes de co-citations (les travaux de Bruno Latour, *La vie de laboratoire*), inférés à partir des bibliographies des articles scientifiques. A prendre un peu de recul, ces graphes transforment une donnée structurée en une autre forme de données structurées. 

Je suppose que vue la taille des [[context]] windows, on peut mettre des interview toutes entières et faire du match-making aussi simplement qu'en faisant correspondre la requête à des bouts d'interviews...sans topic [[modeling]] ou quoi que ce soit. 

Mais comment avoir la preuve, et juger de ce qui est un bon ou un mauvais résultat ? Je suppose qu'il faudra néanmoins un petit pipeline, léger pour arriver à une [[conceptual modeling|modélisation]] sous la forme d'un tri-partite [[knowledge graph]] *Expert* <--> *Compétence* <--> *Document*, avec comme heuristique ([[heuristic]]) une requête two-[[graph hop]]. 

Pourquoi une requête two [[graph hop]] ? 

Considérons tous les cas possibles. Je fais une requête, le premier élément qui ressort est un Document, je fais deux sauts, et je récupère, la compétence associé et je peux remonter jusqu'à l'expert. Si je trouve un Expert, je peux faire two hops vers compétence et document. Et si je tombe sur compétence, il faut que je fasse un hop à droite et un hop à gauche. 

Une spécification suffisante ? 

Il faudra voir quel est le "what good looks like". 
