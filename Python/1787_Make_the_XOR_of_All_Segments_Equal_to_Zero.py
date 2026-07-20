# Author: Kaustav Ghosh
# Problem: Make the XOR of All Segments Equal to Zero
# Approach: The condition forces the array to be periodic with period k, so group indices by i%k into columns. DP over columns tracks the min changes for each running XOR of chosen column values; the answer needs that XOR to be 0

from collections import Counter

class Solution(object):
    def minChanges(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        INF = float('inf')
        MAXV = 1024  # values are < 2^10

        columns = [Counter() for _ in range(k)]
        sizes = [0] * k
        for i, x in enumerate(nums):
            columns[i % k][x] += 1
            sizes[i % k] += 1

        dp = [INF] * MAXV
        dp[0] = 0
        for c in range(k):
            best = min(dp)
            # Baseline: overwrite the whole column, reaching any XOR at full cost
            ndp = [best + sizes[c]] * MAXV
            for v, cnt in columns[c].items():
                keep_cost = sizes[c] - cnt  # keep the v's, change the rest
                for y in range(MAXV):
                    if dp[y ^ v] + keep_cost < ndp[y]:
                        ndp[y] = dp[y ^ v] + keep_cost
            dp = ndp
        return dp[0]
