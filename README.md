# Global Supply Chain & Inventory Intelligence

An end-to-end data analytics portfolio project exploring sales value,
profitability, delivery performance, shipping modes, and product-level
patterns in a global supply-chain dataset.

## Project Overview

Supply-chain teams need to understand not only how much they sell, but
also where profit is generated and where delivery operations may be
underperforming. This project uses the DataCo SMART Supply Chain dataset
to build a repeatable analysis workflow and an interactive three-page
report.

The analysis focuses on: - Executive-level sales and profit indicators -
Product and profitability patterns - Shipping and delivery performance -
Data-quality observations that affect how results should be interpreted

## Tools Used

-   **Python / Pandas** --- data preparation and cleaning
-   **MySQL** --- querying, aggregations, and operational analysis
-   **HTML report with interactive charts** --- presenting the findings
    in three pages
-   **Power BI Desktop** --- explored as a reporting option; the
    deliverable currently included here is the HTML report, not a
    `.pbix` file

> Update this tools list if the final repository contains additional
> scripts or a native Power BI file.

## Dataset

**Source:** DataCo SMART Supply Chain dataset, Mendeley Data, version
5.\
**License:** CC BY 4.0 (confirm attribution and license details on the
dataset's source page before publishing the data itself).

The source dataset contains approximately 180,519 rows and 47 columns. A
cleaned working file was created for analysis, with sensitive columns
removed.

Recommended practice: include the source link and attribution in the
repository. Before uploading the CSV, confirm the dataset's
redistribution terms and avoid publishing any sensitive fields.

## Repository Structure

``` text
global-supply-chain-inventory-intelligence/
├── data/
│   ├── raw/
│   │   └── DataCoSupplyChainDataset.csv
│   └── processed/
│       └── supply_chain_cleaned.csv
├── reports/
│   └── global_supply_chain_interactive_report.html
├── sql/
│   └── [SQL analysis scripts]
└── README.md
```

The `sql/` folder and script names above are a suggested structure;
adjust them to match the files actually committed.

## Key Findings

The following figures are based on the analysis performed for this
project:

  -----------------------------------------------------------------------------
  Metric                                      Result Interpretation
  --------------------- ---------------------------- --------------------------
  Distinct orders                             65,752 Number of distinct orders
                                                     in the analyzed full table

  Order item value                     33,054,402.38 Sum of `Order Item Total`
                                                     across the analyzed
                                                     records

  Recorded profit                       3,966,902.97 Sum of
                                                     `Order Profit Per Order`
                                                     across the analyzed
                                                     records

  Late delivery rate                          57.29% Late rows divided by
                                                     non-cancelled delivery
                                                     rows; cancelled delivery
                                                     rows are excluded

  Non-cancelled                              172,765 Rows included in the
  delivery rows                                      late-delivery-rate
                                                     denominator

  Late delivery rows                          98,977 Rows classified as late in
                                                     the analysis
  -----------------------------------------------------------------------------

**Important:** These totals are calculated from the analyzed dataset and
should not be described as audited financial results. The sales and
profit totals include all statuses unless a section explicitly says
otherwise.

### Shipping Mode Pattern

In the analysis excluding cancelled delivery rows, the observed
late-delivery rates were:

-   First Class: 100%
-   Second Class: 79.83%
-   Same Day: 47.93%
-   Standard Class: 39.77%

These are descriptive results for this dataset. They do not prove that
shipping mode alone caused the delays.

## Data Quality & Limitations

A structural change was observed around October 2017. From November 2017
onward, records show a different quantity/order-row pattern, including
quantity values of one and approximately one row per order. Category mix
also changes around this period.

This change may affect comparisons across time. It is treated as a
data-quality limitation, and the project avoids claiming that the
observed change was caused by a particular business event.

Other interpretation notes: - Cancelled delivery rows are excluded from
the late-delivery-rate calculation. - Some dashboard sections use all
order statuses, while others focus on `COMPLETE` orders. Read each
page's scope note before comparing figures. - Recorded profit and item
value are dataset fields, not independently verified accounting
figures. - Associations in the data are descriptive and do not establish
causation.

## How to View the Report

1.  Open `reports/global_supply_chain_interactive_report.html` in a
    current browser such as Chrome or Edge.
2.  Use the report's page tabs to switch between:
    -   Executive Overview
    -   Product & Profitability
    -   Shipping & Operations
3.  Hover over charts to inspect values. Some interactive chart features
    may depend on the browser and how the report was packaged.

The HTML report is an interactive report deliverable; it is **not** a
native Power BI `.pbix` file.

## Reproducing the Analysis

1.  Obtain the dataset from its official source and preserve its
    attribution.
2.  Run the cleaning workflow to create
    `data/processed/supply_chain_cleaned.csv`.
3.  Load the cleaned data into MySQL and run the SQL analysis scripts.
4.  Open the interactive report in a browser and compare the displayed
    figures with the SQL outputs.

Exact reproduction requires the cleaning script, SQL files, and
report-generation script to be included in the repository. Add their
actual filenames and execution instructions here before publishing.

## Future Improvements

-   Add reproducible Python cleaning and report-generation scripts.
-   Commit clearly named SQL files for every KPI and analysis.
-   Add validation checks that reconcile dashboard figures with SQL
    outputs.
-   Document metric definitions and filter scopes beside each visual.
-   Consider a native Power BI `.pbix` version if the project requires a
    Power BI deliverable.

## Author

**Swethaa K**\
Entry-level data analytics portfolio project
