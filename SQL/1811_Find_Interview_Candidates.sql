-- Author: Kaustav Ghosh
-- Problem: Find Interview Candidates
-- Approach: The medals sit in three columns, so they are first stacked into one row per medal won, which lets both conditions be asked of the same shape of data. Three consecutive contests are then detected by joining that stacked table to itself twice on the same user with contest ids one and two higher, which works because the problem guarantees consecutive contests carry consecutive ids with none skipped. The gold condition is a plain count on the original table. Both are used as membership tests so a user who qualifies several ways over is still reported once.

WITH Medals AS (
    SELECT contest_id, gold_medal AS user_id FROM Contests
    UNION ALL
    SELECT contest_id, silver_medal FROM Contests
    UNION ALL
    SELECT contest_id, bronze_medal FROM Contests
)
SELECT u.name, u.mail
FROM Users AS u
WHERE u.user_id IN (
        SELECT first.user_id
        FROM Medals AS first
        JOIN Medals AS second
            ON second.user_id = first.user_id
           AND second.contest_id = first.contest_id + 1
        JOIN Medals AS third
            ON third.user_id = first.user_id
           AND third.contest_id = first.contest_id + 2
    )
   OR u.user_id IN (
        SELECT gold_medal
        FROM Contests
        GROUP BY gold_medal
        HAVING COUNT(*) >= 3
    );
