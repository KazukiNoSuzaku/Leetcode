# Return the minimum number of insertions to make a string a palindrome.
# Answer = n - LPS (longest palindromic subsequence).

# Author: Kaustav Ghosh

class Solution(object):
    def minInsertions(self, s):
        n = len(s)
        # LPS = LCS of s and reverse(s)
        t = s[::-1]
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return n - dp[n][n]
