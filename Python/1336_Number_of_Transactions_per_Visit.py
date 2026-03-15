# Premium SQL problem - For each possible transaction count (0 to max),
# count how many users made exactly that many transactions per visit.

# Author: Kaustav Ghosh

# SQL solution:
# WITH visits AS (
#   SELECT user_id, visit_date, COUNT(transaction_date) AS cnt
#   FROM Visits v LEFT JOIN Transactions t
#     ON v.user_id = t.user_id AND v.visit_date = t.transaction_date
#   GROUP BY user_id, visit_date
# ),
# nums AS (SELECT 0 AS n UNION ALL SELECT n+1 FROM nums WHERE n < (SELECT MAX(cnt) FROM visits))
# SELECT n AS transactions_count, COUNT(user_id) AS visits_count
# FROM nums LEFT JOIN visits ON nums.n = visits.cnt
# GROUP BY n ORDER BY n;

class Solution(object):
    pass
