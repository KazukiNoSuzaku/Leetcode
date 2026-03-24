# Author: Kaustav Ghosh
# Problem 2051: The Category of Each Member in the Store (Premium)
# SQL Problem:
# SELECT m.member_id, m.name,
#   CASE
#     WHEN COUNT(v.visit_id) = 0 THEN 'Bronze'
#     WHEN SUM(CASE WHEN p.charged_amount > 0 THEN 1 ELSE 0 END) * 100.0
#       / COUNT(v.visit_id) >= 80 THEN 'Diamond'
#     WHEN SUM(CASE WHEN p.charged_amount > 0 THEN 1 ELSE 0 END) * 100.0
#       / COUNT(v.visit_id) >= 50 THEN 'Gold'
#     ELSE 'Silver'
#   END AS category
# FROM Members m
# LEFT JOIN Visits v ON m.member_id = v.member_id
# LEFT JOIN Purchases p ON v.visit_id = p.visit_id
# GROUP BY m.member_id, m.name;

class Solution(object):
    pass
