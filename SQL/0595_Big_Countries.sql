-- A country is big if it has an area of at least three million or a population of at least 25 million.
-- Author: Kaustav Ghosh

SELECT name, population, area
FROM World
WHERE area >= 3000000 OR population >= 25000000;
