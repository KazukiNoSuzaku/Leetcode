-- Author: Kaustav Ghosh
-- Problem: The Most Recent Orders for Each Product
-- Approach: For every order, compare its date with the latest order date recorded for that same product; keeping the matches returns all orders tied on that latest date, which is what "the most recent order(s)" asks for. Products never ordered drop out naturally through the join

SELECT p.product_name, p.product_id, o.order_id, o.order_date
FROM Orders o
JOIN Products p ON o.product_id = p.product_id
WHERE o.order_date = (
    SELECT MAX(o2.order_date)
    FROM Orders o2
    WHERE o2.product_id = o.product_id
)
ORDER BY p.product_name ASC, p.product_id ASC, o.order_id ASC;
