-- Author: Kaustav Ghosh
-- Problem: Find Users With Valid E-Mails
-- Approach: Match the whole address with one regular expression: a leading letter, then any run of letters, digits, underscore, period or dash, then the literal domain. The domain has to be lowercase, so the match is forced case-sensitive with the 'c' flag rather than relying on the default collation

SELECT *
FROM Users
WHERE REGEXP_LIKE(mail, '^[A-Za-z][A-Za-z0-9_.-]*@leetcode\\.com$', 'c');
