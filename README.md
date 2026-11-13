# Retail Performance Analysis | Python & Power BI

**Question:** Which stores and categories warrant closer investigation based on recorded revenue, unit sales and product availability?

This portfolio case study uses a retail sample dataset, not actual Co-op trading records. Python cleans and summarises the data; a Power BI report presents store, category and membership comparisons. The aim is to turn routine KPIs into questions a store manager can act on—not to claim measured sales uplift.

![Executive overview of retail KPIs](images/Executive-Overview.png)

## What I examined

| Area | Measure | Management use |
|---|---|---|
| Store performance | Revenue, units and revenue per unit | Compare store mix before investigating differences |
| Availability | Mean recorded availability by store and category | Identify where to review replenishment practices |
| Membership | Revenue and units by membership status | Describe purchasing patterns without assuming causation |
| Monthly performance | Recorded revenue over time | Check changes and possible seasonality |

**Important metric definition:** Revenue per unit = total revenue / total units. It is **not** average basket value; the dataset does not identify shopping baskets.

## Findings and next decisions

The repository includes the underlying summary exports and a reproducible [management briefing generator](generate_management_brief.py). Run it to create `reports/MANAGEMENT_BRIEF.md` and store, category, membership and monthly CSV tables. The report is generated from the cleaned dataset rather than written around assumed results.

The next operational question is whether categories with lower recorded availability also contribute material revenue. That comparison can prioritise an investigation, but it cannot establish lost sales or prove that a replenishment change will improve revenue.

## Dashboard

| View | Screenshot |
|---|---|
| Store performance and operations | [Open image](images/Store-Performance-Operations.png) |
| Customer and membership | [Open image](images/Customer-Membership-Insights.png) |

The editable report is in `coop_retail_dashboard.pbix`. Screenshots show the existing report; the PBIX's DAX and refresh behaviour have not been independently retested in this update.

## Reproduce

```bash
pip install pandas tabulate
python data_cleaning.py
python data_exploration.py
python generate_management_brief.py
```

Run the scripts from the repository root. The [GitHub Actions workflow](.github/workflows/validate-retail.yml) also runs the pipeline and uploads the management briefing as an artifact.

## Limits

- The sample is not evidence of Co-op's actual performance
- Store comparisons are not adjusted for store size, opening hours or footfall
- Membership comparisons are descriptive, not estimates of membership's effect
- No intervention, revenue improvement or cost saving has been measured
