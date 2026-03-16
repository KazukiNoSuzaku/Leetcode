# Author: Kaustav Ghosh
# Problem: Final Prices With a Special Discount in a Shop
# Approach: Monotone stack finding next smaller or equal element

class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        result = prices[:]
        stack = []
        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                idx = stack.pop()
                result[idx] = prices[idx] - prices[i]
            stack.append(i)
        return result
