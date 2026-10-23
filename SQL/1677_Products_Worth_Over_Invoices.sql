-- Author: Kaustav Ghosh
-- Problem: Product's Worth Over Invoices
-- Approach: The totals are a straight grouped sum of the four invoice columns, but the request is for all products, so a product with no invoices at all must still appear; that calls for a LEFT JOIN, and because the join then produces a row whose invoice columns are entirely NULL, every SUM has to be wrapped so it reports zero rather than NULL. Grouping by the product id rather than the name is the safer key even though names are stated to be unique, and the ordering is by name as asked.

SELECT p.name,
       COALESCE(SUM(i.rest), 0) AS rest,
       COALESCE(SUM(i.paid), 0) AS paid,
       COALESCE(SUM(i.canceled), 0) AS canceled,
       COALESCE(SUM(i.refunded), 0) AS refunded
FROM Product p
LEFT JOIN Invoice i ON i.product_id = p.product_id
GROUP BY p.product_id, p.name
ORDER BY p.name;
