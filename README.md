# 🌍 Automated Cross-Border FX Settlement Pipeline

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)

## 📌 Executive Summary
Payment processors and digital lenders in emerging markets face massive currency volatility risk. When processing cross-border transactions (e.g., USD to NGN), real-time exchange rate fluctuations directly impact settlement payouts and gateway profit margins.

This project is an automated **ETL (Extract, Transform, Load)** data pipeline designed for the fintech sector. It programmatically ingests live macroeconomic API data, calculates exact merchant settlement values based on dynamic fiat spreads, and securely loads the finalized financial ledger into a local data warehouse.

## 🏗️ System Architecture
* **Extract:** Python securely connects to the `ExchangeRate-API` to ingest live fiat currency pairs (NGN, GBP, EUR, ZAR) against a USD base.
* **Transform:** Pandas is utilized to flatten JSON structures, apply a 1.5% payment gateway spread, and calculate real-time `Settlement_Amount_NGN` and `Gateway_Revenue_NGN` for a simulated batch of merchant transactions.
* **Load:** SQLAlchemy establishes a secure connection to a local `SQLite` relational database, appending the daily ledger as an immutable financial record.

## 📊 Sample Database Query Output
When queried via SQL, the pipeline successfully generates the following daily reconciliation report:

| Merchant_ID | Transaction_Amount (USD) | Live_NGN_Rate | Settlement_Amount_NGN | Gateway_Revenue_NGN |
|-------------|--------------------------|---------------|-----------------------|---------------------|
| M_004       | 5000.00                  | 1355.96       | 6,678,127.00          | 101,697.36          |
| M_002       | 1250.50                  | 1355.96       | 1,670,200.00          | 25,434.51           |

## 📂 Repository Structure
```text
fx-settlement-pipeline/
├── .env                    # (Gitignored) API Credentials
├── .gitignore              # Security rules
├── extractor.py            # API ingestion logic
├── transformer.py          # Settlement margin calculations
├── loader.py               # Database loading automation
├── query.py                # SQL validation script
├── settlement_warehouse.db # (Gitignored) Local database
└── README.md               # Project documentation