import pandas as pd
import numpy as np

df = pd.read_csv("./SampleFiles/iris.csv")

# ============================================================
# 1. Sorting
# ============================================================
print(df.sort_values("sepal_length", ascending=False).head())          # Descending order
print(df.sort_values(["species", "petal_length"], ascending=[True, False]).head())

# ============================================================
# 2. Removing Duplicate Rows
# ============================================================
print(df.duplicated().sum())          # Number of duplicate rows
df_unique = df.drop_duplicates()

# ============================================================
# 3. Renaming Columns (Safe Approach)
# ============================================================
df = df.rename(columns={
    "sepal_length": "sepal_length_cm",
    "sepal_width": "sepal_width_cm",
    "petal_length": "petal_length_cm",
    "petal_width": "petal_width_cm"
})

# ============================================================
# 4. Adding a New Column with Conditions (apply / np.where)
# ============================================================
df["size_category"] = np.where(df["sepal_length_cm"] > 6, "Large", "Small")

# Using a custom function
def categorize(row):
    if row["petal_length_cm"] < 2:
        return "Small"
    elif row["petal_length_cm"] < 5:
        return "Medium"
    else:
        return "Large"

df["petal_size"] = df.apply(categorize, axis=1)

# ============================================================
# 5. Counting Values in Each Category (value_counts)
# ============================================================
print(df["species"].value_counts())
print(df["size_category"].value_counts(normalize=True))   # Display as percentages

# ============================================================
# 6. Pivot Table
# ============================================================
print(pd.pivot_table(
    df,
    values="sepal_length_cm",
    index="species",
    columns="size_category",
    aggfunc="mean"
))

# ============================================================
# 7. Correlation Between Columns
# ============================================================
print(df[[
    "sepal_length_cm",
    "sepal_width_cm",
    "petal_length_cm",
    "petal_width_cm"
]].corr())

# ============================================================
# 8. Advanced Filtering
# ============================================================
# Multiple conditions
filtered = df[
    (df["sepal_length_cm"] > 6) &
    (df["species"] == "virginica")
]
print(filtered.head())

# Filtering with isin()
print(df[df["species"].isin(["setosa", "versicolor"])].head())

# ============================================================
# 9. String Operations
# ============================================================
df["species_upper"] = df["species"].str.upper()
df["species_title"] = df["species"].str.title()

# ============================================================
# 10. Random Sampling
# ============================================================
print(df.sample(10))          # Select 10 random rows
print(df.sample(frac=0.2))    # Select 20% of the dataset

# ============================================================
# 11. Saving the Data with Additional Options
# ============================================================
df.to_csv(
    "./SampleFiles/iris_advanced.csv",
    index=False,
    encoding="utf-8-sig"
)  # UTF-8 with BOM (useful for Excel)

# df.to_excel("./SampleFiles/iris_advanced.xlsx", index=False)  # Requires openpyxl

print("\nAll advanced operations completed successfully.")