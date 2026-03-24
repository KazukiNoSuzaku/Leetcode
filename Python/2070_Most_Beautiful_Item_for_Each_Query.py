# Author: Kaustav Ghosh
# Problem 2070: Most Beautiful Item for Each Query

from bisect import bisect_right

class Solution(object):
    def maximumBeauty(self, items, queries):
        """
        :type items: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        items.sort()
        # Build prefix max beauty
        prices = []
        max_beauties = []
        curr_max = 0
        for price, beauty in items:
            curr_max = max(curr_max, beauty)
            prices.append(price)
            max_beauties.append(curr_max)

        result = []
        for q in queries:
            idx = bisect_right(prices, q) - 1
            if idx >= 0:
                result.append(max_beauties[idx])
            else:
                result.append(0)
        return result
