# Colgate-Palmolive Pro Forma Model (2024)

A percent-of-sales pro forma model of **Colgate-Palmolive Company**: income statement, balance sheet and cash flow statement for 2023-2027, with 2024 as the target year. Built in Excel from five years of reported statements (2018-2022).

This is an improved version of a Financial Modelling (BBA2293) group assignment I submitted in the past. It covers only my part, the pro forma statements. Free cash flow, WACC and valuation were done by teammates and are not included.

## What's in here

| Folder | Contents |
|---|---|
| `model/` | `Colgate_Task1_Pro_Forma_Model.xlsx`: historical statements, assumption sheets, pro forma statements, integrity checks |
| `report/` | `Colgate_Pro_Forma_Report.pdf`: full written report (method, assumptions, statements, sensitivity, limitations) |
| `charts/` | The two report figures and `make_charts.py`, which rebuilds them from the workbook |

## Method

- **Sales** grow 3.33% a year (average of an industry forecast of 3.6% and the historical CAGR of 3.06%).
- **Operating costs** (excluding depreciation) come from a regression of costs on sales over 2018-2022 (R-squared 0.97, slope 0.94).
- **Depreciation** is opening gross fixed assets divided by 17 (average historical ratio).
- **Working capital and net fixed assets** follow five-year average ratios to sales.
- **Interest** is 2.44% on $8,766m of borrowings; cash earns 1% on the opening balance.
- **Tax** is the weighted average effective rate (24.19%); dividends grow 1.54% a year.
- **Cash is the balancing item** of the balance sheet. Debt and non-retained-earnings equity are held constant.

## 2024 base case ($ million)

| Sales | EBITDA | Profit after tax | Total assets | Operating cash flow |
|---|---|---|---|---|
| 19,184 | 4,335 | 2,688 | 17,800 | 3,220 |

## Integrity checks

The workbook checks that (1) assets equal liabilities plus equity in every year, (2) cash from the cash flow statement equals balance sheet cash, and (3) 2022 total assets agree to the reported $15,731m. All checks are zero.

## What the model shows (and its limits)

- Costs rose almost one for one with sales, so profit stays near $2.7bn whatever the sales growth. A 1-point change in growth moves 2024 profit by about $15m, while a 0.04 change in the cost slope moves it by about $580m.
- The 3.33% growth assumption is conservative: Colgate reported 2023 sales of $19,457m (+8.3%), 4.6% above the model's 2023 forecast.
- Constant debt and equity make cash build to $4.9bn by 2027. In practice Colgate returns cash through buybacks.
- The 2022 base year excludes the $721m goodwill impairment, so it does not match reported net income.

The report discusses these and other limitations in full.

## Rebuilding the charts

```bash
pip install openpyxl numpy matplotlib pillow
python charts/make_charts.py
```

## Data

Historical figures are from Colgate-Palmolive's published annual financial statements. This is a classroom-style forecast, not investment advice.
- https://investor.colgatepalmolive.com/annual-reports
- https://investor.colgatepalmolive.com/static-files/76063a59-e943-4c5d-8782-46c108c74aca (2022 annual financial report)
- https://investor.colgatepalmolive.com/static-files/cdc1e779-57c6-4e07-86f8-2c14ae9f1650 (2021 annual financial report)
- https://investor.colgatepalmolive.com/static-files/60e687b3-c213-4d8d-9529-1833f5e9f6c3 (2020 annual financial report)

*Remark: Every financial report listed also includes two to three years prior to the reported year*

## License

MIT, see `LICENSE`.
