---
rdf:type: Research Note
title: Limits & Performance
description: Cell counts, column limits, file sizes, and performance cliffs for Excel vs Google Sheets.
tags:
  - limits
  - performance
  - scalability
  - excel
  - google-sheets
timestamp: 2026-06-28T00:00:00Z
broader: "[[spreadsheet]]"
inferred:skos:ancestor: "[[spreadsheet]]"
---

## Platform Limits Comparison

| Dimension | Google Sheets | Excel Desktop |
|-----------|---------------|---------------|
| Total cells | 10 million per spreadsheet | ~17 billion (1M rows × 16K cols per sheet) |
| Max rows per sheet | 10,000,000 (across all sheets) | 1,048,576 per sheet |
| Max columns | 18,278 (ZZZ) | 16,384 (XFD) |
| Characters per cell | 50,000 | 32,767 |
| File size | ~100 MB import limit | 2 GB (32-bit), RAM-bound (64-bit) |
| Formula nesting | ~50–100 levels (undocumented) | 64 levels |
| IMPORT* formulas | 50 per spreadsheet | N/A |
| Sheets per workbook | 200 | Limited by memory |
| Conditional format rules | 500 per sheet (undocumented) | Limited by memory |

### Notable Asymmetries

- Sheets allows **more columns** (18,278 vs 16,384) — an Excel file using columns beyond XFD cannot round-trip
- Excel allows **more characters per cell** (32,767 vs 50,000 in Sheets) — but Sheets is more generous here
- Sheets has a **global cell limit** (10M across all sheets); Excel limits per-sheet but has no global cap

## Performance Cliffs

| Platform | Comfortable | Slow | Unusable |
|----------|------------|------|----------|
| Google Sheets | < 50K rows simple data | 50K–200K rows | > 200K rows or > 10K formula cells |
| Excel Desktop | < 500K rows | 500K–1M rows | > 1M rows or heavy Power Pivot |
| Excel Online | Similar to Sheets | Similar to Sheets | Similar to Sheets |

## Import/Export Size Limits

- Google Sheets import: ~100 MB for `.xlsx` files
- Google Drive upload: 5 TB (but Sheets conversion has its own limit)
- Sheets API: 2 MB recommended max per request payload
- openpyxl: memory-bound; very large files may require `read_only=True` mode

# Citations

[1] [Row Zero: Google Sheets Limits](https://rowzero.com/blog/google-sheets-limits)
[2] [Microsoft: Excel Specifications and Limits](https://support.microsoft.com/en-us/office/excel-specifications-and-limits-1672b34d-7043-467e-8e27-269d656771c3)
[3] [Zapier: Google Sheets Cell Limit](https://zapier.com/blog/google-sheets-cell-limit/)
