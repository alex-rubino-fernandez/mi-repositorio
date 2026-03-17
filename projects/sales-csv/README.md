Author: Alex Rubiño Fernández
Date: March 2026
Repository: mi-repositorio


# 📊 Sales Data Analysis Project

Complete analysis of a sales dataset using Python.
This project covers the entire cycle: exploration, cleaning, analysis and visualization.

## 📁 Project Structure
sales-csv/
├── data/
│ ├── sales-dataset.csv # Original data (1194 rows, 12 columns)
│ └── sales_dataset_cleaned.csv # Cleaned data with new features
├── code/
│ ├── 1-initial-exploration.py # Initial exploration
│ ├── 2-data-cleaning.py # Data cleaning and feature engineering
│ ├── 3-exploratory-analysis.py # Exploratory Data Analysis (EDA)
│ └── 4-insights-report.py # Final report with recommendations
├── outputs/
│ ├── charts/ # Generated charts
│ └── reports/ # Text reports
└── README.md


## 🎯 Objective

Get hands-on experience with real data analysis by applying:
- Data exploration and understanding
- Cleaning and preparation
- Statistical analysis and visualizations
- Business insights extraction

## 🔍 Dataset Overview

- **Rows**: 1,194 transactions
- **Original columns**: 12
- **Final columns**: 18 (after feature engineering)
- **Main variables**: Order ID, Amount, Profit, Quantity, CustomerName, State, City

## 🧹 Processes Performed

### 1. Initial Exploration
- Checked dimensions and data types
- Verified null values (✅ no nulls found)
- Identified numeric (3) and categorical (9) columns

### 2. Data Cleaning & Feature Engineering
- ✅ No duplicate records
- ✅ Converted dates to datetime format
- ✅ Outlier detection (10 in Profit, 0.8%)
- ✅ New columns created:
  - `Profit_Margin`: Profitability per sale
  - `Avg_Unit_Price`: Average unit price
  - `Year`, `Month`, `Month_Name`, `Quarter`: Time components

### 3. Exploratory Data Analysis (EDA)
- Numerical variables distributions
- Correlation matrix
- Top customers, states and cities
- Temporal analysis by month, quarter and year

## 📊 Key Findings

| Category | Result |
|-----------|-----------|
| **Total Sales** | $6.2M |
| **Total Profit** | $1.6M |
| **Average Margin** | 26% |
| **Total Orders** | 547 |
| **Average Order Value** | $11,336 |

**Top Customers:**
1. Cory Evans: $28,557
2. Nicholas Anderson: $27,352
3. Emily Ellison: $27,352

**Top States:**
1. New York: $1.13M
2. Florida: $1.09M
3. California: $1.08M

**Seasonality:**
- Best month: August ($5,509 average)
- Best quarter: Q2 (April-June)
- Sales peak: 2022 ($1.46M)

## 📈 Visualizations

All charts are saved in `outputs/charts/`:
- Distributions of Amount, Profit, Quantity, etc.
- Correlation heatmap
- Top customers and top states bar charts
- Monthly and quarterly trends

## 💡 Business Recommendations

1. **Retain** top 5 customers (they represent 12% of total sales)
2. **Expand** marketing in NY, FL and CA (50% of sales)
3. **Plan promotions** around August (peak) and January (lowest)
4. **Investigate** 2022 success factors to replicate
5. **Launch products** in Q2 (strongest quarter)

## 🛠️ Technologies Used

- Python 3.14
- pandas, numpy
- matplotlib, seaborn
- Git and GitHub
- VS Code

## 🚀 How to Run

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install pandas numpy matplotlib seaborn

