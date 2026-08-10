---
exampleOf: "[[index]]"
usedIn: "[[Graph network analysis]]"
broader: "[[knowledge graph]]"
inferred:skos:ancestor: "[[knowledge graph]]"
---
Index computed between two nodes in a [[Network graph]] that predicts their probabilty to be linked. This measure is based on the instinct that if two nodes have common neighbors and that neighbors have themselves very large neighborhoods, then the connection between those two nodes is less likely than if the neighbor neighbordoods is limited. 

If A and B both follow Cristiano Ronaldo on Linkedin, it is not an insight that will reveal that A and B are connected because the neighborhood is VERY lare (many people follow Cristiano Ronaldo). But if A and B follow Anonymous X that only has 5 neighbors, they are more likely to be linked. 