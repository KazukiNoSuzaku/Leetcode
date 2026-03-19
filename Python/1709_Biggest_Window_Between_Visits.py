# Author: Kaustav Ghosh
# https://leetcode.com/problems/biggest-window-between-visits/
# Premium SQL Problem
#
# SELECT user_id,
#        MAX(DATEDIFF(next_visit, visit_date)) AS biggest_window
# FROM (
#     SELECT user_id, visit_date,
#            LEAD(visit_date, 1, '2021-01-01') OVER (PARTITION BY user_id ORDER BY visit_date) AS next_visit
#     FROM UserVisits
# ) t
# GROUP BY user_id;

class Solution(object):
    pass
