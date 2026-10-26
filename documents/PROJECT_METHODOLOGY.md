# Project Methodology

## Workflow
1. Start with the source DataCo SMART Supply Chain dataset.
2. Clean the data and remove sensitive columns from the working copy.
3. Load the cleaned dataset into MySQL table `supply_chain_cleaned_full`.
4. Run the SQL scripts in `sql/` to calculate executive, delivery, and completed-order metrics.
5. Present the findings in `reports/global_supply_chain_interactive_report.html`.

## Known observations
- The full table has been reported as containing 180,519 rows.
- Distinct orders: 65,752.
- Sum of `Order Item Total`: 33,054,402.38.
- Sum of `Order Profit Per Order`: 3,966,902.97.
- Excluding cancelled delivery rows: 172,765 rows; late rows: 98,977; late rate: 57.29%.
- The delivery-row pattern changes around late 2017, so time-based comparisons require caution.

## Reproducibility note
The SQL files are organized, reproducible versions of the analyses documented during project work. Before publishing, run them against your current MySQL table and compare the results with the dashboard. If your table or column names differ, adjust the queries accordingly.

## Deliverables
- Interactive HTML report with three pages.
- SQL analysis scripts.
- Data dictionary and methodology notes.
- `powerbi/` is reserved for a native `.pbix` file if one is created later; the HTML report is not a `.pbix` file.
