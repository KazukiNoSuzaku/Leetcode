# Author: Kaustav Ghosh
# Problem: Minimum Incompatibility
# Approach: Precompute max-min cost of every valid same-size distinct group (bitmask), then DP over masks combining groups, forcing the lowest free element into the next group to prune

from collections import Counter

class Solution(object):
    def minimumIncompatibility(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        size = n // k
        if size == 1:
            return 0
        if max(Counter(nums).values()) > k:
            return -1

        full = (1 << n) - 1
        group_cost = {}
        for mask in range(1 << n):
            if bin(mask).count('1') != size:
                continue
            vals = [nums[i] for i in range(n) if mask >> i & 1]
            if len(set(vals)) == size:
                group_cost[mask] = max(vals) - min(vals)

        INF = float('inf')
        dp = [INF] * (1 << n)
        dp[0] = 0
        for mask in range(1 << n):
            if dp[mask] == INF:
                continue
            rem = full ^ mask
            low = rem & (-rem)  # force the lowest free element into the next group
            sub = rem
            while sub:
                if sub & low and sub in group_cost:
                    cand = dp[mask] + group_cost[sub]
                    if cand < dp[mask | sub]:
                        dp[mask | sub] = cand
                sub = (sub - 1) & rem

        return dp[full] if dp[full] != INF else -1
