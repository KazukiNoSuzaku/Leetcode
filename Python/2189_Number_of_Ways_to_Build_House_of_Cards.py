# Author: Kaustav Ghosh
# Problem: Number of Ways to Build House of Cards
# Approach: A row of k triangles costs 3k-1 cards (2 per triangle plus k-1 horizontal cards). Each row must have a distinct number of triangles, so a house is a subset of distinct row sizes whose costs sum to n. Count such subsets with a 0/1 subset-sum DP over row sizes k=1,2,3,...

class Solution(object):
    def houseOfCards(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        dp[0] = 1
        k = 1
        while 3 * k - 1 <= n:
            cost = 3 * k - 1
            for s in range(n, cost - 1, -1):
                dp[s] += dp[s - cost]
            k += 1
        return dp[n]
