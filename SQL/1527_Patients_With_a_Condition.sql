-- Author: Kaustav Ghosh
-- Problem: Patients With a Condition
-- Approach: The condition codes are space separated, so a Type I diabetes code either opens the string or follows a space; matching 'DIAB1%' and '% DIAB1%' avoids false hits like SADIAB100

SELECT *
FROM Patients
WHERE conditions LIKE 'DIAB1%'
   OR conditions LIKE '% DIAB1%';
