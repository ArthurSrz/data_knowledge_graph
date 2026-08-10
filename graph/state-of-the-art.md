---
rdf:type: Research Note
title: Round-Trip Fidelity — State of the Art
description: No academic literature or existing tool achieves full-fidelity Excel ↔ Google Sheets sync. The bijectivity project's approach.
tags:
  - round-trip
  - fidelity
  - bijectivity
  - sync
  - excel
  - google-sheets
timestamp: 2026-06-28T00:00:00Z
---

## No Academic Literature Exists

Web searches and paper databases surface **no peer-reviewed research** on spreadsheet interoperability or round-trip fidelity between Excel and Google Sheets.

Related work exists on:
- Spreadsheet error detection (e.g., Panko's research on spreadsheet errors)
- Format interoperability between ODF and OOXML (EU-funded studies)
- Data migration validation in database contexts

But nothing specifically on proving bijective fidelity between two live spreadsheet platforms.

## No Existing Tool Does Full-Fidelity Sync

| Tool | Syncs Values | Syncs Formulas | Syncs Formatting | Syncs Structure |
|------|-------------|----------------|-----------------|----------------|
| Sheetgo | ✓ | ✗ | ✗ | ✗ |
| Zapier | ✓ | ✗ | ✗ | ✗ |
| Celigo | ✓ | ✗ | ✗ | ✗ |
| gspread | ✓ | Partial | ✗ | ✗ |
| Google Drive (native export) | ✓ | ✓ (best-effort) | Partial | Partial |

All existing tools sync **data values only**. None attempt to preserve the full fidelity of formulas, formatting, merges, validation, and structure.

### Google Drive Native Export

Google's own "Download as .xlsx" does the best job but still loses:
- Apps Script / macros
- Sheets-only functions (→ `#NAME?`)
- Sparklines
- Some conditional formatting
- Iterative calculation settings

## The Bijectivity Approach

This project may be the **most rigorous open-source attempt** at proving round-trip fidelity. The approach is:

1. **Forward sync** (xlsx → Google Sheet): cell-by-cell with formula translation, style mapping, merge/validation sync
2. **Reverse sync** (Google Sheet → xlsx): reconstruct the workbook from the Sheets API
3. **Audit**: compare the original xlsx with the reverse-synced xlsx across 6 dimensions (values, formulas, styles, merges, validation, structure)

### What "Bijective" Means Here

A true mathematical bijection requires a 1:1 mapping in both directions. In practice, spreadsheet bijectivity is constrained by:

- **Expressiveness gaps**: features that exist in one platform but not the other
- **Semantic gaps**: same concept, different behavior (e.g., [calculated fields in pivot tables](/pivots/calculated-fields.md))
- **Silent coercion**: values that change without error (see [implicit type coercion](compatibility%201.md))
- **Metadata loss**: settings that don't transfer (see [iterative calculation](/engine/differences.md))

The audit's job is to **detect and report** these gaps, not eliminate them — some are fundamental to the platforms.

# Citations

[1] [Google Support: Compatibility with other editors](https://support.google.com/docs/thread/75690726)
[2] [gspread #659: Formatting support request](https://github.com/burnash/gspread/issues/659)
[3] [Celigo: Bidirectional sync with Sheets](https://www.celigo.com/blog/create-a-bidirectional-data-sync-with-google-sheets-templates/)
[4] [FasterCapital: Cross-platform Compatibility](https://fastercapital.com/content/Cross-platform-Compatibility--Working-Across-Devices--Excel-and-Google-Sheets--Cross-platform-Compatibility.html)
