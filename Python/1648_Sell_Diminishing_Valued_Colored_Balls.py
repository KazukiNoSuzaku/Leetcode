# Author: Kaustav Ghosh
# https://leetcode.com/problems/sell-diminishing-valued-colored-balls/

class Solution(object):
    def maxProfit(self, inventory, orders):
        """
        :type inventory: List[int]
        :type orders: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        inventory.sort(reverse=True)
        inventory.append(0)
        profit = 0
        width = 0
        for i in range(len(inventory) - 1):
            width += 1
            if inventory[i] > inventory[i + 1]:
                diff = inventory[i] - inventory[i + 1]
                total_balls = width * diff
                if total_balls <= orders:
                    # Sum from inventory[i+1]+1 to inventory[i], times width
                    profit += width * (inventory[i] + inventory[i + 1] + 1) * diff // 2
                    profit %= MOD
                    orders -= total_balls
                else:
                    full_rows = orders // width
                    remainder = orders % width
                    top = inventory[i]
                    profit += width * (top + top - full_rows + 1) * full_rows // 2
                    profit += remainder * (top - full_rows)
                    profit %= MOD
                    orders = 0
                    break
        return profit % MOD
