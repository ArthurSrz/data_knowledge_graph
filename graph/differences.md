---
rdf:type: Research Note
title: Calculation Engine Differences
description: Iterative calculation settings, partial column ranges, and evaluation order differences between Excel and Google Sheets.
tags:
  - calculation
  - circular-references
  - evaluation
  - excel
  - google-sheets
timestamp: 2026-06-28T00:00:00Z
instanceOf: "[[excel vs. gsheet problem]]"
---

## Iterative Calculation (Circular References)

When a formula references its own [[output]] — directly or through a chain — both platforms need "iterative calculation" to resolve the circular dependency.

| Aspect | Google Sheets | [[Excel]] |
|--------|---------------|-------|
| [[Default]] state | **Off** | **Off** (but easier to discover) |
| Enable via | File → Settings → Calculation → Iterative calculation | File → Options → Formulas → Enable iterative calculation |
| Max iterations | Configurable ([[default]] 50) | Configurable ([[default]] 100) |
| Convergence threshold | Configurable | Configurable ([[default]] 0.001) |

### The [[Bijectivity]] Problem

The iterative calculation setting is **[[spreadsheet]]-level [[metadata]]**. When a [[Google Sheet]] with iterative calculation enabled is exported to `.xlsx`:

1. The setting does **not** transfer
2. Formulas that depend on iteration produce `#CIRC!` errors or wrong values
3. There is no visible warning — the file opens, formulas evaluate, results are silently wrong

This is **silent [[metadata]] loss** — one of the hardest categories to detect.

### Self-Referencing Array Formulas

A common [[pattern]]: an array formula where row N depends on row N-1 (e.g., cumulative sums, running balances). In Sheets this requires iterative calculation enabled. [[Excel]] evaluates row-by-row more naturally within dynamic array spill ranges.

## Partial Column Ranges

Google Sheets supports open-ended ranges like `A4:A`. See also [Formula Compatibility](compatibility%201.md).

| Expression | Google Sheets | [[Excel]] |
|-----------|---------------|-------|
| `A4:A` | ✓ From A4 to last [[data]] row | ✗ Syntax error |
| `A:A` | ✓ Entire column | ✓ Entire column |
| `A4:A1000` | ✓ Fixed range | ✓ Fixed range |

`=SUM(B4:B)` automatically includes new rows added below B4. [[Excel]] has no equivalent — `B:B` includes rows 1–3 (which may contain headers or other [[data]]), and `B4:B1048576` is a fixed range to the theoretical max row.

## [[evaluation]] Order

Both platforms evaluate formulas in dependency order, but edge cases differ:

- **Volatile [[functions]]** (`NOW()`, `RAND()`, `TODAY()`): recalculate on every sheet change in both platforms, but Sheets throttles recalculation more aggressively in large sheets.
- **Cross-sheet dependencies**: both handle these, but API-driven updates in Sheets may not [[trigger]] recalculation of dependent formulas in other sheets within the same batchUpdate.

# Citations

[1] [Google Help: Iterative calculation](https://support.google.com/docs/answer/58515)
[2] [Microsoft: Change formula recalculation](https://support.microsoft.com/en-us/office/change-formula-recalculation-iteration-or-precision-in-excel-73fc7dac-91cf-4d36-86e8-67124f6bcce4)
