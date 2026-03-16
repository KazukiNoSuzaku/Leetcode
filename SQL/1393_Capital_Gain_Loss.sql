-- Author: Kaustav Ghosh
-- Problem: Capital Gain/Loss
-- Approach: SUM with CASE WHEN for buy/sell operations

SELECT stock_name,
       SUM(CASE WHEN operation = 'Sell' THEN price ELSE -price END) AS capital_gain_loss
FROM Stocks
GROUP BY stock_name;
