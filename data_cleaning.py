import pandas as pd

# 1. Load data
df = pd.read_csv("E:/Git_projects/dada/Retail_Convenience_Analytics_Dataset.csv")

# 2. Check basic info
print(df.head())
print(df.info())
print(df.isnull().sum())

# 3. Clean column names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# 4. Convert date column
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# 5. Standardise text columns
text_cols = ["store", "category", "member"]

for col in text_cols:
    df[col] = df[col].astype(str).str.strip().str.title()

# 6. Clean numeric columns
df["revenue"] = pd.to_numeric(df["revenue"], errors="coerce")
df["units"] = pd.to_numeric(df["units"], errors="coerce")
df["availability_pct"] = pd.to_numeric(df["availability_pct"], errors="coerce")

# 7. Remove duplicate rows
df = df.drop_duplicates()

# 8. Remove invalid records
df = df[df["revenue"] >= 0]
df = df[df["units"] > 0]
df = df[(df["availability_pct"] >= 0) & (df["availability_pct"] <= 100)]

# 9. Add useful dashboard columns
df["month"] = df["date"].dt.to_period("M").astype(str)
df["year"] = df["date"].dt.year
df["month_name"] = df["date"].dt.month_name()
df["day_name"] = df["date"].dt.day_name()

# 10. Create calculated field: average basket value
df["avg_basket_value"] = df["revenue"] / df["units"]

# 11. Create member flag
df["is_member"] = df["member"].apply(lambda x: 1 if x == "Yes" else 0)

# 12. Final checks
print(df.head())
print(df.info())
print(df.isnull().sum())


print("Original rows:", 5000)
print("Cleaned rows:", len(df))
print("Rows removed:", 5000 - len(df))

summary = {
    "total_rows": len(df),
    "total_revenue": round(df["revenue"].sum(), 2),
    "total_units": df["units"].sum(),
    "unique_customers": round(df["customer_id"].nunique(), 2),
    "avg_availability": round(df["availability_pct"].mean(), 2),
    "avg_basket_value": round(df["revenue"].sum() / df["units"].sum(), 2)
}

print(summary)

# 13. Save cleaned file
df.to_csv("E:/Git_projects/dada/coop_retail_cleaned_dataset.csv", index=False)

print("Cleaned file saved successfully!")