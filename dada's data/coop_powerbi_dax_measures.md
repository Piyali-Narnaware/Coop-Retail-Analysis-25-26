# Power BI DAX Measures — Co-op Convenience Retail Analytics

Use these measures after loading `Retail_Convenience_Analytics_Dataset.csv` into Power BI as a table named `Retail`.
Create a separate Date table for proper time intelligence.

```DAX
Date = CALENDAR(MIN(Retail[Date]), MAX(Retail[Date]))
```

Then mark `Date[Date]` as the Date table and connect `Date[Date]` to `Retail[Date]`.

## Core KPI Measures

```DAX
Total Revenue = SUM(Retail[Revenue])

Total Units = SUM(Retail[Units])

Transactions = COUNTROWS(Retail)

Average Basket Value = DIVIDE([Total Revenue], [Transactions])

Average Units per Transaction = DIVIDE([Total Units], [Transactions])

Average Availability % = AVERAGE(Retail[Availability_Pct])
```

## Membership Measures

```DAX
Member Revenue =
CALCULATE(
    [Total Revenue],
    Retail[Member] = "Yes"
)

Non-Member Revenue =
CALCULATE(
    [Total Revenue],
    Retail[Member] = "No"
)

Member Revenue Share % =
DIVIDE([Member Revenue], [Total Revenue])

Member Transactions =
CALCULATE(
    [Transactions],
    Retail[Member] = "Yes"
)

Member Penetration % =
DIVIDE([Member Transactions], [Transactions])

Member Average Basket Value =
CALCULATE(
    [Average Basket Value],
    Retail[Member] = "Yes"
)

Non-Member Average Basket Value =
CALCULATE(
    [Average Basket Value],
    Retail[Member] = "No"
)
```

## Store & Category Performance

```DAX
Revenue per Store = [Total Revenue]

Revenue per Category = [Total Revenue]

Units per Category = [Total Units]

Revenue Rank by Store =
RANKX(
    ALL(Retail[Store]),
    [Total Revenue],
    ,
    DESC
)

Revenue Rank by Category =
RANKX(
    ALL(Retail[Category]),
    [Total Revenue],
    ,
    DESC
)
```

## Availability / Operational Risk

```DAX
Availability Target % = 95

Availability Gap % =
[Average Availability %] - [Availability Target %]

Stores Below Availability Target =
COUNTROWS(
    FILTER(
        VALUES(Retail[Store]),
        [Average Availability %] < [Availability Target %]
    )
)

Availability Status =
IF(
    [Average Availability %] >= [Availability Target %],
    "On Target",
    "Below Target"
)
```

## Time Trend Measures

```DAX
Revenue MTD =
TOTALMTD([Total Revenue], 'Date'[Date])

Revenue Previous Month =
CALCULATE(
    [Total Revenue],
    DATEADD('Date'[Date], -1, MONTH)
)

Revenue MoM Change =
[Total Revenue] - [Revenue Previous Month]

Revenue MoM Change % =
DIVIDE([Revenue MoM Change], [Revenue Previous Month])
```

## Tooltip Measures

```DAX
Revenue Contribution % =
DIVIDE(
    [Total Revenue],
    CALCULATE([Total Revenue], ALL(Retail))
)

Category Contribution % =
DIVIDE(
    [Total Revenue],
    CALCULATE([Total Revenue], ALL(Retail[Category]))
)
```
