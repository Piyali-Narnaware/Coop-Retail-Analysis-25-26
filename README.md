# Co-op Retail Analytics Dashboard

![Power BI](https://img.shields.io/badge/Power%20BI-dashboard-yellow)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![DAX](https://img.shields.io/badge/DAX-measures-orange)

A comprehensive retail analytics dashboard for the Co-operative retail organisation, analysing revenue performance, customer membership behaviour, category contribution, and store operations. Built with Power BI, DAX, and Python-powered data pipelines.

---

## Dashboard Pages

| Page | Focus | Key Metrics |
|------|-------|-------------|
| **Executive Overview** | High-level KPIs | Total Revenue, Total Units, Unique Customers, Avg Availability, Avg Basket Value |
| **Store Performance & Operations** | Store-level analysis | Revenue by store, Availability %, Operational efficiency |
| **Customer & Membership Insights** | Customer behaviour | Member vs Non-member revenue, Membership impact |

### Executive Overview
![Executive Overview](images/Executive-Overview.png)

### Store Performance & Operations
![Store Performance](images/Store-Performance-Operations.png)

### Customer & Membership Insights
![Customer Insights](images/Customer-Membership-Insights.png)

---

## Data Pipeline

```
┌──────────────────┐     ┌───────────────────┐     ┌──────────────────┐     ┌──────────────────┐
│  Raw Retail CSV  │────▶│  Python Cleaning  │────▶│  Cleaned Data    │────▶│  Power BI        │
│                  │     │  (pandas)         │     │  + Summary CSVs  │     │  Dashboard.pbix  │
│  Transactions    │     │  - Strip whitespc │     │                  │     │  DAX Measures    │
│  Stores          │     │  - Type convert   │     │  store_revenue   │     │  - Total Revenue │
│  Customers       │     │  - Remove invalid │     │  monthly_revenue │     │  - AOV           │
│  Categories      │     │  - Calc basket    │     │  category_summary│     │  - On-Time Del % │
└──────────────────┘     └───────────────────┘     └──────────────────┘     └──────────────────┘
```

### Data Cleaning (`data_cleaning.py`)

- Whitespace stripping and standardised text formatting
- Date conversion and validation
- Outlier detection and removal
- Invalid record filtering
- Basket value calculation per transaction

### Data Exploration (`data_exploration.py`)

- Revenue grouped by store, category, customer, member status
- Monthly revenue trend computation
- Product availability percentage analysis
- Exported summary CSVs for Power BI ingestion

---

## Key Insights

- **Revenue Segmentation** — Identified top-performing stores, categories, and customer segments
- **Customer Behaviour** — Member vs non-member revenue contribution patterns
- **Product Availability** — Correlation between stock availability and revenue by store/category
- **Temporal Trends** — Monthly revenue patterns revealed seasonal demand fluctuations

---

## Project Structure

```
├── coop_retail_dashboard.pbix          # Power BI dashboard file
├── data_cleaning.py                    # Python data preparation
├── data_exploration.py                 # Python exploratory analysis
├── scripts/
│   ├── script1.py                      # Additional analysis scripts
│   └── script2.py
├── images/                             # Dashboard screenshots
│   ├── Executive-Overview.png
│   ├── Store-Performance-Operations.png
│   └── Customer-Membership-Insights.png
├── data/                               # Raw datasets
│   ├── file1.csv
│   └── file2.csv
├── *_summary.csv                       # Pre-aggregated CSVs for dashboard
├── README.md
```

---

## Installation

```bash
git clone https://github.com/Piyali-Narnaware/Coop-Retail-Analysis-25-26.git
cd Coop-Retail-Analysis-25-26
pip install pandas numpy matplotlib seaborn
```

Run data preparation:

```bash
python data_cleaning.py
python data_exploration.py
```

Open `coop_retail_dashboard.pbix` in Power BI Desktop.

---

## Dependencies

- Microsoft Power BI Desktop
- Python 3.8+ (pandas, numpy, matplotlib)
- DAX (built into Power BI)
