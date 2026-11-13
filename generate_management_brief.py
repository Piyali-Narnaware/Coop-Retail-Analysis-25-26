"""Generate a decision-focused report from the repository's retail sample data.

Descriptive comparisons only: no causal claims or realised savings.
"""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent
df = pd.read_csv(ROOT / "coop_retail_cleaned_dataset.csv", parse_dates=["date"])
required = {"date", "store", "category", "member", "revenue", "units", "availability_pct"}
missing = required - set(df.columns)
if missing:
    raise ValueError(f"Missing columns: {sorted(missing)}")
assert df["date"].notna().all()
assert df["units"].gt(0).all()
assert df["revenue"].ge(0).all()

def group_summary(column):
    result = df.groupby(column, dropna=False).agg(
        revenue=("revenue", "sum"),
        units=("units", "sum"),
        avg_availability_pct=("availability_pct", "mean"),
        observations=("revenue", "size"),
    )
    result["revenue_per_unit"] = result["revenue"] / result["units"]
    return result.sort_values("revenue", ascending=False).round(2)

store = group_summary("store")
category = group_summary("category")
member = group_summary("member")
monthly = df.groupby(df["date"].dt.to_period("M")).agg(
    revenue=("revenue", "sum"), units=("units", "sum")
)
monthly.index = monthly.index.astype(str)
out = ROOT / "reports"
out.mkdir(exist_ok=True)
for name, frame in [("store", store), ("category", category), ("membership", member), ("monthly", monthly)]:
    frame.to_csv(out / f"{name}_performance.csv")

def md_table(frame, n=6):
    selected = frame.head(n).reset_index()
    return selected.to_markdown(index=False, floatfmt=".2f")

report = f"""# Retail performance: management briefing

**Dataset:** portfolio retail sample included in this repository; not actual Co-op trading results.

**Period:** {df["date"].min().date()} to {df["date"].max().date()}  
**Valid records:** {len(df):,}  
**Recorded revenue:** {df["revenue"].sum():,.2f} (currency not independently verified)  
**Units:** {df["units"].sum():,.0f}  
**Weighted revenue per unit:** {df["revenue"].sum()/df["units"].sum():.2f}

## Highest recorded revenue by store
{md_table(store)}

## Highest recorded revenue by category
{md_table(category)}

## Membership comparison
{md_table(member)}

## Management interpretation

1. **Store performance:** Investigate whether the highest-revenue stores also have lower recorded availability. Revenue alone does not adjust for footfall, store size or trading hours.
2. **Category availability:** Review low-availability categories alongside revenue and units to identify candidates for replenishment investigation. These data do not establish lost sales.
3. **Membership:** Compare member/non-member revenue and revenue per unit descriptively. Do not infer that membership causes higher spend without a controlled analysis.
4. **Trend:** Use `reports/monthly_performance.csv` to inspect seasonality; do not infer growth without accounting for changes in store mix or coverage.

## Decision and validation notes

- Recommended next action: investigate the largest availability gaps in commercially important categories before proposing replenishment changes.
- Any revenue uplift, waste reduction or operational saving would require a measured intervention or a clearly labelled scenario.
- Revenue per unit is calculated as **sum(revenue) / sum(units)**, not the mean of row-level ratios and not average basket value.
- Availability is the simple mean of recorded availability percentages; no stock- or sales-weighted interpretation is implied.
- This is descriptive portfolio analysis, not a claim about Co-op's actual commercial performance.
"""
(out / "MANAGEMENT_BRIEF.md").write_text(report, encoding="utf-8")
print("Generated management briefing and four performance CSVs in reports/")
