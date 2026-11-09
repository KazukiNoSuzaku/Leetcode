-- Author: Kaustav Ghosh
-- Problem: Convert Date Format
-- Approach: The whole task is a formatting one, so a single DATE_FORMAT call builds the string: %W gives the full weekday name, %M the full month name, %e the day of the month without a leading zero, and %Y the four-digit year. Using %e rather than %d matters because the expected output writes the ninth of August as 9 and not 09. The result is aliased back to day so the column keeps the name the problem asks for.

SELECT DATE_FORMAT(day, '%W, %M %e, %Y') AS day
FROM Days;
