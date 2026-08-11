# Azure End-to-End Data Pipeline

In this project, I've shared my work around implementing an end-to-end data engineering pipeline using Microsoft Azure Services. The pipeline has 7 steps:

1. **Raw data**: provided on GitHub
2. **Azure Data Factory (ADF)**: for pipeline orchestration
3. **Azure Data Lake Storage (ADL)**: to store raw data
4. **Azure Synapse Analytics**: for data warehousing purposes
5. **Databricks**: used for data transformation by PySpark
6. **Azure Data Lake Storage (ADL)**: to store transformed data
7. **Power BI**: for data visualization

## Architecture

```
GitHub (Raw CSVs)
    ↓
Azure Data Factory (ForEach + Copy Activity)
    ↓
ADLS Gen2 — Bronze Layer (Raw CSVs)
    ↓
Databricks (PySpark Transformation)
    ↓
ADLS Gen2 — Silver Layer (Cleaned CSVs)
    ↓
Azure Synapse Analytics (Serverless SQL Views)
    ↓
Power BI (Dashboards & Visualizations)
```

## Dataset

Tokyo 2020 Olympics dataset containing 5 CSV files:
- **Athletes** — 11,085 athletes with name, country, and discipline
- **Coaches** — coaches with name, country, discipline, and event
- **EntriesGender** — male/female participation counts per discipline
- **Medals** — medal counts (Gold, Silver, Bronze) per country
- **Teams** — team entries with discipline, country, and event

## Project Structure

```
├── data/                  # Raw CSV files (Bronze layer)
├── databricks/            # PySpark transformation notebook
├── synapse/               # SQL scripts for views
├── graphs/                # Power BI visualizations
└── README.md
```

## Tools & Technologies

- Azure Data Factory
- Azure Data Lake Storage Gen2
- Azure Databricks (PySpark)
- Azure Synapse Analytics (Serverless SQL Pool)
- Power BI
- GitHub
