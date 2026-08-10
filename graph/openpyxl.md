---
rdf:type: Research Note
title: openpyxl Limitations
description: Features silently lost when round-tripping xlsx files through openpyxl — shapes, slicers, macros, sparklines, comments.
tags:
  - openpyxl
  - python
  - library
  - xlsx
  - limitations
timestamp: 2026-06-28T00:00:00Z
instanceOf: "[[excel vs. gsheet problem]]"
broader: "[[Python]]"
inferred:skos:ancestor:
  - "[[Application development]]"
  - "[[Process]]"
  - "[[Programming language]]"
  - "[[Python]]"
---

## Features Lost on Round-Trip Through openpyxl

| [[feature]] | Status |
|---------|--------|
| Shapes (images, drawings) | Dropped on open/save |
| Slicers | Stripped |
| VBA [[macros]] | Silently wiped (use `keep_vba=True` + `.xlsm` to preserve) |
| Sparklines | No support — lost |
| Threaded comments | No support — likely dropped |
| Comment formatting and dimensions | Lost; comments not supported in `read_only` mode |
| Charts across sheets | May raise exceptions |
| Conditional formatting | Cannot validate [[rules]]; not supported in `write_only` mode |
| `.xls` format | Not supported (use `xlrd`) |
| `.xlsb` format | Not supported |

### Practical Impact

Any [[bijectivity]] tool using openpyxl inherits these limitations. Features that openpyxl drops are invisible to the sync pipeline — they can't be detected, preserved, or audited.

### gspread Limitations

The popular `gspread` [[Python]] wrapper adds convenience but:

- Does not handle formatting sync at all
- No support for merges, [[data]] validation, or conditional formatting
- Limited batch operation support
- Rate limiting must be handled manually

# Citations

[1] [openpyxl docs: Optimized Modes](https://openpyxl.readthedocs.io/en/stable/optimized.html)
[2] [pandas #44868: openpyxl loses features](https://github.com/pandas-dev/pandas/issues/44868)
[3] [gspread #659: Formatting support](https://github.com/burnash/gspread/issues/659)
