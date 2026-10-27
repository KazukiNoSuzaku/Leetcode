-- Author: Kaustav Ghosh
-- Problem: Count Apples and Oranges
-- Approach: Every box counts, including the ones holding no chest, so the join has to be a LEFT JOIN from Boxes; an inner join would silently drop boxes whose chest_id is NULL and undercount the total. That NULL chest also means the chest's columns arrive as NULL for those rows, and since NULL added to anything is NULL, each chest column is coalesced to zero before being added rather than afterwards. The result is a single grand total, so there is no grouping at all.

SELECT SUM(b.apple_count + COALESCE(c.apple_count, 0)) AS apple_count,
       SUM(b.orange_count + COALESCE(c.orange_count, 0)) AS orange_count
FROM Boxes b
LEFT JOIN Chests c ON c.chest_id = b.chest_id;
