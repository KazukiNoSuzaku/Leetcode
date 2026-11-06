# Author: Kaustav Ghosh
# Problem: Maximum Ice Cream Bars
# Approach: Every bar counts the same towards the total regardless of price, so for any budget the best plan is to take the cheapest bars; swapping a bought bar for an unbought cheaper one never reduces the count and never increases the spend. Sorting the prices and buying in order until the money runs out therefore gives the answer, and the loop stops at the first bar that cannot be afforded because every later one costs at least as much.

class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        bought = 0
        for price in sorted(costs):
            if price > coins:
                break
            coins -= price
            bought += 1
        return bought
