---
has part:
  - "[[graph/direction]]"
  - "[[graph/vector length]]"
iso-thes:broaderGeneric: "[[vector]]"
iso-thes:broaderInstantial: "[[geometric concept]]"
iso-thes:broaderPartitive: "[[graph/Euclidean space]]"
skos:broader: "[[index]]"
---
An [[index]] made of [[Vectors]]. Can be queried in [[CYPHER]] language.

### Vanilla [[query]] to create [[index]] 

```
CREATE VECTOR INDEX chunkEmbedding IF NOT EXISTS
FOR (n:Chunk)
ON n.embedding
OPTIONS {indexConfig: {
 `vector.dimensions`: 1536,
 `vector.similarity_function`: 'cosine'
}};
```

