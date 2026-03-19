# Author: Kaustav Ghosh
# https://leetcode.com/problems/minimum-incompatibility/

class Solution(object):
    def minimumIncompatibility(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        group_size = n // k
        INF = float('inf')

        # Precompute valid subsets of size group_size
        valid = {}
        for mask in range(1, 1 << n):
            if bin(mask).count('1') != group_size:
                continue
            elements = []
            for i in range(n):
                if mask & (1 << i):
                    elements.append(nums[i])
            if len(set(elements)) != len(elements):
                continue
            valid[mask] = max(elements) - min(elements)

        full = (1 << n) - 1
        dp = [INF] * (1 << n)
        dp[0] = 0

        for mask in range(full + 1):
            if dp[mask] == INF:
                continue
            remain = full ^ mask
            sub = remain
            while sub > 0:
                if sub in valid:
                    dp[mask | sub] = min(dp[mask | sub], dp[mask] + valid[sub])
                sub = (sub - 1) & remain
        return dp[full] if dp[full] != INF else -1
