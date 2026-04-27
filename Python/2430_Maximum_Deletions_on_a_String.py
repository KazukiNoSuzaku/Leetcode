class Solution:
    def deleteString(self, s: str) -> int:
        n = len(s)
        # lcp[i][j] = length of longest common prefix of s[i:] and s[j:]
        lcp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] == s[j]:
                    lcp[i][j] = lcp[i + 1][j + 1] + 1

        dp = [1] * n
        for i in range(n - 2, -1, -1):
            for k in range(1, (n - i) // 2 + 1):
                if lcp[i][i + k] >= k:
                    dp[i] = max(dp[i], 1 + dp[i + k])
        return dp[0]
