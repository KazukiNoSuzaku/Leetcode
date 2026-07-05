# Author: Kaustav Ghosh
# Problem: Number of Ways to Form a Target String Given a Dictionary
# Approach: Precount each letter per column; sweep columns left to right, extending dp[j] (ways to build target[:j]) using that column, iterating j backward so a column is used at most once

class Solution(object):
    def numWays(self, words, target):
        """
        :type words: List[str]
        :type target: str
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        cols = len(words[0])
        m = len(target)

        col_count = [[0] * 26 for _ in range(cols)]
        for word in words:
            for k, ch in enumerate(word):
                col_count[k][ord(ch) - 97] += 1

        dp = [0] * (m + 1)
        dp[0] = 1
        for col in range(cols):
            for j in range(min(col, m - 1), -1, -1):
                c = col_count[col][ord(target[j]) - 97]
                if c:
                    dp[j + 1] = (dp[j + 1] + dp[j] * c) % MOD
        return dp[m]
