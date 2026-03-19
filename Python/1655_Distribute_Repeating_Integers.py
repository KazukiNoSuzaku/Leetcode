# Author: Kaustav Ghosh
# https://leetcode.com/problems/distribute-repeating-integers/

from collections import Counter

class Solution(object):
    def canDistribute(self, nums, quantity):
        """
        :type nums: List[int]
        :type quantity: List[int]
        :rtype: bool
        """
        counts = list(Counter(nums).values())
        quantity.sort(reverse=True)
        m = len(quantity)

        # Precompute subset sums of quantity
        subset_sum = [0] * (1 << m)
        for mask in range(1, 1 << m):
            for i in range(m):
                if mask & (1 << i):
                    subset_sum[mask] = subset_sum[mask ^ (1 << i)] + quantity[i]
                    break

        n = len(counts)
        full = (1 << m) - 1
        dp = [0] * (1 << m)
        dp[0] = n  # any count can satisfy empty set

        # dp[mask] = how many counts remain after satisfying mask
        # Actually use bitmask DP differently
        # dp[mask] = True if we can satisfy customers in mask
        dp = [False] * (1 << m)
        dp[0] = True

        for c in counts:
            # For each count, try to assign subsets to it
            new_dp = dp[:]
            for mask in range(full, 0, -1):
                if new_dp[mask]:
                    continue
                sub = mask
                while sub > 0:
                    if subset_sum[sub] <= c and dp[mask ^ sub]:
                        new_dp[mask] = True
                        break
                    sub = (sub - 1) & mask
            dp = new_dp

        return dp[full]
