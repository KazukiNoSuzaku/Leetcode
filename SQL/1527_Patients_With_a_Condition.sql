-- Author: Kaustav Ghosh
-- Problem: 1527 - Patients With a Condition
-- Approach: LIKE for DIAB1 prefix in conditions column

SELECT patient_id, patient_name, conditions
FROM Patients
WHERE conditions LIKE 'DIAB1%' OR conditions LIKE '% DIAB1%';
