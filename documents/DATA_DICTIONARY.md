# Data Dictionary and Metric Definitions

## Dataset overview
- Source: DataCo SMART Supply Chain dataset, Mendeley Data, version 5.
- Working table: `supply_chain_cleaned_full` in database `supply_chain_intelligence`.
- The analyzed cleaned dataset contains approximately 180,519 rows. Confirm the exact row count after importing your final cleaned CSV.

## Key fields used
| Field | Meaning in this project |
|---|---|
| `Order Id` | Identifier used to count distinct orders |
| `Order Item Total` | Monetary item-value field summed for the sales/value KPI |
| `Order Profit Per Order` | Recorded profit field summed for the profit KPI |
| `Order Status` | Order status used to scope completed-order analysis |
| `Delivery Status` | Delivery outcome used to calculate late-delivery rate |
| `Shipping Mode` | Shipping service category used to compare delivery outcomes |

## Metric definitions
- **Distinct orders:** count of distinct `Order Id` values.
- **Total order item value:** sum of `Order Item Total` across the selected records.
- **Total recorded profit:** sum of `Order Profit Per Order` across the selected records.
- **Late delivery rate:** late-delivery rows divided by non-cancelled delivery rows, multiplied by 100.
- **Completed-order metrics:** the same monetary fields filtered to `Order Status = 'COMPLETE'`.

## Interpretation cautions
- These are descriptive dataset metrics, not audited financial results.
- Some report pages use all statuses; others focus on `COMPLETE`. Check each page's scope before comparing totals.
- Cancelled delivery rows are excluded from late-delivery-rate denominators.
- A structural change was observed around October/November 2017, including a shift in row/order/quantity patterns and category mix. Comparisons across that period should be treated cautiously.
- Shipping-mode late rates do not establish that shipping mode alone caused delays.

## Attribution
Record the official dataset landing-page URL and required attribution in the final repository. Verify the current source-page license/redistribution terms before committing the dataset itself.
