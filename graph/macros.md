---
rdf:type: Research Note
title: Macros & Scripting
description: VBA and Apps Script are completely incompatible ecosystems with no reliable automated conversion path.
tags:
  - macros
  - vba
  - apps-script
  - scripting
  - excel
  - google-sheets
timestamp: 2026-06-28T00:00:00Z
instanceOf: "[[excel vs. gsheet problem]]"
broader: "[[Application development]]"
inferred:skos:ancestor:
  - "[[Application development]]"
  - "[[Process]]"
---

## The Core Problem

VBA and Apps Script are completely incompatible ecosystems. There is no automated conversion [[path]] that works reliably.

## [[Excel]] → Google Sheets

- **VBA macros are silently stripped** on import. No error, no warning — the file opens, the macros are gone.
- UserForms, ActiveX controls, COM [[add]]-ins: silently removed.
- [[Power]] Query and [[Power]] Pivot connections: no equivalent in Sheets.

### Google's Macro Converter

Google offers a [Macro Converter](https://developers.google.com/apps-script/guides/macro-converter/overview) [[add]]-on that attempts VBA → Apps Script translation. However:

- **Restricted to Enterprise Plus / Education Plus** customers
- Handles only partial conversion — complex VBA requires manual rewriting
- No support for UserForms, ActiveX, or COM
- Event handlers map imperfectly (Workbook_Open → onOpen, etc.)

## Google Sheets → [[Excel]]

- **Apps Script is completely lost** when exporting to `.xlsx`
- Custom menus, sidebar UIs, triggers, web apps: all gone
- onEdit/onChange triggers have no `.xlsx` equivalent
- Apps Script libraries and service connections: no [[mapping]]

## Implications for [[Bijectivity]]

Macro/script sync is out of scope for automated round-trip — the platforms use fundamentally different execution environments (V8 vs COM/VBA runtime). The [[best]] a sync tool can do is **detect and report** that macros/scripts exist, not preserve them.

# Citations

[1] [Google Developers: Macro Converter](https://developers.google.com/apps-script/guides/macro-converter/overview)
[2] [Google Community: VBA conversion](https://support.google.com/docs/thread/210876169)
