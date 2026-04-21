# Premium SQL problem
# Find the invoice_id with maximum total price, then return all its line items.
#
# WITH totals AS (
#     SELECT invoice_id, SUM(quantity * price_per_unit) AS total
#     FROM Purchases
#     GROUP BY invoice_id
# )
# SELECT p.product_id, p.quantity, p.price_per_unit * p.quantity AS price
# FROM Purchases p
# WHERE p.invoice_id = (
#     SELECT invoice_id FROM totals ORDER BY total DESC, invoice_id ASC LIMIT 1
# )
# ORDER BY p.product_id
