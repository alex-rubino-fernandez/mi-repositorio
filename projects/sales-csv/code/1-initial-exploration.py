"""
Sales Data Analysis - Initial Exploration
Objective: Understand the basic structure of the dataset
Questions to answer:
1. How many rows and columns do I have?
2. What data types are in each column?
3. Are there null values?
4. Which columns are numeric and which are categorical?
"""

# Import pandas
import pandas as pd

# Load the data
sales = pd.read_csv("C:/Users/alexr/OneDrive/Escritorio/GitHub/repositorio-git/projects/sales-csv/data/sales-dataset.csv")
print(sales.head()) # data.head

# Dataset dimensions
print(f"\n Dimensions: {sales.shape[0]} rows × {sales.shape[1]} columns")

""" 
There are 1194 rows and 12 variables in sales dataset.
"""

# Column names
for i, col in enumerate(sales.columns, 1):
    print(f" {i}. '{col}'")

"""
Using a "for" loop, we iterate through "sales" and obtain the names of all the columns.
"""

# Data types
print(sales.dtypes)

# Null values
null_counts = sales.isnull().sum()
print(null_counts[null_counts > 0] if any(null_counts > 0) else "No null values found!")

"""
In the variable null_counts, we count the total number of null values in the sales CSV. 
Then, we print the columns with null values using an if-else condition. 
In this case, no null values were found.
"""

# Select numeric columns
numeric_columns = sales.select_dtypes(include=['int64', 'float64']).columns.tolist()
print(f"\n Numeric columns ({len(numeric_columns)}): {numeric_columns}")

# Select categorical columns
categorical_columns = sales.select_dtypes(include=['object']).columns.tolist()
print(f"\n Categorical columns ({len(categorical_columns)}): {categorical_columns}")

"""
In dtypes, we saw how the columns were structured. 
Now, we select the variables that include integers and floats for numeric columns, 
and objects for categorical columns. 
We identified 3 numeric columns and 9 categorical columns.
"""