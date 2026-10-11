-- Author: Kaustav Ghosh
-- Problem: Warehouse Manager
-- Approach: The unit count lives in Warehouse while the dimensions live in Products, so joining on product_id brings both onto one row, and a single unit's volume is the product of its three dimensions multiplied by how many units are stored; summing that per warehouse name gives the occupied volume. An inner join is the right kind here because a warehouse row always references a real product, and warehouses with no rows at all simply have no volume to report.

SELECT w.name AS warehouse_name,
       SUM(p.Width * p.Length * p.Height * w.units) AS volume
FROM Warehouse w
JOIN Products p ON w.product_id = p.product_id
GROUP BY w.name;
