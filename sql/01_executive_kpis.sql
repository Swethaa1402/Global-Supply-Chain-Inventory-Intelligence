-- Executive KPIs
-- Run against the full cleaned table in the supply_chain_intelligence database.
-- Assumes table: supply_chain_cleaned_full
-- These metrics are descriptive dataset totals, not audited financial results.

USE supply_chain_intelligence;

SELECT
    COUNT(DISTINCT `Order Id`) AS distinct_orders,
    ROUND(SUM(`Order Item Total`), 2) AS total_order_item_value,
    ROUND(SUM(`Order Profit Per Order`), 2) AS total_recorded_profit
FROM supply_chain_cleaned_full;

-- Order-status scope: inspect counts before comparing status-filtered metrics.
SELECT
    `Order Status`,
    COUNT(*) AS row_count,
    COUNT(DISTINCT `Order Id`) AS distinct_orders
FROM supply_chain_cleaned_full
GROUP BY `Order Status`
ORDER BY row_count DESC;
