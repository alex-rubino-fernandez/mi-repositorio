"""
Sales Data Analysis - Insights Report
Objective: Summarize key findings and generate final insights
Questions to answer:
1. What are the most important metrics?
2. Who are the best customers?
3. Where are the best markets?
4. When is the best time for sales?
5. What recommendations can we make?
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from datetime import datetime


# CONFIGURATION

script_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(script_dir)
data_path = os.path.join(project_dir, "data", "sales_dataset_cleaned.csv")
charts_path = os.path.join(project_dir, "outputs", "charts")
reports_path = os.path.join(project_dir, "outputs", "reports")

os.makedirs(reports_path, exist_ok=True)

# Load data
sales = pd.read_csv(data_path)
print(f"\n Loaded data: {sales.shape[0]} rows, {sales.shape[1]} columns")

# Key metrics

total_sales = sales['Amount'].sum()
total_profit = sales['Profit'].sum()
avg_margin = (sales['Profit'].sum() / sales['Amount'].sum() * 100).round(2)
total_orders = sales['Order ID'].nunique()
avg_order_value = (total_sales / total_orders).round(2)

print(f"\n Total Sales: ${total_sales:,.2f}")
print(f" Total Profit: ${total_profit:,.2f}")
print(f" Average Margin: {avg_margin}%")
print(f" Total Orders: {total_orders}")
print(f" Average Order Value: ${avg_order_value:,.2f}")


# Top costumers

top_5 = sales.groupby('CustomerName')['Amount'].sum().sort_values(ascending=False).head(5)
print("\n Top 5 customers:")
for i, (name, amount) in enumerate(top_5.items(), 1):
    print(f" {i}. {name}: ${amount:,.2f}")


# Top states

state_sales = sales.groupby('State')['Amount'].sum().sort_values(ascending=False).head(5)
print("\n Top 5 states:")
for i, (state, amount) in enumerate(state_sales.items(), 1):
    print(f" {i}. {state}: ${amount:,.2f}")


# Seasonality

monthly = sales.groupby('Month')['Amount'].mean()
best_month = monthly.idxmax()
best_month_value = monthly.max()
worst_month = monthly.idxmin()
worst_month_value = monthly.min()

month_names = {1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',
               7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}

print(f"\n Best month: {month_names[best_month]} (${best_month_value:,.2f} avg)")
print(f" Worst month: {month_names[worst_month]} (${worst_month_value:,.2f} avg)")
print(f" Difference: ${best_month_value - worst_month_value:,.2f}")


# Recommendations

recommendations = [
    "1. Focus retention efforts on top customers (Cory Evans, Nicholas Anderson, etc.)",
    "2. Expand marketing in New York, Florida, and California (top 3 states)",
    "3. Plan promotions around August (peak month) and January (lowest month)",
    "4. Investigate 2022 peak to replicate success factors",
    "5. Consider Q2 (April-June) for product launches (strongest quarter)"
]

for rec in recommendations:
    print(f"\n {rec}")

# SAVE REPORT

report = f"""
SALES ANALYSIS INSIGHTS REPORT
Date: {datetime.now().strftime('%Y-%m-%d')}

KEY METRICS
-----------
Total Sales: ${total_sales:,.2f}
Total Profit: ${total_profit:,.2f}
Average Margin: {avg_margin}%
Total Orders: {total_orders}
Average Order Value: ${avg_order_value:,.2f}

TOP 5 CUSTOMERS
--------------
{chr(10).join([f"{i+1}. {name}: ${amount:,.2f}" for i, (name, amount) in enumerate(top_5.items())])}

TOP 5 STATES
-----------
{chr(10).join([f"{i+1}. {state}: ${amount:,.2f}" for i, (state, amount) in enumerate(state_sales.items())])}

SEASONALITY
----------
Best Month: {month_names[best_month]} (${best_month_value:,.2f})
Worst Month: {month_names[worst_month]} (${worst_month_value:,.2f})

RECOMMENDATIONS
--------------
{chr(10).join(recommendations)}
"""

report_file = os.path.join(reports_path, f'insights_report_{datetime.now().strftime("%Y%m%d")}.txt')
with open(report_file, 'w') as f:
    f.write(report)

print(f"\n Report saved to: {report_file}")