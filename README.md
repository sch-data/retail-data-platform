# Retail Data Platform

## Project Overview

This project explores the 2009–2010 portion of the UCI Online Retail II dataset using Python. It currently includes data quality assessment, data cleaning, exploratory data analysis and data visualisation. Future versions will extend the project with SQL, dashboards, machine learning and data engineering features.

## Dataset

The project uses the 2009–2010 transaction data from the UCI Online Retail II dataset. The original dataset spans two years (2009–2011). The second year of data (2010–2011) will be used for later stages of the project to demonstrate automated data ingestion and pipeline processing.

## Repository Structure

```text
retail-data-platform/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   └── 01_data_exploration.ipynb
├── sql/
├── scripts/
├── .gitignore
├── README.md
└── requirements.txt
```

Additional SQL scripts, dashboards and pipeline components will be added as the project develops.

## Installation

```bash
git clone https://github.com/sch-data/retail-data-platform.git
cd retail-data-platform

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

## Current Progress

- Data quality assessment
- Data cleaning and preprocessing
- Exploratory data analysis
- Data visualisation

## Roadmap

Future development of the project will include:

- Build a relational database and analyse the cleaned dataset using SQL to answer business questions.
- Develop an interactive dashboard to communicate key sales metrics.
- Build an automated data processing pipeline.
- Extend the project with predictive modelling.
- Deploy the data pipeline using a cloud platform.

## Licence & Attribution

This project uses the Online Retail II dataset from the UCI Machine Learning Repository.

- Source: UCI Machine Learning Repository
- Dataset: [UCI Online Retail II](https://archive.ics.uci.edu/dataset/502/online+retail+ii)
- Creator: Dr Daqing Chen
- DOI: 10.24432/C5CG6D
- Licence: CC BY 4.0