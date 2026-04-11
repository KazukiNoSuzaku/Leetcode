# Author: Kaustav Ghosh
# Problem: 2274. Maximum Consecutive Floors Without Special Floors
# URL: https://leetcode.com/problems/maximum-consecutive-floors-without-special-floors/
# Difficulty: Medium
#
# Approach:
# Sort the special floors. The answer is the maximum gap between consecutive
# special floors (and the edges bottom/top).

class Solution(object):
    def maxConsecutive(self, bottom, top, special):
        """
        :type bottom: int
        :type top: int
        :type special: List[int]
        :rtype: int
        """
        special.sort()
        best = special[0] - bottom
        for i in range(1, len(special)):
            best = max(best, special[i] - special[i - 1] - 1)
        best = max(best, top - special[-1])
        return best
