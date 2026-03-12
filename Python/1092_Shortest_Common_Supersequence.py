# Author: Kaustav Ghosh
# 1092. Shortest Common Supersequence
# https://leetcode.com/problems/shortest-common-supersequence/

class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        m, n = len(str1), len(str2)
        dp = [[""] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = str1[:i]
        for j in range(n + 1):
            dp[0][j] = str2[:j]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + str1[i-1]
                else:
                    if len(dp[i-1][j]) < len(dp[i][j-1]):
                        dp[i][j] = dp[i-1][j] + str1[i-1]
                    else:
                        dp[i][j] = dp[i][j-1] + str2[j-1]
        return dp[m][n]
