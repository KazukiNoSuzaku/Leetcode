# Author: Kaustav Ghosh
# Problem: 2175. The Change in Global Rankings
# URL: https://leetcode.com/problems/the-change-in-global-rankings/
# Premium SQL Problem
#
# SQL Approach:
# Compute old rank using RANK() on the original rating, then compute new rank
# using RANK() on (rating + points_change), and return the difference.
#
# SQL Solution:
# WITH old_ranks AS (
#     SELECT team_id,
#            RANK() OVER (ORDER BY rating DESC) AS old_rank
#     FROM TeamPoints
# ),
# new_ranks AS (
#     SELECT t.team_id,
#            RANK() OVER (ORDER BY (t.rating + p.points_change) DESC) AS new_rank
#     FROM TeamPoints t
#     JOIN PointsChange p ON t.team_id = p.team_id
# )
# SELECT o.team_id,
#        t.name,
#        (o.old_rank - n.new_rank) AS rank_diff
# FROM old_ranks o
# JOIN new_ranks n ON o.team_id = n.team_id
# JOIN TeamPoints t ON o.team_id = t.team_id;

class Solution(object):
    pass
