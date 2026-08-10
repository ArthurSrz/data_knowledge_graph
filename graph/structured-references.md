---
rdf:type: Research Note
title: Structured Table References
description: Excel structured references (`Table1[@Column]`) vs Google Sheets table support — the critical `#This Row` gap.
tags:
  - structured-references
  - tables
  - this-row
  - excel
  - google-sheets
timestamp: 2026-06-28T00:00:00Z
instanceOf: "[[excel vs. gsheet problem]]"
broader: "[[spreadsheet]]"
inferred:skos:ancestor: "[[spreadsheet]]"
---

[[Excel]] has long supported structured references: `Table1[Column]`, `Table1[@Column]`, `Table1[#Headers]`.

Google Sheets added table/structured reference support in **late 2023**, but with significant gaps:

| [[feature]] | [[Excel]] | Google Sheets |
|---------|-------|---------------|
| `Table1[Column]` | ✓ | ✓ |
| `Table1[@Column]` (`#This Row`) | ✓ | ✗ **Not supported** |
| `Table1[#Headers]` | ✓ | Limited |
| `Table1[#Totals]` | ✓ | Limited |
| Use in conditional formatting | ✓ | ✗ |
| Use in charts | ✓ | ✗ |
| Use in pivot tables | ✓ | ✗ |
| Use with `INDIRECT` | ✓ | ✗ |
| Spaces in table names | ✓ | Converted to underscores |

## The `#This Row` Gap

`Table1[@Column]` (the "this row" specifier) is **critical** for row-level formulas inside tables — e.g., `=[@Revenue] / [@Units]`. This is one of [[Excel]]'s most-used table features, and it has no Sheets equivalent.

A formula like `=[@Price] * [@Quantity]` must be converted to explicit cell references (e.g., `=C2 * D2`) when syncing to Sheets, losing the semantic relationship to the table structure.

# Citations

[1] [Google Support: Tables in Sheets](https://support.google.com/docs/answer/15637642?hl=en)
[2] [Coefficient: Excel Table References in Sheets](https://coefficient.io/use-cases/excel-table-references-google-sheets-workarounds)
