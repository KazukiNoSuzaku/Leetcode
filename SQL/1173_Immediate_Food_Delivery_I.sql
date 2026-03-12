-- Author: Kaustav Ghosh
-- Percentage of immediate orders (order_date = customer_pref_delivery_date)

SELECT ROUND(
    SUM(CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
    2
) AS immediate_percentage
FROM Delivery;
