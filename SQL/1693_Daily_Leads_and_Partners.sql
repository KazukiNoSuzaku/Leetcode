-- Author: Kaustav Ghosh
-- Problem: Daily Leads and Partners
-- Approach: The table is explicitly allowed to contain duplicate rows, so the counts have to be of distinct ids rather than of rows; COUNT(DISTINCT ...) is therefore doing the real work here and a plain COUNT would over-report every repeated lead or partner. Grouping by both the date and the make matches the requested granularity, and the two distinct counts are independent of one another, so a single grouped pass produces both.

SELECT date_id,
       make_name,
       COUNT(DISTINCT lead_id) AS unique_leads,
       COUNT(DISTINCT partner_id) AS unique_partners
FROM DailySales
GROUP BY date_id, make_name;
