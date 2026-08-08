# Author: Kaustav Ghosh
# Problem: Minimum Total Space Wasted With K Resizing Operations
# Approach: With k resizes the timeline splits into at most k+1 constant-size segments, each sized to its own maximum. A segment [l, r] wastes max*len - sum. DP over prefix length and number of segments, trying every split point

class Solution(object):
    def minSpaceWastedKResizing(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        prefix = [0] * (n + 1)
        for i, v in enumerate(nums):
            prefix[i + 1] = prefix[i] + v

        def cost(l, r):  # inclusive
            mx = max(nums[l:r + 1])
            return mx * (r - l + 1) - (prefix[r + 1] - prefix[l])

        INF = float('inf')
        segments = min(k + 1, n)
        # dp[c][i] = min waste covering first i elements using c segments
        dp = [[INF] * (n + 1) for _ in range(segments + 1)]
        dp[0][0] = 0
        for c in range(1, segments + 1):
            for i in range(1, n + 1):
                for p in range(c - 1, i):        # previous prefix length
                    if dp[c - 1][p] < INF:
                        cand = dp[c - 1][p] + cost(p, i - 1)
                        if cand < dp[c][i]:
                            dp[c][i] = cand
        return min(dp[c][n] for c in range(1, segments + 1))
