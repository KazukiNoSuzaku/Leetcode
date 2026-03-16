# Author: Kaustav Ghosh
# Problem: Parallel Courses II (Premium)
# Approach: Bitmask DP prerequisite scheduling, pick up to k courses per semester

class Solution(object):
    def minNumberOfSemesters(self, n, relations, k):
        """
        :type n: int
        :type relations: List[List[int]]
        :type k: int
        :rtype: int
        """
        prereq = [0] * n
        for u, v in relations:
            prereq[v - 1] |= 1 << (u - 1)

        full = (1 << n) - 1
        dp = [n] * (full + 1)
        dp[0] = 0

        for mask in range(full + 1):
            if dp[mask] == n:
                continue
            # Find available courses
            available = 0
            for i in range(n):
                if not (mask & (1 << i)) and (prereq[i] & mask) == prereq[i]:
                    available |= 1 << i
            # Enumerate subsets of available with at most k bits
            subset = available
            while subset > 0:
                if bin(subset).count('1') <= k:
                    dp[mask | subset] = min(dp[mask | subset], dp[mask] + 1)
                subset = (subset - 1) & available
        return dp[full]
