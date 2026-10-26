-- Completed-order metrics
-- This query explicitly scopes the figures to COMPLETE order status.
-- Assumes table: supply_chain_cleaned_full

USE supply_chain_intelligence;

SELECT
    COUNT(DISTINCT `Order Id`) AS completed_distinct_orders,
    ROUND(SUM(`Order Item Total`), 2) AS completed_order_item_value,
    ROUND(SUM(`Order Profit Per Order`), 2) AS completed_recorded_profit
FROM supply_chain_cleaned_full
WHERE `Order Status` = 'COMPLETE';
