# Author: Kaustav Ghosh
# Problem 1843: Suspicious Bank Accounts (Premium)
# SQL Problem - Solution in comments
#
# SELECT DISTINCT a.account_id
# FROM Accounts a
# JOIN Transactions t ON a.account_id = t.account_id
# WHERE t.type = 'Creditor'
# GROUP BY a.account_id, DATE_FORMAT(t.day, '%Y-%m')
# HAVING SUM(t.amount) > a.max_income
# ORDER BY a.account_id;
#
# (Need two consecutive months - full solution uses window/lag)
# WITH monthly AS (
#     SELECT a.account_id,
#            DATE_FORMAT(t.day, '%Y-%m') AS month,
#            PERIOD_DIFF(DATE_FORMAT(t.day, '%Y%m'), '000000') AS m_num
#     FROM Accounts a
#     JOIN Transactions t ON a.account_id = t.account_id
#     WHERE t.type = 'Creditor'
#     GROUP BY a.account_id, DATE_FORMAT(t.day, '%Y-%m')
#     HAVING SUM(t.amount) > a.max_income
# )
# SELECT DISTINCT m1.account_id
# FROM monthly m1
# JOIN monthly m2 ON m1.account_id = m2.account_id
#     AND m1.m_num = m2.m_num - 1
# ORDER BY m1.account_id;

class Solution(object):
    pass
