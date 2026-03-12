# Premium problem - not available without subscription
# Author: Kaustav Ghosh
# Typical approach: DP probability of getting exactly target heads from n coins

class Solution(object):
    def probabilityOfHeads(self, prob, target):
        """
        :type prob: List[float]
        :type target: int
        :rtype: float
        """
        n = len(prob)
        dp = [0.0] * (target + 1)
        dp[0] = 1.0
        for i in range(n):
            for j in range(min(i + 1, target), -1, -1):
                dp[j] = dp[j] * (1 - prob[i])
                if j > 0:
                    dp[j] += dp[j - 1] * prob[i]
        return dp[target]
