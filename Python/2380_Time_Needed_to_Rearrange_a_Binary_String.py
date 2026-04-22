class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        # dp[i] = steps for the '1' at position i to pass all preceding '0's
        # dp[i] = max(dp[i-1] + 1, zeros_count) when s[i]=='1' and zeros_count > 0
        ans = zeros = 0
        for i, ch in enumerate(s):
            if ch == '0':
                zeros += 1
            elif zeros:
                ans = max(ans + 1, zeros)
        return ans
