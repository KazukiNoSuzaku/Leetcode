# Author: Kaustav Ghosh
# Problem: Stone Game III
# Approach: DP choosing 1, 2, or 3 stones, maximize score difference

class Solution(object):
    def stoneGameIII(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: str
        """
        n = len(stoneValue)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            dp[i] = float('-inf')
            total = 0
            for k in range(1, 4):
                if i + k - 1 < n:
                    total += stoneValue[i + k - 1]
                    dp[i] = max(dp[i], total - dp[i + k])
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        return "Tie"
