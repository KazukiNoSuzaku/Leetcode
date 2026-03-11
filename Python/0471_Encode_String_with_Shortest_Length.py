# Given a string s, encode the string such that its encoded length is the shortest.
# The encoding rule is: k[encoded_string], where the encoded_string inside the square
# brackets is being repeated exactly k times.

# Author: Kaustav Ghosh

class Solution(object):
    def encode(self, s):
        n = len(s)
        dp = [[''] * n for _ in range(n)]
        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                sub = s[i:j+1]
                dp[i][j] = sub
                # Try repeated substring compression
                t = sub + sub
                pos = t.find(sub, 1)
                if pos < len(sub):
                    k = len(sub) // pos
                    compressed = '%d[%s]' % (k, dp[i][i+pos-1])
                    if len(compressed) < len(dp[i][j]):
                        dp[i][j] = compressed
                # Try split
                for m in range(i, j):
                    combo = dp[i][m] + dp[m+1][j]
                    if len(combo) < len(dp[i][j]):
                        dp[i][j] = combo
        return dp[0][n-1]
