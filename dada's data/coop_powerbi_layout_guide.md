# Power BI Dashboard Build Guide — Co-op Theme

## Theme Colours

Use a clean Co-op inspired theme:

- Primary blue: `#00B1E7`
- Navy text: `#002B49`
- Background: `#F5FBFE`
- Card background: `#FFFFFF`
- Teal accent: `#0F8482`
- Light green accent: `#E1EC54`
- Orange warning: `#FFB886`
- Risk red: `#D6424B`
- Grey labels: `#6B7280`

The blue direction is based on Co-op UK digital/brand assets rather than the green theme often associated with other supermarkets. Co-op’s public assets show blue logo usage, while its experience library includes broader secondary palette colours.

## Page 1: Executive Overview

### Canvas

- Size: 16:9
- Background: `#F5FBFE`
- Top header: blue rectangle `#00B1E7`
- Header title: `Co-op Convenience Retail Analytics`
- Font: Segoe UI or Aptos

### Top Slicers

Place under the header:

1. Date slicer
2. Store slicer
3. Category slicer
4. Member slicer

### KPI Cards

Create 5 KPI cards:

1. Total Revenue
2. Transactions
3. Average Basket Value
4. Average Availability %
5. Member Revenue Share %

Format cards:

- White background
- Rounded corners if available
- Navy values
- Grey category labels
- No heavy border

### Main Visuals

1. **Revenue by Store**  
   Horizontal bar chart. Sort descending by revenue.

2. **Revenue by Category**  
   Column chart. Use category on X-axis and revenue on Y-axis.

3. **Monthly Revenue Trend**  
   Line chart using the Date table month field.

4. **Availability Risk by Store**  
   Bar chart with conditional colour:
   - Teal if availability >= 95%
   - Red/orange if availability < 95%

5. **Member vs Non-Member Basket Value**  
   Clustered column chart using Member on X-axis and Average Basket Value as values.

6. **Key Insights Text Box**  
   Add manually written insight bullets after reviewing the dashboard.

## Page 2: Store Performance

Recommended visuals:

- Revenue by Store
- Average Basket Value by Store
- Units Sold by Store
- Availability % by Store
- Store ranking matrix

Suggested matrix columns:

- Store
- Total Revenue
- Transactions
- Average Basket Value
- Average Availability %
- Revenue Rank by Store

## Page 3: Membership Insights

Recommended visuals:

- Donut chart: Member vs Non-Member Revenue
- Card: Member Revenue Share %
- Card: Member Penetration %
- Bar chart: Member vs Non-Member Average Basket Value
- Store-level member penetration table

## Page 4: Availability & Operations

Recommended visuals:

- Availability % by Store
- Stores Below Availability Target card
- Revenue vs Availability scatter plot
- Category availability table

## Suggested Report Title

**Co-op Convenience Retail Analytics: Store, Category, Membership & Availability Performance**

## Suggested Power BI File Name

`Coop_Convenience_Retail_Analytics.pbix`
