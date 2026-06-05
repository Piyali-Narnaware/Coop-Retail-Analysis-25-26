import pandas as pd

# Load cleaned dataset
df = pd.read_csv("E:/Git_projects/dada/coop_retail_cleaned_dataset.csv")

# Check columns
print("Columns in dataset:")
print(df.columns.tolist())

# Make sure date is datetime
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# -----------------------------
# 1. Revenue by Store
# -----------------------------
store_revenue = (
    df.groupby("store")["revenue"]
    .sum()
    .sort_values(ascending=False)
    .round(2)
)

print("\nRevenue by Store")
print(store_revenue)

# -----------------------------
# 2. Revenue by Category
# -----------------------------
category_revenue = (
    df.groupby("category")["revenue"]
    .sum()
    .sort_values(ascending=False)
    .round(2)
)

print("\nRevenue by Category")
print(category_revenue)

# -----------------------------
# 3. Revenue by Customer
# -----------------------------
customer_revenue = (
    df.groupby("customer_id")["revenue"]
    .sum()
    .sort_values(ascending=False)
    .round(2)
)

print("\nTop 10 Customers by Revenue")
print(customer_revenue.head(10))

# -----------------------------
# 4. Member vs Non-Member Revenue
# -----------------------------
member_revenue = (
    df.groupby("member")["revenue"]
    .sum()
    .sort_values(ascending=False)
    .round(2)
)

print("\nMember vs Non-Member Revenue")
print(member_revenue)

# -----------------------------
# 5. Monthly Revenue Trend
# -----------------------------
monthly_revenue = (
    df.groupby("month")["revenue"]
    .sum()
    .sort_index()
    .round(2)
)

print("\nMonthly Revenue Trend")
print(monthly_revenue)

# -----------------------------
# 6. Store Revenue by Month
# -----------------------------
store_revenue_by_month = (
    df.groupby(["store", "month"])["revenue"]
    .sum()
    .reset_index()
    .sort_values(["store", "month"])
)

store_revenue_by_month["revenue"] = store_revenue_by_month["revenue"].round(2)

print("\nStore Revenue by Month")
print(store_revenue_by_month.head(20))

# -----------------------------
# 7. Availability by Store
# -----------------------------
availability_by_store = (
    df.groupby("store")["availability_pct"]
    .mean()
    .sort_values(ascending=False)
    .round(2)
)

print("\nAvailability by Store")
print(availability_by_store)

# -----------------------------
# 8. Availability by Category
# -----------------------------
availability_by_category = (
    df.groupby("category")["availability_pct"]
    .mean()
    .sort_values(ascending=False)
    .round(2)
)

print("\nAvailability by Category")
print(availability_by_category)

# -----------------------------
# 9. Availability by Member
# -----------------------------
availability_by_member = (
    df.groupby("member")["availability_pct"]
    .mean()
    .sort_values(ascending=False)
    .round(2)
)

print("\nAvailability by Member")
print(availability_by_member)

# -----------------------------
# 10. Basket Value by Store
# -----------------------------
basket_value_by_store = (
    df.groupby("store")["avg_basket_value"]
    .mean()
    .sort_values(ascending=False)
    .round(2)
)

print("\nBasket Value by Store")
print(basket_value_by_store)

# -----------------------------
# 11. Basket Value by Category
# -----------------------------
basket_value_by_category = (
    df.groupby("category")["avg_basket_value"]
    .mean()
    .sort_values(ascending=False)
    .round(2)
)

print("\nBasket Value by Category")
print(basket_value_by_category)

# -----------------------------
# 12. Basket Value by Member
# -----------------------------
basket_value_by_member = (
    df.groupby("member")["avg_basket_value"]
    .mean()
    .sort_values(ascending=False)
    .round(2)
)

print("\nBasket Value by Member")
print(basket_value_by_member)

# -----------------------------
# 13. Store Summary Table
# -----------------------------
store_summary = (
    df.groupby("store")
    .agg(
        total_revenue=("revenue", "sum"),
        total_units=("units", "sum"),
        unique_customers=("customer_id", "nunique"),
        avg_availability=("availability_pct", "mean"),
        avg_basket_value=("avg_basket_value", "mean")
    )
    .round(2)
    .sort_values("total_revenue", ascending=False)
)

print("\nStore Summary")
print(store_summary)

# -----------------------------
# 14. Category Summary Table
# -----------------------------
category_summary = (
    df.groupby("category")
    .agg(
        total_revenue=("revenue", "sum"),
        total_units=("units", "sum"),
        unique_customers=("customer_id", "nunique"),
        avg_availability=("availability_pct", "mean"),
        avg_basket_value=("avg_basket_value", "mean")
    )
    .round(2)
    .sort_values("total_revenue", ascending=False)
)

print("\nCategory Summary")
print(category_summary)

# -----------------------------
# 15. Member Summary Table
# -----------------------------
member_summary = (
    df.groupby("member")
    .agg(
        total_revenue=("revenue", "sum"),
        total_units=("units", "sum"),
        unique_customers=("customer_id", "nunique"),
        avg_availability=("availability_pct", "mean"),
        avg_basket_value=("avg_basket_value", "mean")
    )
    .round(2)
    .sort_values("total_revenue", ascending=False)
)

print("\nMember Summary")
print(member_summary)

# -----------------------------
# 16. Overall KPI Summary
# -----------------------------
kpi_summary = {
    "total_revenue": round(df["revenue"].sum(), 2),
    "total_units": int(df["units"].sum()),
    "unique_customers": int(df["customer_id"].nunique()),
    "avg_availability": round(df["availability_pct"].mean(), 2),
    "avg_basket_value": round(df["revenue"].sum() / df["units"].sum(), 2)
}

print("\nOverall KPI Summary")
print(kpi_summary)

# -----------------------------
# 17. Save Data Exploration outputs
# -----------------------------
# Dashboard-ready exports

monthly_revenue_df = monthly_revenue.reset_index()
store_revenue_df = store_revenue.reset_index()
category_revenue_df = category_revenue.reset_index()
member_revenue_df = member_revenue.reset_index()

monthly_revenue_df.to_csv("E:/Git_projects/dada/monthly_revenue.csv", index=False)
store_revenue_df.to_csv("E:/Git_projects/dada/store_revenue.csv", index=False)
category_revenue_df.to_csv("E:/Git_projects/dada/category_revenue.csv", index=False)
member_revenue_df.to_csv("E:/Git_projects/dada/member_revenue.csv", index=False)

print("Dashboard export files saved successfully.")

