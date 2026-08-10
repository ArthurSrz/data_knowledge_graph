---
rdf:type: Research Note
title: Audit Implementation Notes
description: Floating-point tolerance, formula vs value comparison, and enhancement tab exclusion in the bijectivity audit.
tags:
  - audit
  - floating-point
  - tolerance
  - openpyxl
  - testing
timestamp: 2026-06-28T00:00:00Z
instanceOf: "[[excel vs. gsheet problem]]"
---

## Floating-Point Tolerance in Value Comparison

The Sheets API returns numeric values as [[JSON]] `number` (IEEE 754 double). [[openpyxl]] reads cell values from the OOXML `<v>` element (also IEEE 754 double, serialised as a string). Intermediate serialisation / deserialisation steps can introduce sub-epsilon rounding [[differences]].

Mitigation: use a relative tolerance of `1e-6` (i.e. `|a-b|/max(|a|,|b|) < 1e-6`) for numeric cells, with a fallback to string equality for non-numeric values.

## [[openpyxl]] `data_only=False` Returns Formula Strings, Not Computed Values

When [[openpyxl]] opens an xlsx file with `data_only=False` (the [[default]]), cells containing formulas return the formula string (e.g. `"=SUM(A1:A10)"`), not the last-calculated value. The last-calculated value is only available with `data_only=True`, which in turn makes non-formula cells return `None` if the file was never opened and saved in [[Excel]].

Mitigation: skip value comparison for any `xl_val` that is a string starting with `"="`. For a stricter audit, open the pulled xlsx with `data_only=True`; be aware that cells never calculated by [[Excel]] will then read as `None`.

## Enhancement Tabs Excluded from [[Bijectivity]] Inventory

The tabs `{"📋 Index", "📊 Dashboard"}` are created by `enhance_gsheet.py` and have no counterpart in the source xlsx. Both the forward-[[bijectivity]] [[test]] and the reverse-[[bijectivity]] [[test]] subtract this set from the tab inventory before asserting equality.

This set is defined as `ENHANCEMENT_TABS` in each [[test]] file. If new enhancement-only tabs are added, `ENHANCEMENT_TABS` must be updated in both [[test]] files or tab-count assertions will fail.
