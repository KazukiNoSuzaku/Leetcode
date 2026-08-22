# Author: Kaustav Ghosh
# Problem: Find Good Days to Rob the Bank
# Approach: Precompute, for each day, the length of the non-increasing run ending there and the non-decreasing run starting there. A day is good when both runs are at least `time` long

class Solution(object):
    def goodDaysToRobBank(self, security, time):
        """
        :type security: List[int]
        :type time: int
        :rtype: List[int]
        """
        n = len(security)
        dec = [0] * n  # non-increasing run length before/at i
        inc = [0] * n  # non-decreasing run length at/after i
        for i in range(1, n):
            if security[i] <= security[i - 1]:
                dec[i] = dec[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if security[i] <= security[i + 1]:
                inc[i] = inc[i + 1] + 1
        return [i for i in range(n) if dec[i] >= time and inc[i] >= time]
