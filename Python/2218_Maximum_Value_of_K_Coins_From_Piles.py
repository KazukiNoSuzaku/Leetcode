# Author: Kaustav Ghosh
# Problem: 2218. Maximum Value of K Coins From Piles
# URL: https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/
# Difficulty: Hard
#
# Approach:
# DP where dp[j] = max coins obtainable using exactly j picks from the piles
# processed so far. For each pile, consider taking 0..min(len(pile), j) coins
# from the top (prefix sums make this O(pile_size) per state). Update dp in
# reverse to avoid using the same pile twice.

class Solution(object):
    def maxValueOfCoins(self, piles, k):
        """
        :type piles: list[list[int]]
        :type k: int
        :rtype: int
        """
        dp = [0] * (k + 1)
        for pile in piles:
            # Precompute prefix sums for this pile
            prefix = [0]
            for coin in pile:
                prefix.append(prefix[-1] + coin)
            # Iterate in reverse to prevent reuse of current pile
            for j in range(k, 0, -1):
                for take in range(1, min(len(pile), j) + 1):
                    dp[j] = max(dp[j], dp[j - take] + prefix[take])
        return dp[k]
