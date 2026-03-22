# Author: Kaustav Ghosh
# Premium problem - Leetflex Banned Accounts
# SQL: Find accounts that logged in from two different IPs on the same day
# SELECT DISTINCT l1.account_id
# FROM LogInfo l1 JOIN LogInfo l2
# ON l1.account_id = l2.account_id
# AND l1.ip_address != l2.ip_address
# AND l1.login BETWEEN l2.login AND l2.logout;

class Solution(object):
    pass
