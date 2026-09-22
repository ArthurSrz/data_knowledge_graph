---
TypeOf: "[[index]]"
has part(s):
  - "[[graph/direction]]"
  - "[[graph/vector length]]"
subclass of: "[[vector]]"
instance of: "[[Geometric concept]]"
part of: "[[graph/Euclidean space]]"
skos:broader: "[[index]]"
inferred:skos:ancestor:
  - "[[Index]]"
  - "[[Vector]]"
inferred:skos:broader:
  - "[[Index]]"
  - "[[Vector]]"
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

