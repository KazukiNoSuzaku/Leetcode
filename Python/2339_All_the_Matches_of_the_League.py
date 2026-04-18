# Author: Kaustav Ghosh
# 2339. All the Matches of the League
# https://leetcode.com/problems/all-the-matches-of-the-league/
# Premium SQL: self-join Teams table to generate all home/away match combinations

# SQL Solution:
# SELECT t1.team_name AS home_team,
#        t2.team_name AS away_team
# FROM Teams t1
# JOIN Teams t2
#   ON t1.team_name != t2.team_name;

class Solution(object):
    pass
