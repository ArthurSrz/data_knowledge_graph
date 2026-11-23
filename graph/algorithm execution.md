---
iso-thes:broaderGeneric: "[[process]]"
skos:altLabel:
  - "run"
  - "job execution"
skos:definition: "One occurrence of an algorithm being carried out on given inputs, in a given environment, with a start, an end and an outcome."
kg:uses: "[[algorithm]]"
properties for this type:
  - "inception"
  - "duration"
skos:scopeNote:
  - "Different from [[algorithm]]: the run is an occurrent, the algorithm an information content entity."
---
A run of an [[algorithm]]: an occurrent, with a start, a duration and an end state. Anything about running is a property of the run, not of the algorithm: success, failure, how long it took, whether it hit a limit.

**Three checks, three different claims.** In order:

1. **Liveness**: the system answers (a connection opens, a query returns). Says nothing about the outputs.
2. **Termination within contract**: the run ended `SUCCEEDED` under its limits. The success criterion belongs to the *context*. Example: a 1,800 s workflow timeout around a job that would accept 3,600 s. One out-of-memory restart and the run "fails" with the same algorithm.
3. **Plausibility of outputs**: compare with the previous run. A drift (e.g. −0.7 % scored voters, 376,432 → 373,742) can be normal, coming from the inputs, or a regression. Only this check touches what the algorithm produces.

A green status (`SUCCEEDED`) only proves checks 1 and 2. Watch the margin to the limit (here, the job step's duration against 1,800 s), not the total time.

**Example:** election scoring pipeline, run of 22/11/2026: succeeded in 31 min 53 s; Neo4j answers; 373,742 voters scored.
