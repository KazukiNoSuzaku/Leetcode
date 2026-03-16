# Author: Kaustav Ghosh
# Problem: Form Largest Integer With Digits That Add up to Target
# Approach: DP to maximize number of digits first, then maximize digit values

class Solution(object):
    def largestNumber(self, cost, target):
        """
        :type cost: List[int]
        :type target: int
        :rtype: str
        """
        dp = [float('-inf')] * (target + 1)
        dp[0] = 0
        for t in range(1, target + 1):
            for i in range(9):
                if cost[i] <= t:
                    dp[t] = max(dp[t], dp[t - cost[i]] + 1)

        if dp[target] < 0:
            return "0"

        result = []
        remaining = target
        for digit in range(9, 0, -1):
            while remaining >= cost[digit - 1] and dp[remaining] == dp[remaining - cost[digit - 1]] + 1:
                result.append(str(digit))
                remaining -= cost[digit - 1]

        return ''.join(result)
