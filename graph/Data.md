---
relatedTo: "[[Data science team]]"
fundamentalTo: "[[machine learning projects]]"
enables: "[[Supervised learning]]"
transforms: "[[feature]]"
ParentChild: "[[Datum]]"
skos:narrower: "[[data object]]"
broader: "[[Process]]"
inferred:skos:ancestor: "[[Process]]"
inferred:skos:narrower:
  - "[[Data catalog]]"
  - "[[Data lineage]]"
  - "[[Data mapping]]"
  - "[[Data model]]"
  - "[[Data quality]]"
  - "[[Data quantity]]"
  - "[[Data silos]]"
  - "[[Datum]]"
  - "[[collecting data]]"
  - "[[data type]]"
  - "[[index]]"
  - "[[metadata]]"
  - "[[open data]]"
  - "[[raw data]]"
---

# Data

Data is the fundamental building block of all [[machine learning systems]]. It represents the [[observations]], measurements, and facts collected from the real world that machines use to learn patterns and make predictions.

## Types of Data

### [[Structured Data]]
- Organized in rows and columns (tabular format)
- Examples: spreadsheets, SQL databases
- Easy to [[search]] and analyze

### [[Unstructured Data]]
- No predefined format or organization
- Examples: text documents, images, videos, audio
- Requires preprocessing before analysis

### [[Semi-structured Data]]
- Contains tags or markers to separate elements
- Examples: [[JSON]], [[XML]], emails
- Offers flexibility with some organization

## [[Data Quality]] Dimensions

1. **[[Accuracy]]**: How closely data values match the true values
2. **[[Completeness]]**: Presence of all required data elements
3. **[[consistency]]**: Uniformity across different [[datasets]]
4. **Timeliness**: Data is current and up-to-date
5. **Validity**: Data conforms to defined business [[rules]]
6. **Uniqueness**: No unwanted duplicates

## Data Lifecycle

1. Collection/[[Generation]]
2. Storage/[[Management]]
3. Processing/Transformation
4. Analysis/[[modeling]]
5. Visualization/Reporting
6. Archival/Disposal

## Challenges

- **[[Data Drift]]**: Changes in data distribution over time
- **Data [[bias]]**: Systematic distortions in data collection
- **[[Data Privacy]]**: Protecting [[sensitive information]]
- **Data Volume**: Managing large-scale [[datasets]]

See also: [[Data preparation]], [[Data quality]], [[Data privacy]], [[Data collection]]
