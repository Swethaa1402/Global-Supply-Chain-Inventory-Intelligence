-- Delivery performance
-- Late-delivery rate excludes rows with cancelled shipping/delivery.
-- Assumes table: supply_chain_cleaned_full

USE supply_chain_intelligence;

SELECT
    COUNT(*) AS non_cancelled_delivery_rows,
    SUM(CASE WHEN `Delivery Status` = 'Late delivery' THEN 1 ELSE 0 END) AS late_delivery_rows,
    ROUND(
        100.0 * SUM(CASE WHEN `Delivery Status` = 'Late delivery' THEN 1 ELSE 0 END)
        / NULLIF(SUM(CASE WHEN `Delivery Status` <> 'Shipping canceled' THEN 1 ELSE 0 END), 0),
        2
    ) AS late_delivery_rate_pct
FROM supply_chain_cleaned_full
WHERE `Delivery Status` <> 'Shipping canceled';

-- Shipping-mode late rate, excluding cancelled rows.
SELECT
    `Shipping Mode`,
    COUNT(*) AS non_cancelled_rows,
    SUM(CASE WHEN `Delivery Status` = 'Late delivery' THEN 1 ELSE 0 END) AS late_rows,
    ROUND(
        100.0 * SUM(CASE WHEN `Delivery Status` = 'Late delivery' THEN 1 ELSE 0 END)
        / NULLIF(COUNT(*), 0),
        2
    ) AS late_rate_pct
FROM supply_chain_cleaned_full
WHERE `Delivery Status` <> 'Shipping canceled'
GROUP BY `Shipping Mode`
ORDER BY late_rate_pct DESC;
