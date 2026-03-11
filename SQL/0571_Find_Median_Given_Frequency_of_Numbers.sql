-- Find the median of all numbers given a frequency table.
-- Author: Kaustav Ghosh

SELECT AVG(num) AS median
FROM (
    SELECT num,
           SUM(frequency) OVER (ORDER BY num) AS cum_freq,
           SUM(frequency) OVER () / 2.0 AS half_total
    FROM Numbers
) t
WHERE cum_freq - frequency < half_total AND cum_freq >= half_total;
