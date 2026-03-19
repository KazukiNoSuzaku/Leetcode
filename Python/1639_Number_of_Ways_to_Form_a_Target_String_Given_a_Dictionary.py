# Author: Kaustav Ghosh
# https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/

class Solution(object):
    def numWays(self, words, target):
        """
        :type words: List[str]
        :type target: str
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        m = len(target)
        k = len(words[0])

        # Count frequency of each char at each position
        freq = [[0] * 26 for _ in range(k)]
        for w in words:
            for j, c in enumerate(w):
                freq[j][ord(c) - ord('a')] += 1

        dp = [0] * (m + 1)
        dp[0] = 1
        for j in range(k):
            for i in range(min(m, j + 1), 0, -1):
                c = ord(target[i - 1]) - ord('a')
                dp[i] = (dp[i] + dp[i - 1] * freq[j][c]) % MOD
        return dp[m]
