# Author: Kaustav Ghosh
# Problem: Minimum Cost to Separate Sentence Into Rows
# Approach: DP over the starting word. dp[i] is the minimum cost to lay out words[i:]. From i, greedily extend a row while its length (words plus single spaces) fits k; a non-final row costs (k-length)^2, the final row is free. Take the minimum over all row breaks

class Solution(object):
    def minimumCost(self, sentence, k):
        """
        :type sentence: str
        :type k: int
        :rtype: int
        """
        words = sentence.split()
        n = len(words)
        INF = float('inf')
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            dp[i] = INF
            length = 0
            for j in range(i, n):
                length += len(words[j]) + (0 if j == i else 1)
                if length > k:
                    break
                cost = 0 if j == n - 1 else (k - length) ** 2
                dp[i] = min(dp[i], cost + dp[j + 1])
        return dp[0]
