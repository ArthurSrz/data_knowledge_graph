---
iso-thes:broaderGeneric: "[[information content entity]]"
skos:definition: "A finite, written specification of steps that turns inputs into outputs; an information content entity, not the running of it."
skos:scopeNote:
  - "Different from [[algorithm execution]]: the algorithm is a continuant, each run is a process."
---
An algorithm is an [[information content entity]]: a [[generically dependent continuant]] that stays the same whatever happens when it is run. Its *runs* are a different kind of thing, an [[algorithm execution]] (a [[process]]).

What this distinction changes in practice (learned checking the election scoring pipeline, 2026-11-23):

- **"Is it working?" is never a question about the algorithm.** It asks about its executions: state, duration, whether they ended within their contract. The algorithm itself can neither be "up" nor "down".
- **Same algorithm, different outputs.** Output = algorithm × state of the input data at the time of the run. Between two runs of the same score v3 code (16/11 → 22/11/2026), the number of scored voters went from 376,432 to 373,742. A deterministic algorithm does not give a stable output; the drift comes from the inputs.
- **A failed run does not falsify the algorithm.** The 15/11 and 16/11 failures came from the orchestrator's 1,800 s timeout, a property of the execution context, not of the algorithm.

See [[algorithm execution]] for the checks this calls for.
