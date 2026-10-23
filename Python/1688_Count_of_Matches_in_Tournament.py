# Author: Kaustav Ghosh
# Problem: Count of Matches in Tournament
# Approach: Every match eliminates exactly one team and the tournament ends with one team standing, so the number of matches is forced to be one fewer than the number of teams regardless of how the byes fall in odd rounds. That makes the simulation unnecessary.

class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        return n - 1
