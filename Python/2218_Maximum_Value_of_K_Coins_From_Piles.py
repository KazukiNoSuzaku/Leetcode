# Author: Kaustav Ghosh
# Problem: Maximum Value of K Coins From Piles
# Approach: From each pile you may only take a prefix of the top coins, so this is a grouped knapsack. dp[c] is the best value using exactly c coins so far; for each pile try taking j coins off the top (prefix sum) and combine with dp[c-j]

class Solution(object):
    def maxValueOfCoins(self, piles, k):
        """
        :type piles: List[List[int]]
        :type k: int
        :rtype: int
        """
        dp = [0] * (k + 1)
        for pile in piles:
            # prefix sums of taking 0..len(pile) coins from the top
            prefix = [0]
            for coin in pile:
                prefix.append(prefix[-1] + coin)
            ndp = list(dp)
            for c in range(1, k + 1):
                best = dp[c]  # take nothing from this pile
                take_max = min(len(pile), c)
                for j in range(1, take_max + 1):
                    val = dp[c - j] + prefix[j]
                    if val > best:
                        best = val
                ndp[c] = best
            dp = ndp
        return dp[k]
