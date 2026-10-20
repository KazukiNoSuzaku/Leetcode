# Author: Kaustav Ghosh
# Problem: Sell Diminishing-Valued Colored Balls
# Approach: A ball's value is the count remaining of its colour, so the most valuable ball available is always from whichever colour has the most left, which means selling strictly in descending order of value. Doing that one ball at a time would be far too slow with a billion orders, so I sort the colours descending and sell in horizontal slabs instead: all colours currently at or above a given value are sold down together to the next distinct value, and the revenue of a slab is an arithmetic series computed in closed form. When the orders run out mid-slab, the remaining orders fill whole levels across the slab's width and then a partial level, the leftover of which is taken at a single value. The modulus is applied only at the very end, since reducing earlier would corrupt the comparisons.

class Solution(object):
    def maxProfit(self, inventory, orders):
        """
        :type inventory: List[int]
        :type orders: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        levels = sorted(inventory, reverse=True)
        levels.append(0)
        profit = 0
        for i in range(len(levels) - 1):
            high = levels[i]
            low = levels[i + 1]
            width = i + 1
            available = (high - low) * width
            if orders >= available:
                # Whole slab: values high down to low + 1, across width colours.
                profit += width * (high + low + 1) * (high - low) // 2
                orders -= available
            else:
                whole_levels = orders // width
                leftover = orders % width
                profit += width * (2 * high - whole_levels + 1) * whole_levels // 2
                profit += leftover * (high - whole_levels)
                orders = 0
                break
        return profit % MOD
