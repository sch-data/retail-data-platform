# Retail Data Platform

## Project Overview

This project explores the UCI Online Retail II dataset using Python. It currently includes data quality assessment, reusable data cleaning and feature engineering scripts, exploratory data analysis, data visualisation, a PostgreSQL relational database and SQL analysis. Future versions will extend the project with dashboards, machine learning and data engineering features.

## Roadmap

This project is being developed in stages to demonstrate data analysis, data engineering and machine learning skills using a single real-world dataset.

| Version | Status | Focus |
|---------|--------|-------|
| V1 | ✅ Complete | Data cleaning, exploratory data analysis and visualisation |
| V2 | ✅ Complete | Reusable Python data processing pipeline |
| V3 | ✅ Complete | PostgreSQL database and SQL analysis |
| V4 | 🚧 In Progress | Interactive dashboard |
| V5 | ⏳ Planned | Machine learning and customer analytics |
| V6 | ⏳ Planned | Automated ETL pipeline |
| V7 | ⏳ Planned | Cloud deployment |

## Dataset

The current version of the project uses the 2009–2010 transaction data from the UCI Online Retail II dataset. The original dataset spans two years (2009–2011). The second year of data (2010–2011) will be used for later stages of the project to demonstrate automated data ingestion and pipeline processing.

Download the dataset from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/502/online+retail+ii) and place `online_retail_II.xlsx` in:

`data/raw/online_retail/`

## Repository Structure

```text
retail-data-platform/
├── assets/
│   ├── monthly_revenue_trend.png
│   └── top_countries_excluding_uk.png
├── data/
│   ├── raw/
│   │   └── online_retail/
│   └── processed/
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   └── 02_sales_analysis.ipynb
├── scripts/
│   ├── clean_data.py
│   ├── create_features.py
│   └── load_to_postgres.py
├── sql/
│   ├── analysis_queries.sql
│   └── schema.sql
├── .gitignore
├── README.md
└── requirements.txt
```

## Installation

1. Clone the Repository

```bash
git clone https://github.com/sch-data/retail-data-platform.git
cd retail-data-platform
```
2. Create a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate #Linux/MacOS
```
3. Install Dependencies

```bash
pip install -r requirements.txt
```
4. Run the data processing scripts:

```bash
python scripts/clean_data.py
python scripts/create_features.py
```

5. Create and populate the PostgreSQL database

```bash
createdb retail_data
psql retail_data < sql/schema.sql
python scripts/load_to_postgres.py
```

6. Run the SQL analysis

```bash
psql retail_data -f sql/analysis_queries.sql
```

## PostgreSQL Database

The cleaned transaction data is loaded into a relational PostgreSQL database with three tables:

- `products` — product information
- `invoices` — invoice-level information
- `invoice_items` — individual transaction lines linking invoices and products

```text
Raw Excel data
      ↓
Python cleaning
      ↓
Cleaned CSV
      ↓
PostgreSQL database
      ↓
SQL analysis
```

SQL queries analyse overall and monthly sales, product and country performance, top customers, and month-over-month revenue change.

## Example visualisations

### Monthly Revenue Trend

![Monthly Revenue Trend](assets/monthly_revenue_trend.png)

### Top 10 Countries by Revenue (Excluding UK)

![Top 10 Countries](assets/top_countries_excluding_uk.png)

## Key Findings

- December 2010 contained only the first nine days of transactions and was excluded from monthly trend analysis.
- Duplicate records, cancelled or returned transactions, and three bad debt adjustment records were identified and removed during data cleaning.
- Revenue increased substantially between September and November 2010, indicating strong seasonal demand ahead of the holiday period.
- The United Kingdom generated the vast majority of total revenue, with the Republic of Ireland and the Netherlands as the largest international markets.
- Most orders were of relatively low value, with only a small number of exceptionally large orders.

## Licence & Attribution

This project uses the Online Retail II dataset from the UCI Machine Learning Repository.

- Source: UCI Machine Learning Repository
- Dataset: [UCI Online Retail II](https://archive.ics.uci.edu/dataset/502/online+retail+ii)
- Creator: Dr Daqing Chen
- DOI: 10.24432/C5CG6D
- Licence: CC BY 4.0