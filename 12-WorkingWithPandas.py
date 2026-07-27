# Pandas is the most important library for data manipulation and analysis in Python.
# It is built on top of NumPy and provides two main data structures:
#       Series → 1-dimensional labeled array
#       DataFrame → 2-dimensional labeled table (like an Excel sheet or SQL table)

# pip install pandas

# Creating Series & DataFrames

# Series
import pandas as pd
import numpy as np
s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
s = pd.Series({'a': 10, 'b': 20, 'c': 30})

# DataFrame from dictionary
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['NY', 'LA', 'Chicago', 'Houston'],
    'Salary': [70000, 80000, 90000, 95000]
})

# From list of lists
df2 = pd.DataFrame(
    [[1, 'A'], [2, 'B'], [3, 'C']],
    columns=['ID', 'Label']
)

# From NumPy array
df3 = pd.DataFrame(np.random.randn(5, 3), columns=['A', 'B', 'C'])

# Essential Attributes & Inspection
df.shape          # (rows, columns)
df.columns        # column names
df.index          # row labels
df.dtypes         # data types of each column
df.info()         # summary (memory, nulls, dtypes)
df.describe()     # statistical summary of numeric columns
df.head(3)        # first 3 rows
df.tail(2)        # last 2 rows
df.sample(3)      # random sample

#Selecting Data
# # Select columns
df['Name']                    # Series
df[['Name', 'Age']]           # DataFrame

# Select rows by position
df.iloc[0]                    # first row
df.iloc[1:3]                  # rows 1 and 2
df.iloc[1:3, 0:2]             # rows + columns by position

# Select rows by label
df.loc[0]                     # row with index 0
df.loc[0:2, ['Name', 'City']] # rows + columns by label

# Boolean indexing (most powerful)
df[df['Age'] > 30]
df[(df['Age'] > 30) & (df['Salary'] > 85000)]
df[df['City'].isin(['NY', 'LA'])]

# Adding / Removing / Modifying Columns
# Add new column
df['Bonus'] = df['Salary'] * 0.1
df['Senior'] = df['Age'] >= 35

# Modify existing column
df['Salary'] = df['Salary'] + 5000

# Remove columns
df = df.drop(columns=['Bonus'])
# or
del df['Senior']
# Rename columns
df = df.rename(columns={'Name': 'FullName', 'City': 'Location'})

# Handling Missing Data
df.isna()                     # boolean mask of missing values
df.isnull().sum()             # count of missing values per column

df.dropna()                   # drop rows with any NaN
df.dropna(subset=['Age'])     # drop only if Age is missing
df.fillna(0)                  # fill all NaNs with 0
df['Age'].fillna(df['Age'].mean(), inplace=True)



# ============================================================
# GroupBy + Sorting + Merging + Apply/Map (Using Original DataFrame)
# ============================================================

import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['NY', 'LA', 'Chicago', 'Houston'],
    'Salary': [70000, 80000, 90000, 95000]
})

print("Original DataFrame:")
print(df)
print("=" * 60)

# GroupBy -------------------------------

print("\n1. Basic aggregation (mean Salary by City):")
print(df.groupby('City')['Salary'].mean())

print("\n2. Multiple columns:")
print(df.groupby('City')[['Age', 'Salary']].mean())

print("\n3. Multiple aggregations:")
print(df.groupby('City').agg({
    'Age': 'mean',
    'Salary': ['mean', 'max', 'min']
}))

print("\n4. Group + transform:")
df['AvgSalaryByCity'] = df.groupby('City')['Salary'].transform('mean')
print(df)

# Sorting & Ranking ------------------------------
print("\n5. Sort by Salary (descending):")
print(df.sort_values('Salary', ascending=False))

print("\n6. Sort by City then Age:")
print(df.sort_values(['City', 'Age'], ascending=[True, False]))

print("\n7. Add Rank based on Salary:")
df['Rank'] = df['Salary'].rank(ascending=False).astype(int)
print(df)

# Merging & Joining ------------------------------
print("\n" + "=" * 60)
print("Merging & Joining examples:")

df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['A', 'B', 'C']})
df2 = pd.DataFrame({'ID': [1, 2, 4], 'Score': [90, 85, 88]})

print("\nInner Join:")
print(pd.merge(df1, df2, on='ID', how='inner'))

print("\nLeft Join:")
print(pd.merge(df1, df2, on='ID', how='left'))

print("\nOuter Join:")
print(pd.merge(df1, df2, on='ID', how='outer'))

# Apply / Map / Vectorized Operations  --------------------------
print("\n" + "=" * 60)
print("Apply / Map / String methods:")

# Apply
df['Name_Length'] = df['Name'].apply(len)

# Map
df['City_Code'] = df['City'].map({'NY': 1, 'LA': 2, 'Chicago': 3, 'Houston': 4})

print(df)

print("\nUppercase names:")
print(df['Name'].str.upper())

print("\nNames containing 'A':")
print(df['Name'].str.contains('A'))

print("\nSplit names (example):")
print(df['Name'].str.split('e'))   # just for demonstration


# Reading & Writing Files (Commented - files don't exist)
print("\n" + "=" * 60)
print("Reading & Writing Files (examples - commented out):")

# Uncomment these lines only when you have the actual files

# df = pd.read_csv('data.csv')
# df = pd.read_excel('data.xlsx', sheet_name='Sheet1')
# df = pd.read_json('data.json')
# df = pd.read_parquet('data.parquet')

# df.to_csv('output.csv', index=False)
# df.to_excel('output.xlsx', index=False)
# df.to_parquet('output.parquet')

print("File reading/writing examples are commented to avoid errors.")
