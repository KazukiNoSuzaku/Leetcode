from bisect import bisect_left

class Solution:
    def maximizeWin(self, prizePositions: list[int], k: int) -> int:
        # dp[i] = best one-segment count using only first i prizes; sweep right endpoint with binary search.
        n = len(prizePositions)
        dp = [0] * (n + 1)
        ans = 0
        for r in range(n):
            l = bisect_left(prizePositions, prizePositions[r] - k)
            count = r - l + 1
            ans = max(ans, dp[l] + count)
            dp[r + 1] = max(dp[r], count)
        return ans
