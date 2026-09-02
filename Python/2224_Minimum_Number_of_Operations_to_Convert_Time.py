# Author: Kaustav Ghosh
# Problem: Minimum Number of Operations to Convert Time
# Approach: Compute the minute difference between the two times, then greedily use the largest increments first (60, 15, 5, 1). Because each increment is a multiple of the next, greedy is optimal

class Solution(object):
    def convertTime(self, current, correct):
        """
        :type current: str
        :type correct: str
        :rtype: int
        """
        def minutes(t):
            h, m = t.split(':')
            return int(h) * 60 + int(m)

        diff = minutes(correct) - minutes(current)
        ops = 0
        for step in (60, 15, 5, 1):
            ops += diff // step
            diff %= step
        return ops
