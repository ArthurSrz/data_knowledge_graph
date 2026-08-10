---
rdf:type: Research Note
title: Google Sheets API Quirks
description: Rate limits, atomic batchUpdate rollback, field mask traps, coercion pitfalls, and named range eventual-consistency issues.
tags:
  - sheets-api
  - google-api
  - rate-limits
  - batchUpdate
  - excel
  - google-sheets
timestamp: 2026-06-28T00:00:00Z
instanceOf: "[[excel vs. gsheet problem]]"
broader: "[[spreadsheet]]"
inferred:skos:ancestor: "[[spreadsheet]]"
---

## Rate Limits

| Limit | Value |
|-------|-------|
| Read requests | 300/min per project |
| Write requests | 300/min per project |
| Per-user limit | 60 requests/min |
| Recommended payload | ≤ 2 MB per request |
| Request timeout | 180 seconds |

## Behavioral Gotchas

- **Atomic batchUpdate**: if any sub-request in a batch fails, the **entire batch rolls back**. A single bad merge or formatting request can undo hundreds of valid changes.

- **Field masks with `*` wildcard**: can revert unspecified fields to their defaults. Always specify exact fields to update.

- **503 errors on complex spreadsheets**: large batchUpdate requests or spreadsheets with many formulas can [[trigger]] server-side timeouts.

- **USER_ENTERED mode coercion**: strings like `"+123"`, `"-456"`, or date-like strings are auto-converted to numbers or dates. Must escape with leading apostrophe.

- **SSL/TLS issues**: `SSLEOFError` can occur on large batch operations. Requires retry logic with exponential backoff.

- **Formula recalculation**: API-driven cell updates may not [[trigger]] recalculation of dependent formulas in other sheets within the same batchUpdate call.

- **Inter-batch eventual-[[consistency]] gap for named ranges**: Deleting named ranges in one `batchUpdate` and re-adding them in a subsequent call can fail with `"a named range with that name already exists"` — the second call is validated against a snapshot where the first batch's deletes have not yet propagated. Mitigation: always issue deletes and adds in the **same** atomic `batchUpdate`, with delete requests ordered before [[add]] requests.

- **`addDimensionGroup` union-expansion for overlapping ranges**: When a new `addDimensionGroup` request partially overlaps an existing group, the Sheets API silently expands the existing group to the union of both ranges instead of creating a second independent group. This causes row drift when adding section-level outline groups on top of row-level groups already synced from [[Excel]].

- **Percentage cells store raw decimal, not display value**: A cell formatted as percentage and displaying "40%" contains the raw value `0.40`. Conditional format formulas that compare against percentage cells must scale the raw value, e.g. `=B2*100<40` rather than `=B2<40`.

# Citations

[1] [Sheets API: Usage Limits](https://developers.google.com/workspace/sheets/api/limits)
