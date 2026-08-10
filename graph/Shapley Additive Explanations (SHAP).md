---
broader: "[[Interpretability]]"
inferred:skos:ancestor: "[[Interpretability]]"
---
Le mode de fonctionnement de SHAP est de **décomposer le résultat d’un modèle par les sommes de l’impact de chaque caractéristique**. SHAP calcule une valeur qui représente la contribution de chaque caractéristique au résultat du modèle. Ces valeurs peuvent être utilisées pour comprendre l’importance de chaque caractéristique et expliquer le résultat du modèle à un humain. Ceci apporte notamment une valeur ajoutée aux agences et aux équipes qui rendent des comptes à leurs clients ou leurs managers.

SHAP possède plusieurs propriétés intéressantes, comme sa **neutralité** vis-à-vis des modèles. **Cela lui permet d’être utilisé sur n’importe quel modèle d’apprentissage**, de produire des explications cohérentes et de gérer les comportements complexes des modèles (lorsque les caractéristiques interagissent entre elles, par exemple).

### Pourquoi SHAP est-il utile ?

SHAP comporte de nombreuses utilités pour les professionnels de la Data Science. Tout d’abord, cette technique permet d’expliquer les prédictions des modèles de [Machine Learning](https://datascientest.com/machine-learning-tout-savoir) de manière compréhensible aux humains. **Grâce à l’attribution d’une valeur à chaque caractéristique entrée, il montre comment et dans quelle mesure chaque caractéristique a contribué au résultat final de la prédiction**. Ainsi, l’équipe peut comprendre comment le modèle a pris sa décision et peut identifier les caractéristiques les plus importantes.

Comme expliqué précédemment, ce modèle est dit agnostique (neutre). Il peut être utilisé avec n’importe quel modèle de Machine Learning. Vous n’avez donc pas à vous soucier de la structure du modèle pour comprendre le résultat de la **prédiction avec SHAP**. En plus, ce modèle est cohérent. Vous pouvez donc faire confiance aux explications produites, peu importe le modèle étudié.

Enfin, SHAP est particulièrement utile pour **gérer des comportements complexes**. Vous pouvez utiliser cette technique pour comprendre comment différentes caractéristiques affectent ensemble la prédiction du modèle.