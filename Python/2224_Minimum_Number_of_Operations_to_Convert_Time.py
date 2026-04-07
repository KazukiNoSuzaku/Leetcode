# Author: Kaustav Ghosh
# Problem: 2224. Minimum Number of Operations to Convert Time
# URL: https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/
# Difficulty: Easy
#
# Approach:
# Convert both times to total minutes. Greedily subtract the largest allowed
# increment (60, 15, 5, 1) that fits into the remaining difference, counting
# each use as one operation.

class Solution(object):
    def convertTime(self, current, correct):
        """
        :type current: str
        :type correct: str
        :rtype: int
        """
        def to_minutes(t):
            h, m = t.split(':')
            return int(h) * 60 + int(m)

        diff = to_minutes(correct) - to_minutes(current)
        ops = 0
        for step in [60, 15, 5, 1]:
            ops += diff // step
            diff %= step
        return ops
