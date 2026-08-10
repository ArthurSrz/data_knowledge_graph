---
rdf:type: Research Note
title: Named Ranges
description: Scoping differences, ghost/orphaned ranges after tab deletion, and formula-only named ranges between Excel and Google Sheets.
tags:
  - named-ranges
  - scoping
  - ghost-ranges
  - excel
  - google-sheets
timestamp: 2026-06-28T00:00:00Z
instanceOf: "[[excel vs. gsheet problem]]"
broader: "[[spreadsheet]]"
inferred:skos:ancestor: "[[spreadsheet]]"
---

Named ranges are the **safest cross-platform bridge** — they translate cleanly between [[Excel]] and Google Sheets in most cases.

## Scoping Difference

- **[[Excel]]**: supports both workbook-scoped and **worksheet-scoped** named ranges. A name like `Total` can exist independently on Sheet1 and Sheet2.
- **Google Sheets API**: treats named ranges as **[[spreadsheet]]-global**. There is limited support for worksheet-scoped names.

This scoping difference can cause collisions when converting a workbook with same-named ranges on different sheets.

## Ghost / Orphaned Named Ranges After Tab Deletion

When a sheet tab is deleted (via `deleteSheet` in a `batchUpdate`), any named ranges that referenced that tab are not automatically deleted. These "ghost" ranges:

- No longer appear in the `namedRanges` list returned by `spreadsheets().get()` — they have no retrievable ID.
- Cannot be deleted via the API because their `namedRangeId` is unavailable.
- Still occupy the name in the [[spreadsheet]]'s internal namespace: a subsequent `addNamedRange` with the same name returns [[HTTP]] 400 `"already exists"`.

This is a Sheets API bug / undocumented behaviour. The only user-facing fix is manual removal via the Sheets UI under **[[data]] → Named ranges**.

## Formula-Only Named Ranges

Some [[Excel]] named ranges are defined by formulas (e.g., `=OFFSET(Sheet1!$A$1, 0, 0, COUNTA(Sheet1!$A:$A), 1)`). These dynamic named ranges:

- May not have a static cell reference to sync
- Can reference [[functions]] not available in Sheets
- The [[bijectivity]] codebase falls back to cached values for formula-only names

# Citations

[1] [ModelMonkey: Named Ranges in Sheets](https://modelmonkey.io/blog/named-ranges-google-sheets)
