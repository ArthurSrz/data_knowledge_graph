---
rdf:type: Research Note
title: Data Validation Differences
description: Error handling modes, validation type granularity, checkbox behavior, and dropdown list differences between Excel and Google Sheets.
tags:
  - data-validation
  - checkboxes
  - dropdowns
  - excel
  - google-sheets
timestamp: 2026-06-28T00:00:00Z
instanceOf: "[[excel vs. gsheet problem]]"
---

## Error Handling Modes

| Mode | [[Excel]] | Google Sheets |
|------|-------|---------------|
| Stop (reject input) | ✓ | ✓ ("Reject input") |
| Warning (allow with warning) | ✓ | ✓ ("Show warning") |
| Information (allow with info) | ✓ | ✗ |

[[Excel]]'s three-tier system (Stop / Warning / Information) maps to only two options in Sheets. The "Information" mode — which accepts the value but shows an info icon — has no Sheets equivalent.

## Validation Type Granularity

| Type | [[Excel]] | Google Sheets |
|------|-------|---------------|
| Whole number | ✓ (distinct type) | ✗ (NUMBER_BETWEEN, must infer) |
| Decimal | ✓ (distinct type) | ✓ (NUMBER_BETWEEN) |
| List (dropdown) | ✓ | ✓ |
| Date | ✓ | ✓ |
| Time | ✓ (distinct type) | ✗ (no TIME validation) |
| Text length | ✓ | ✓ (TEXT_CONTAINS etc.) |
| Custom formula | ✓ | ✓ |
| Checkbox | ✓ (as boolean DV) | ✓ (native checkbox) |

The Sheets API `NUMBER_BETWEEN` doesn't distinguish whole vs. decimal — a reverse sync must guess from the actual values whether to use [[Excel]]'s "Whole number" or "Decimal" type.

## Checkbox Behavior

- **Google Sheets**: native checkbox UI element, stored as a [[data]] validation rule with `BOOLEAN` type
- **[[Excel]]**: checkboxes exist but are form controls or ActiveX objects, not [[data]] validation
- **On export**: Sheets checkboxes become plain `TRUE`/`FALSE` text in [[Excel]]

## Dropdown Lists

- Basic in-cell dropdowns work on both platforms
- **[[Cross-sheet source references]]** can break during conversion — Sheets allows `Sheet2!A1:A10` as a list source, but the reference format may not survive round-trip if sheet names change or contain special characters

# Citations

[1] [Statology: Data Validation Comparison](https://www.statology.org/how-to-use-google-sheets-data-validation-versus-excels-data-validation/)
