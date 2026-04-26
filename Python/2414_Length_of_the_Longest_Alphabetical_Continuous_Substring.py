class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        ans = run = 1
        for i in range(1, len(s)):
            if ord(s[i]) == ord(s[i - 1]) + 1:
                run += 1
                ans = max(ans, run)
            else:
                run = 1
        return ans
