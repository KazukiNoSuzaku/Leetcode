-- Report all the sales persons who did not have any orders related to the company named "RED".
-- Author: Kaustav Ghosh

SELECT name
FROM SalesPerson
WHERE sales_id NOT IN (
    SELECT o.sales_id
    FROM Orders o
    JOIN Company c ON o.com_id = c.com_id
    WHERE c.name = 'RED'
);
