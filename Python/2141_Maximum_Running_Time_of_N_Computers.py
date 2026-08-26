# Author: Kaustav Ghosh
# Problem: Maximum Running Time of N Computers
# Approach: Binary search the runtime T. Since only one computer draws from a battery at a time, a battery can supply at most min(charge, T) minutes over a T-minute run. Running n computers for T minutes needs total usable charge >= n*T

class Solution(object):
    def maxRunTime(self, n, batteries):
        """
        :type n: int
        :type batteries: List[int]
        :rtype: int
        """
        def feasible(t):
            return sum(min(b, t) for b in batteries) >= n * t

        lo, hi = 0, sum(batteries) // n
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if feasible(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
