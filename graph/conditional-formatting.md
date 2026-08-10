---
rdf:type: Research Note
title: Formatting & Styles
description: Conditional formatting, theme colors, fonts, charts, and sparklines — what converts and what is lost.
tags:
  - formatting
  - styles
  - conditional-formatting
  - charts
  - sparklines
  - excel
  - google-sheets
timestamp: 2026-06-28T00:00:00Z
instanceOf: "[[excel vs. gsheet problem]]"
broader: "[[spreadsheet]]"
inferred:skos:ancestor: "[[spreadsheet]]"
---

## Conditional Formatting

| [[feature]] | [[Excel]] | Google Sheets | Converts? |
|---------|-------|---------------|-----------|
| Highlight cell [[rules]] | ✓ | ✓ | Partially — formula references may shift |
| Top/Bottom [[rules]] | ✓ | ✓ | Partially |
| [[data]] bars | ✓ | ✗ | No — silently dropped |
| Icon sets | ✓ | ✗ | No — silently dropped |
| Color scales | ✓ | ✓ | Partially — theme colors shift |
| Custom formula [[rules]] | ✓ | ✓ | Partially — cell references don't always remap correctly |

Rule execution order and precedence differ between platforms. The "stop if true" logic in [[Excel]] has no direct equivalent in Sheets.

## Theme Colors

[[Excel]] uses a [[theme color]] system with tint/shade modifiers. Google Sheets has a simpler color [[model]]. When converting:

- Theme-referenced colors change unpredictably
- Tinted colors (e.g., "Accent 1, Lighter 40%") become fixed RGB values
- Round-trip loses the theme reference — the color value may survive but it's no longer theme-linked

## Fonts

- Platform-specific fonts (Calibri on Windows, Arial on Sheets) cause substitution
- Font rendering [[differences]] change column widths and row heights
- Vertical alignment may shift

## Charts

| [[feature]] | Converts? |
|---------|-----------|
| Basic charts (bar, line, pie) | Mostly yes |
| 3D effects, shadows | Lost |
| Custom [[data]] labels | Lost or simplified |
| Secondary axes | May not transfer |
| Advanced formatting | Lost |

## Sparklines

**Fundamentally incompatible.** No conversion in either direction.

- **Google Sheets**: `=SPARKLINE(data, options)` — a formula in a cell
- **[[Excel]]**: Ribbon-inserted [[sparkline]] objects stored as sheet-level [[metadata]]

There is no [[mapping]] between these representations.

# Citations

[1] [Numerous.ai: Convert Without Losing Formatting](https://numerous.ai/blog/how-to-convert-google-sheets-to-excel-without-losing-formatting)
[2] [GPTforWork: Excel to Sheets Formatting](https://gptforwork.com/blog/how-to-convert-excel-to-google-sheets-without-losing-formatting)
[3] [Latenode: Conditional Formatting Issues](https://community.latenode.com/t/conditional-formatting-issues-when-converting-excel-to-google-sheets/23289)
