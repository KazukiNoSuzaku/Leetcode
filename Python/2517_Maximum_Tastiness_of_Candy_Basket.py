# Author: Kaustav Ghosh
# Problem: Maximum Tastiness of Candy Basket
# Approach: If a gap of g is achievable then so is anything smaller, so binary search g. Checking it is greedy on the sorted prices: walk upward taking a candy whenever it is at least g past the last one taken, and the gap works when that collects k candies

class Solution(object):
    def maximumTastiness(self, price, k):
        """
        :type price: List[int]
        :type k: int
        :rtype: int
        """
        prices = sorted(price)

        def fits(gap):
            taken = 1
            last = prices[0]
            for value in prices[1:]:
                if value - last >= gap:
                    taken += 1
                    last = value
            return taken >= k

        low, high = 0, prices[-1] - prices[0]
        while low < high:
            mid = (low + high + 1) // 2
            if fits(mid):
                low = mid
            else:
                high = mid - 1
        return low
