# Author: Kaustav Ghosh
# https://leetcode.com/problems/minimum-total-space-wasted-with-k-resizing-operations/

class Solution(object):
    def minSpaceWastedKResizing(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        # Precompute waste for segment [i, j]
        # waste[i][j] = max(nums[i..j]) * (j-i+1) - sum(nums[i..j])
        waste = [[0] * n for _ in range(n)]
        for i in range(n):
            mx = 0
            total = 0
            for j in range(i, n):
                mx = max(mx, nums[j])
                total += nums[j]
                waste[i][j] = mx * (j - i + 1) - total

        # dp[i][j] = min waste for nums[0..i] with j resizes
        INF = float('inf')
        dp = [[INF] * (k + 2) for _ in range(n)]
        for i in range(n):
            dp[i][0] = waste[0][i]
            for j in range(1, k + 1):
                for p in range(i):
                    if dp[p][j - 1] < INF:
                        dp[i][j] = min(dp[i][j], dp[p][j - 1] + waste[p + 1][i])

        return min(dp[n - 1][:k + 1])
