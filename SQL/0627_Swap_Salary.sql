-- Swap all 'm' and 'f' values in the sex column of the Salary table in one UPDATE.
-- Author: Kaustav Ghosh

UPDATE Salary
SET sex = CASE WHEN sex = 'm' THEN 'f' ELSE 'm' END;
