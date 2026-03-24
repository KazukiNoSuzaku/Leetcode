# Author: Kaustav Ghosh
# Problem 2026: Low-Quality Problems (Premium)
#
# SQL Solution (Premium):
# SELECT problem_id
# FROM Problems
# WHERE likes / (likes + dislikes) * 100 < 60
# ORDER BY problem_id;
#
# Or using: WHERE likes * 100 < (likes + dislikes) * 60

class Solution(object):
    pass
