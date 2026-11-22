---
iso-thes:broaderInstantial: "[[Data modeling technique]]"
---
Modeling technique involves structuring data into the shape of a star, aptly named the [star schema](https://en.wikipedia.org/wiki/Star_schema), which is simple to visualise and easily understood by non-data technical business users.

This process involves making tables that represent known business details and activities.

- Measurements such as ‘how much’ or ‘how many’ are placed in central **fact tables**.
- Information like ‘who, what, when, and where’ is put into related **dimension tables**.


## Cheatsheet

1. A great fact table is aligned with business transaction that created them, at the lowest possible grain
2. A great fact table is also at a low enough grain so you can make use of as many common dimension tables as possibles