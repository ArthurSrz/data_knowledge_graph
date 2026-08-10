---
rdf:type: Research Note
title: Pivot Tables
description: Calculated fields produce different numerical results on each platform due to order-of-operations differences. Power Pivot has no Sheets equivalent.
tags:
  - pivot-tables
  - calculated-fields
  - power-pivot
  - excel
  - google-sheets
timestamp: 2026-06-28T00:00:00Z
instanceOf: "[[excel vs. gsheet problem]]"
broader: "[[spreadsheet]]"
inferred:skos:ancestor: "[[spreadsheet]]"
---

## Critical: Calculated Fields Produce Different Results

The same calculated field formula produces **different numerical results** on each platform. There is no setting to reconcile this.

| Platform | Order of Operations |
|----------|-------------------|
| **[[Excel]]** | Aggregates first, then calculates (sums columns, then applies formula) |
| **Google Sheets** | Calculates first, then aggregates (applies formula row-by-row, then sums) |

### Example

Given a calculated field `= Revenue / Units`:
- **[[Excel]]**: `SUM(Revenue) / SUM(Units)` = weighted average
- **Sheets**: `SUM(Revenue_i / Units_i)` = sum of per-row ratios

These are mathematically different operations. A pivot table that shows "Average Price" via a calculated field will show **different numbers** on each platform with no error or warning.

## Features Lost: [[Excel]] → Sheets

| [[feature]] | Status in Sheets |
|---------|-----------------|
| Calculated items | ✗ Not supported |
| Grouping by custom date periods | Limited |
| "Show values as" (% of grand total, running total, rank) | Partial |
| Multiple value field settings | Limited |
| Report filter pages | ✗ |
| Timeline slicers | ✗ (basic slicers only, added late) |
| Conditional formatting tied to pivot fields | ✗ |
| [[Power]] Pivot (DAX, multi-table models) | ✗ No equivalent |

## [[Power]] Pivot / [[Data Model]] Gap

[[Excel]] supports [[Power]] Pivot — multi-table joins via relationships, DAX formulas, and millions-of-rows [[data]] models. Google Sheets has **zero equivalent**. Pivot tables in Sheets operate on a single flat range only.

This is a fundamental architectural difference, not a missing [[feature]].

# Citations

[1] [Microsoft Q&A: Calculated field differences](https://learn.microsoft.com/en-us/answers/questions/5263257/same-formula-for-pivot-table-calculated-field-give)
[2] [Ben Collins: Slicers in Google Sheets](https://www.benlcollins.com/spreadsheets/slicers-in-google-sheets/)
