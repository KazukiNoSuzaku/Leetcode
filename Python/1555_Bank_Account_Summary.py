# Author: Kaustav Ghosh
# Problem: 1555 - Bank Account Summary (Premium SQL)
# Approach: Join transactions, compute balance, flag those below credit limit

# SQL Solution (Premium Problem):
# SELECT u.user_id, u.user_name, u.credit + COALESCE(SUM(
#     CASE
#         WHEN t.paid_by = u.user_id THEN -t.amount
#         WHEN t.paid_to = u.user_id THEN t.amount
#         ELSE 0
#     END
# ), 0) AS credit,
# CASE WHEN u.credit + COALESCE(SUM(
#     CASE
#         WHEN t.paid_by = u.user_id THEN -t.amount
#         WHEN t.paid_to = u.user_id THEN t.amount
#         ELSE 0
#     END
# ), 0) < 0 THEN 'Yes' ELSE 'No' END AS credit_limit_breached
# FROM Users u
# LEFT JOIN Transactions t ON t.paid_by = u.user_id OR t.paid_to = u.user_id
# GROUP BY u.user_id, u.user_name, u.credit;

class Solution(object):
    pass
