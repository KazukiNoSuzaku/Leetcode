# Author: Kaustav Ghosh
# Problem: Distribute Repeating Integers
# Approach: Reduce to value frequencies; DP over customer bitmasks — for each frequency bucket, try satisfying any submask of still-unserved customers whose demand fits

from collections import Counter

class Solution(object):
    def canDistribute(self, nums, quantity):
        """
        :type nums: List[int]
        :type quantity: List[int]
        :rtype: bool
        """
        counts = list(Counter(nums).values())
        m = len(quantity)
        full = (1 << m) - 1

        # Total demand of each customer subset
        demand = [0] * (1 << m)
        for mask in range(1, 1 << m):
            low = mask & -mask
            i = low.bit_length() - 1
            demand[mask] = demand[mask ^ low] + quantity[i]

        dp = [False] * (1 << m)
        dp[0] = True
        for c in counts:
            nxt = dp[:]  # this bucket serves nobody new
            for mask in range(1 << m):
                if not dp[mask]:
                    continue
                remaining = full ^ mask
                sub = remaining
                while sub > 0:
                    if demand[sub] <= c:
                        nxt[mask | sub] = True
                    sub = (sub - 1) & remaining
            dp = nxt
            if dp[full]:
                return True
        return dp[full]
