---
rdf:type: Research Note
title: Formula Compatibility — Google Sheets vs Excel
description: Functions unique to each platform, array formula incompatibilities, and implicit type coercion differences.
tags:
  - formulas
  - compatibility
  - excel
  - google-sheets
  - array-formulas
timestamp: 2026-06-28T00:00:00Z
instanceOf: "[[excel vs. gsheet problem]]"
---

## Google Sheets-Only [[Functions]]

These [[functions]] produce `#NAME?` in [[Excel]] — there is no equivalent:

| Function | Purpose |
|----------|---------|
| `QUERY` | SQL-like [[queries]] on ranges |
| `ARRAYFORMULA` | Explicit array expansion wrapper |
| `IMPORTRANGE` | Pull [[data]] from another [[spreadsheet]] |
| `IMPORTHTML` | Import tables/lists from a web page |
| `IMPORTDATA` | Import CSV/TSV from a URL |
| `IMPORTXML` | Import [[data]] via XPath |
| `IMPORTFEED` | Import RSS/Atom feeds |
| `GOOGLEFINANCE` | Live stock/currency [[data]] |
| `GOOGLETRANSLATE` | Translate text between languages |
| `DETECTLANGUAGE` | Detect the language of a string |
| `SPARKLINE` | Inline mini-charts (formula-based) |
| `IMAGE` | Embed an image in a cell |
| `SORTN` | Top-N sort ([[Excel]] has no single equivalent) |
| `COUNTUNIQUE` | Count distinct values |
| `SPLIT` | Split text into columns |
| `JOIN` | Join array into a single string |
| `TO_DATE` / `TO_PERCENT` / `TO_DOLLARS` / `TO_TEXT` | Type coercion |
| `ADD`, `MINUS`, `MULTIPLY`, `DIVIDE` | Operator aliases |

34+ [[functions]] total have no [[Excel]] counterpart.

## [[Excel]]-Only [[Functions]]

| Function | Purpose |
|----------|---------|
| `STOCKHISTORY` | Historical stock [[data]] (linked [[data]] types) |
| `FIELDVALUE` | Extract fields from linked [[data]] types |
| [[Power]] Query / [[Power]] Pivot | No equivalent in Sheets at all |

`XLOOKUP`, `LAMBDA`, `LET` were added to Sheets in 2022–2023 but older spreadsheets may not recognize them.

## ARRAYFORMULA vs CSE vs Dynamic Arrays

This is the single biggest compatibility pain point:

- **Google Sheets**: uses `ARRAYFORMULA()` wrapper. Supports infinite ranges like `A:A`. The wrapper is explicit.
- **[[Excel]] (legacy)**: uses Ctrl+Shift+Enter (CSE) with `{}` braces. Cannot use whole-column ranges in CSE formulas.
- **[[Excel]] 365**: uses implicit spilling — no function marker at all. Results spill automatically from the anchor cell.

`ARRAYFORMULA()` produces `#NAME?` in [[Excel]]. [[Excel]]'s implicit spill has no explicit marker that Sheets can recognize. There is no lossless translation.

## Partial Column Ranges

Google Sheets supports **partial column ranges** like `A4:A` — [[meaning]] "from A4 down to the last row with [[data]]." [[Excel]] has **no equivalent syntax**:

- `A:A` — entire column (includes rows above A4)
- `A4:A1000` — explicit bound (breaks if [[data]] grows past row 1000)
- `A4:INDEX(A:A, COUNTA(A:A))` — dynamic workaround, fragile

A formula like `=SUM(B4:B)` in Sheets has no lossless [[Excel]] counterpart.

## Implicit Type Coercion

[[Excel]] automatically converts text-that-looks-like-a-number to a number inside nested function calls. Google Sheets does **not** consistently do this.

**Example**: `=MIN(255, MID(J4, ..., ...))` — `MID()` returns `"6"` (text). [[Excel]] implicitly converts to `6` → `MIN(255, 6) = 6` ✓. Sheets: text is not converted → unexpected result, **no error**.

This is arguably worse than a `#NAME?` error because it causes **silent wrong results**.

**Fix**: wrap with `VALUE()`: `MIN(255, VALUE(MID(...)))`

# Citations

[1] [OpenAsApp: Incompatible Functions](https://help.openasapp.com/incompatible-functions)
[2] [Ablebits: Google Sheets Functions Not in Excel](https://www.ablebits.com/office-addins-blog/google-sheets-functions-not-xl/)
[3] [Statology: ARRAYFORMULA vs Excel Arrays](https://www.statology.org/how-to-use-google-sheets-arrayformula-function-versus-excels-array-formulas/)
[4] [InfoInspired: Array Formula Differences](https://infoinspired.com/sheets-vs-excel-formula/array-formula-differs-in-google-sheets-and-excel/)
[5] [Stack Overflow #79518268](https://stackoverflow.com/questions/79518268/excel-vs-sheets-formula-substitution)
