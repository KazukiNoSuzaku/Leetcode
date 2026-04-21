class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        # dp[c] = longest ideal subsequence ending with character c
        dp = [0] * 26
        for ch in s:
            i = ord(ch) - ord('a')
            best = 1 + max(dp[max(0, i - k): i + k + 1])
            dp[i] = max(dp[i], best)
        return max(dp)
