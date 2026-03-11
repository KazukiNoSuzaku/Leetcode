# You are given an integer array nums. Two players are playing a game with this array.
# Player 1 and player 2 take turns picking from the ends. Return true if player 1 can win.

# Author: Kaustav Ghosh

class Solution(object):
    def predictTheWinner(self, nums):
        n = len(nums)
        dp = nums[:]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i] = max(nums[i] - dp[i+1], nums[j] - dp[i])
        return dp[0] >= 0
