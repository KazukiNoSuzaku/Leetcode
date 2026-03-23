# Author: Kaustav Ghosh
# Problem 1872: Stone Game VIII

class Solution(object):
    def stoneGameVIII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        n = len(stones)
        # Compute prefix sums
        for i in range(1, n):
            stones[i] += stones[i - 1]
        # Work backwards: dp represents best difference Alice can achieve
        # Starting from rightmost choice
        result = stones[n - 1]
        for i in range(n - 2, 0, -1):
            result = max(result, stones[i] - result)
        return result
