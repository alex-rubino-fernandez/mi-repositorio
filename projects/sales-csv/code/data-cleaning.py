"""
Sales Data Analysis - Data Cleaning
Objective: Prepare and clean the data for analysis
Questions to answer:
1. Are there duplicate records?
2. Are data types correct? (dates as datetime, numbers as numbers)
3. Are there inconsistent categories? (types, different formats)
4. Are there outliers in numeric columns?
5. Can we create new useful columns?
"""

import pandas as pd
import numpy as np

# Load the data
sales = pd.read_csv("C:/Users/alexr/OneDrive/Escritorio/repositorio-git/projects/sales-csv/data/sales-dataset.csv")

# Checking for duplicates
duplicate_count = sales.duplicated().sum()
print(f"\n Number of duplicate rows: {duplicate_count}")

'''
We check for duplicates using the duplicated() function and count them with sum().
In this dataset, there are no duplicate records.
'''

# Checking data types

print(sales.dtypes) #current data types

# Identify potential data columns
date_columns = [col for col in sales.columns if 'date' in col.lower() or 'time' in col.lower()]
if date_columns:
    print(f"\n Potential date columns found: {date_columns}")
    
    for col in date_columns:
        # Try to convert to datetime
        try:
            sales[col] = pd.to_datetime(sales[col])
            print(f"Converted '{col}' to datetime")
        except:
            print(f"Could not convert '{col}' to datetime")


'''
First, we display the current data types using dtypes.
Then, with a list comprehension, we iterate through all column names and check if any 
contain the words 'date' or 'time' (case insensitive).
If such columns exist, we attempt to convert them to datetime format.
This ensures proper time-based analysis later.
'''

# Checking categorical columns for inconsistencies
# Select categorical columns (object type)
categorical_columns = sales.select_dtypes(include=['object']).columns.tolist()
print(f"\n Categorical columns found: {categorical_columns}")

for col in categorical_columns:
    print(f"\n Analyzing column: '{col}'")
    
    # Get unique values count
    unique_count = sales[col].nunique()
    print(f" Unique values: {unique_count}")
    
    # Check for leading/trailing spaces
    has_spaces = any(sales[col].astype(str).str.contains('^\\s|\\s$', regex=True))
    if has_spaces:
        print(f" Found leading/trailing spaces")
        # Clean the spaces
        sales[col] = sales[col].astype(str).str.strip()
        print(f" Spaces removed")
    else:
        print(f" No leading/trailing spaces")
    
    # Show sample values
    print(f" Sample values: {sales[col].unique()[:5]}")

'''
We identify categorical columns (those with data type 'object').
For each categorical column, we check:
1. Number of unique values (helps identify high-cardinality columns)
2. Presence of leading/trailing spaces that could cause grouping issues
3. Sample values to spot inconsistencies in spelling or format
If spaces are found, we remove them using strip() to ensure clean categories.
'''

# Checking for outliers in numeric columns

# Select numeric columns
numeric_columns = sales.select_dtypes(include=['int64', 'float64']).columns.tolist()
print(f"\n Numeric columns found: {numeric_columns}")

for col in numeric_columns:
    print(f"\n Analyzing column: '{col}'")
    
    # Calculate statistics
    mean_val = sales[col].mean()
    std_val = sales[col].std()
    min_val = sales[col].min()
    max_val = sales[col].max()
    
    print(f" Mean: {mean_val:.2f}")
    print(f" Std deviation: {std_val:.2f}")
    print(f" Range: [{min_val:.2f}, {max_val:.2f}]")
    
    # Method 1: Using IQR (Interquartile Range)
    Q1 = sales[col].quantile(0.25)
    Q3 = sales[col].quantile(0.75)
    IQR = Q3 - Q1
    
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    outliers_iqr = sales[(sales[col] < lower_bound) | (sales[col] > upper_bound)]
    outlier_count_iqr = len(outliers_iqr)
    
    print(f" IQR method - Outliers: {outlier_count_iqr} ({outlier_count_iqr/len(sales)*100:.1f}%)")
    
    # Method 2: Using Z-Score (values beyond 3 standard deviations)
    z_scores = np.abs((sales[col] - mean_val) / std_val)
    outliers_z = sales[z_scores > 3]
    outlier_count_z = len(outliers_z)
    
    print(f" Z-Score method - Outliers: {outlier_count_z} ({outlier_count_z/len(sales)*100:.1f}%)")
    
'''
Outlier detection helps identify anomalous values that might skew our analysis.
We use two complementary methods:
1. IQR method: Values beyond 1.5 * IQR below Q1 or above Q3
2. Z-Score method: Values more than 3 standard deviations from the mean
Both methods are valid; comparing them gives a robust view of potential outliers.

RESULTS:
- Amount: No outliers detected. Range: $508-$9,992, Mean: $5,178
- Profit: IQR method: 10 outliers (0.8%), Z-Score: 4 outliers (0.3%). 
  Range: $50-$4,930, Mean: $1,349
- Quantity: No outliers detected. Range: 1-20 units, Mean: 10.7

The Profit column contains a small number of potential outliers worth 
investigating further. Amount and Quantity show no extreme values.
'''

# New useful columns

# Create Year and Month from date column
if date_columns:
    date_col = date_columns[0]
    print(f"\nCreating features from '{date_col}':")
    
    sales['Year'] = sales[date_col].dt.year
    sales['Month'] = sales[date_col].dt.month
    sales['Month_Name'] = sales[date_col].dt.month_name()
    sales['Quarter'] = sales[date_col].dt.quarter
    
    print(f"Added: Year, Month, Month_Name, Quarter")

# Create profit margin
if 'Amount' in sales.columns and 'Profit' in sales.columns:
    print(f"\nCreating profit margin:")
    sales['Profit_Margin'] = (sales['Profit'] / sales['Amount'] * 100).round(2)
    print(f"Added: Profit_Margin (%)")

# Create average unit price
if 'Amount' in sales.columns and 'Quantity' in sales.columns:
    print(f"\nCreating average unit price:")
    sales['Avg_Unit_Price'] = (sales['Amount'] / sales['Quantity']).round(2)
    print(f"Added: Avg_Unit_Price")

'''
Feature engineering creates new columns from existing data:
- Year, Month, Month_Name, Quarter: Enable time-based analysis
- Profit_Margin: Shows profitability percentage regardless of sale size
- Avg_Unit_Price: Reveals pricing patterns across transactions

These derived columns often provide more insights than raw data.
'''

# Verification
print(sales.head(10))

"""
VERIFICATION OUTPUT SUMMARY:

Six new columns were successfully created:
- Profit_Margin: Ranges from 12% to 44%, showing varying profitability
- Avg_Unit_Price: Ranges from $88 to $1,945, indicating different product tiers
- Time features: Year, Month, Month_Name, Quarter added for temporal analysis

Total columns expanded from 12 to 18. All calculations completed successfully.

Note: Same Order ID appears across different months (e.g., B-26776 in June, July, Dec). 
This suggests possible data duplication to investigate before aggregation.
"""