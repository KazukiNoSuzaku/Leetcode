# Author: Kaustav Ghosh
# 1048. Longest String Chain
# https://leetcode.com/problems/longest-string-chain/

class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words.sort(key=len)
        dp = {}
        best = 1
        for word in words:
            dp[word] = 1
            for i in range(len(word)):
                prev = word[:i] + word[i+1:]
                if prev in dp:
                    dp[word] = max(dp[word], dp[prev] + 1)
            best = max(best, dp[word])
        return best
