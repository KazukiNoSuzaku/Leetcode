# Author: Kaustav Ghosh
# Problem: Count of Matches in Tournament
# Approach: Every match eliminates exactly one team and one champion remains, so it always takes n-1 matches

class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        return n - 1
