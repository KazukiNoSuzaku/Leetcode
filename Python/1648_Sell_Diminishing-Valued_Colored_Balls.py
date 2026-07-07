# Author: Kaustav Ghosh
# Problem: Sell Diminishing-Valued Colored Balls
# Approach: Sort counts descending and sell in horizontal "levels": drop all top colors down to the next distinct height at once using arithmetic-series sums, handling the final partial level

class Solution(object):
    def maxProfit(self, inventory, orders):
        """
        :type inventory: List[int]
        :type orders: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        inventory.sort(reverse=True)
        inventory.append(0)  # sentinel floor

        revenue = 0
        width = 0  # number of colors currently at the top level
        for i in range(len(inventory) - 1):
            cur, nxt = inventory[i], inventory[i + 1]
            width += 1
            drop = cur - nxt  # levels we could sell across all `width` colors

            if orders >= drop * width:
                # Sell values cur, cur-1, ..., nxt+1 for every color at the top
                revenue += width * (cur + nxt + 1) * (cur - nxt) // 2
                orders -= drop * width
            else:
                full = orders // width      # complete levels sold to all colors
                rem = orders % width        # extra colors sold one more level
                bottom = cur - full + 1
                revenue += width * (cur + bottom) * full // 2
                revenue += rem * (bottom - 1)
                revenue %= MOD
                return revenue % MOD
            revenue %= MOD

        return revenue % MOD
