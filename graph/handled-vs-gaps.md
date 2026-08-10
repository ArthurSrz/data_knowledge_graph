---
rdf:type: Research Note
title: Codebase Status — Handled vs Gaps
description: Maps each research category to what the bijectivity codebase already handles vs. known gaps that remain unaddressed.
tags:
  - status
  - implementation
  - gaps
  - bijectivity
  - roadmap
timestamp: 2026-06-28T00:00:00Z
instanceOf: "[[excel vs. gsheet problem]]"
broader: "[[spreadsheet]]"
inferred:skos:ancestor: "[[spreadsheet]]"
---

## Handled ✓

| Issue | Where | How |
|-------|-------|-----|
| XLOOKUP spill | `xlsx_to_gsheet.py:81-141` | Rewrites `XLOOKUP(MIN(ABS(...)))` to `INDEX/MATCH` |
| Locale separators (`;` vs `,`) | Both sync files | Detects locale, normalizes separators and decimals |
| Embedded newlines in formulas | `xlsx_to_gsheet.py:148-151` | Strips before sending to Sheets API |
| Array formula anchors | `xlsx_to_gsheet.py:212-243` | Detects anchor cells, lets non-anchors spill |
| API rate limits / batching | `xlsx_to_gsheet.py:26-65` | Splits into ≤5K cell / ≤1.5MB batches, SSL retry |
| Stale value orphaning | `xlsx_to_gsheet.py:515-526` | batchClear all sheets before every write |
| Phantom dimensions | Both sync files | Caps formatting to actual [[data]] extent |
| Text-to-number coercion | `xlsx_to_gsheet.py:249-256` | Escapes `+/-` strings with apostrophe prefix |
| Light font suppression | `xlsx_to_gsheet.py:790-800` | Suppresses light fonts when no dark background |
| Named range formula fallback | `xlsx_to_gsheet.py:306-316` | Falls back to cached values for formula-only names |
| Merged cell sync | `xlsx_to_gsheet.py:1075-1102` | Unmerge-all then reapply from source |
| [[data]] validation type [[mapping]] | `gsheet_to_xlsx.py:248-271` | Guesses whole vs decimal from values |
| Named ranges | `xlsx_to_gsheet.py` | Syncs to Sheets; cached fallback for formulas |
| [[data]] validation | Both sync files | Forward and reverse sync with type [[mapping]] |
| Frozen panes | Both sync files | Synced bidirectionally |
| Comments | Both sync files | Synced bidirectionally |

## Not Handled ✗

| Issue | Category | Difficulty | Notes |
|-------|----------|-----------|-------|
| Partial column ranges (`A4:A`) | Formulas | Hard | No [[Excel]] equivalent — needs translation strategy |
| Iterative calculation settings | Calc engine | Medium | [[Spreadsheet]]-level [[metadata]], not synced |
| Implicit type coercion | Formulas | Hard | Silent divergence, would need formula analysis |
| ARRAYFORMULA ↔ dynamic arrays | Formulas | Hard | Fundamental syntax incompatibility |
| Sheets-only [[functions]] (QUERY, etc.) | Formulas | N/A | No [[Excel]] equivalent exists |
| Sparklines | Formatting | N/A | Incompatible representations |
| Icon sets / [[data]] bars | Formatting | Medium | No Sheets equivalent |
| Checkboxes | Formatting | Medium | Become TRUE/FALSE text |
| VBA / Apps Script | [[macros]] | N/A | Different runtimes, out of scope |
| Pivot table calculated fields | Pivots | Hard | Different [[evaluation]] [[semantics]] |
| [[Power]] Pivot / [[data]] models | Pivots | N/A | No Sheets equivalent |
| Structured table references (`@`) | Tables | Medium | `#This Row` not supported in Sheets |
| Shapes / images | Formatting | Hard | [openpyxl drops on open/save](/api/openpyxl.md) |
| Slicers | Formatting | Hard | [openpyxl strips them](/api/openpyxl.md) |
| Print areas / page breaks | Formatting | Low | Not currently synced |
| Threaded comments | Structure | Medium | [[openpyxl]] doesn't support |

## [[classification]]

### Out of scope (no possible [[mapping]])
- [VBA / Apps Script](/scripting/macros.md)
- [Power Pivot / data models](/pivots/calculated-fields.md)
- Sheets-only [[functions]] with no [[Excel]] equivalent
- [Sparklines](/formatting/conditional-formatting.md) (incompatible representations)

### Could be addressed (translation possible)
- [Partial column ranges](compatibility%201.md) → bounded range with heuristic max row
- [Iterative calculation](/engine/differences.md) → sync as workbook setting
- [Checkboxes](/validation/rules.md) → [[data]] validation boolean
- Icon sets → alternative conditional formatting
- Print areas → sync via Sheets API [[properties]]
- [Structured references](/references/structured-references.md) → explicit cell references

### Requires formula analysis (hardest)
- Implicit type coercion detection
- ARRAYFORMULA translation
- [Calculated field semantic differences](/pivots/calculated-fields.md)
