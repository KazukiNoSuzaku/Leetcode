# Author: Kaustav Ghosh
# Problem: Maximum Ice Cream Bars
# Approach: To buy the most bars, buy cheapest first; sort prices and take them while the budget lasts

class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        bought = 0
        for price in sorted(costs):
            if coins < price:
                break
            coins -= price
            bought += 1
        return bought
