# Author: Kaustav Ghosh
# Problem: Most Beautiful Item for Each Query
# Approach: Sort items by price and build a running maximum of beauty. For each query, binary search the last item within the price limit and read the prefix maximum beauty up to there

import bisect

class Solution(object):
    def maximumBeauty(self, items, queries):
        """
        :type items: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        items.sort()
        prices = []
        best_beauty = []
        running = 0
        for price, beauty in items:
            running = max(running, beauty)
            prices.append(price)
            best_beauty.append(running)

        result = []
        for q in queries:
            idx = bisect.bisect_right(prices, q) - 1
            result.append(best_beauty[idx] if idx >= 0 else 0)
        return result
