# Author: Kaustav Ghosh
# Problem: Minimum Cost of Buying Candies With Discount
# Approach: For every two candies bought you get a cheaper one free. Sorting descending and taking candies in groups of three lets the cheapest of each group (every third) be free; sum the rest

class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.sort(reverse=True)
        return sum(c for i, c in enumerate(cost) if i % 3 != 2)
