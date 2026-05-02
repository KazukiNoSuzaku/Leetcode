"""
SQL problem — Form a Chemical Bond.

Table: Elements(symbol VARCHAR, type ENUM('Metal','Nonmetal','Noble Gas'), electron_affinity INT)

Return all (metal, nonmetal) pairs that can form a chemical bond.
Order by metal symbol, then nonmetal symbol.

SELECT m.symbol AS metal,
       nm.symbol AS nonmetal
FROM Elements m
CROSS JOIN Elements nm
WHERE m.type = 'Metal'
  AND nm.type = 'Nonmetal'
ORDER BY metal, nonmetal;
"""
