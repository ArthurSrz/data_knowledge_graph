---
has part(s):
  - "[[graph/direction]]"
  - "[[graph/vector length]]"
subclass of: "[[vector]]"
instance of: "[[geometric concept]]"
part of: "[[graph/Euclidean space]]"
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

