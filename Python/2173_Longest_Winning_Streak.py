# Author: Kaustav Ghosh
# Problem: 2173. Longest Winning Streak
# URL: https://leetcode.com/problems/longest-winning-streak/
# Premium SQL Problem
#
# SQL Approach:
# Use window functions to detect consecutive wins per player.
# Assign a group id by subtracting a row_number (within player ordered by date)
# from a win-only row_number to get contiguous groups, then count max group size.
#
# SQL Solution:
# WITH wins AS (
#     SELECT player_id, match_day,
#            ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY match_day) AS rn_all,
#            ROW_NUMBER() OVER (PARTITION BY player_id, result ORDER BY match_day) AS rn_win
#     FROM Matches
#     WHERE result = 'Win'
# ),
# streaks AS (
#     SELECT player_id, (rn_all - rn_win) AS grp, COUNT(*) AS streak_len
#     FROM wins
#     GROUP BY player_id, grp
# ),
# max_streaks AS (
#     SELECT player_id, MAX(streak_len) AS longest_streak
#     FROM streaks
#     GROUP BY player_id
# )
# SELECT p.player_id,
#        COALESCE(ms.longest_streak, 0) AS longest_streak
# FROM (SELECT DISTINCT player_id FROM Matches) p
# LEFT JOIN max_streaks ms ON p.player_id = ms.player_id
# ORDER BY p.player_id;

class Solution(object):
    pass
