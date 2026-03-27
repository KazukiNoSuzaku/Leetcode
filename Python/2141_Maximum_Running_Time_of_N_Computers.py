# Author: Kaustav Ghosh
# https://leetcode.com/problems/maximum-running-time-of-n-computers/

class Solution(object):
    def maxRunTime(self, n, batteries):
        """
        :type n: int
        :type batteries: List[int]
        :rtype: int
        """
        lo, hi = 1, sum(batteries) // n

        while lo < hi:
            mid = (lo + hi + 1) // 2
            # Each battery contributes at most mid minutes
            total = sum(min(b, mid) for b in batteries)
            if total >= n * mid:
                lo = mid
            else:
                hi = mid - 1

        return lo
