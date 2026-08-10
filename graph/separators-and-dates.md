---
rdf:type: Research Note
title: Locale & Language Issues
description: Formula argument separators, translated function names, and date handling differences between Excel and Google Sheets.
tags:
  - locale
  - i18n
  - separators
  - dates
  - function-names
  - excel
  - google-sheets
timestamp: 2026-06-28T00:00:00Z
instanceOf: "[[excel vs. gsheet problem]]"
broader: "[[spreadsheet]]"
inferred:skos:ancestor: "[[spreadsheet]]"
---

## Formula Argument Separators

| Locale | Argument Separator | Decimal Separator |
|--------|-------------------|-------------------|
| en_US, en_GB | `,` (comma) | `.` (period) |
| fr_FR, de_DE, es_ES, etc. | `;` (semicolon) | `,` (comma) |

### How Each Platform Handles This

- **[[Excel]]**: stores formulas with locale-specific separators in the UI, but the `.xlsx` [[XML]] format uses **English function names and commas** internally.
- **Google Sheets UI**: shows locale-specific separators based on the [[spreadsheet]]'s locale setting.
- **Sheets API**: always accepts and returns **US-locale syntax** (commas as separators, periods as decimals).

### Implications for [[Bijectivity]]

The API normalization is favorable: both [[openpyxl]] (reading `.xlsx` [[XML]]) and the Sheets API use English/comma syntax. The translation [[layer]] doesn't need to handle locale conversion.

However, **embedded newlines** in formulas are a problem: [[Excel]] allows them (for readability in long formulas), but Sheets does not. These must be stripped before sending to the Sheets API.

## Translated Function Names

[[Excel]] translates function names per locale:

| English | French | German |
|---------|--------|--------|
| VLOOKUP | RECHERCHEV | SVERWEIS |
| IF | SI | WENN |
| SUM | SOMME | SUMME |
| AVERAGE | MOYENNE | MITTELWERT |
| COUNTIF | NB.SI | ZÄHLENWENN |

The `.xlsx` format stores **canonical English names** internally, regardless of display locale. Google Sheets always uses English names in the API. This simplifies the [[bijectivity]] problem.

## Date Handling

Both platforms store dates as serial numbers (1900 epoch, with the intentional Lotus 1-2-3 bug treating 1900 as a leap year). Display is locale-dependent.

For round-trip safety: use `UNFORMATTED_VALUE` when reading from the Sheets API to get raw serial numbers, avoiding locale-dependent date [[parsing]].

### Known Date Bug

Both [[Excel]] and Sheets inherit the **1900 leap year bug** from Lotus 1-2-3: February 29, 1900 is treated as valid (it wasn't). Serial number 60 maps to this phantom date. Both platforms agree on this bug, so it's not a conversion issue.

# Citations

[1] [xtractor.app: Commas vs Semicolons](https://xtractor.app/commas-vs-semicolons-in-google-sheets-formulas-a-locale-based-parse-error/)
[2] [Ben Collins: Sheets Location Settings](https://www.benlcollins.com/spreadsheets/sheets-location/)
[3] [excel-translator.de](https://en.excel-translator.de/vlookup/)
[4] [PerfectXL: French-English Translations](https://www.perfectxl.com/academy/functions/translations/french-english/)
