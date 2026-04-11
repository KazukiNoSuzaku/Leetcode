# Author: Kaustav Ghosh
# Problem: 2266. Count Number of Texts
# URL: https://leetcode.com/problems/count-number-of-texts/
# Difficulty: Medium
#
# Approach:
# DP where dp[i] = number of ways to decode pressedKeys[:i].
# Keys 7 and 9 allow up to 4 consecutive presses, others up to 3.
# For each position, look back up to the max allowed consecutive same digits.

class Solution(object):
    def countTexts(self, pressedKeys):
        """
        :type pressedKeys: str
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        n = len(pressedKeys)
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            max_press = 4 if pressedKeys[i - 1] in ('7', '9') else 3
            for j in range(1, max_press + 1):
                if i - j < 0:
                    break
                if pressedKeys[i - j] != pressedKeys[i - 1]:
                    break
                dp[i] = (dp[i] + dp[i - j]) % MOD
        return dp[n]
