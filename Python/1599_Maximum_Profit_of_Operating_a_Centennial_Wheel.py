# Author: Kaustav Ghosh
# Problem: Maximum Profit of Operating a Centennial Wheel
# Approach: Simulate rotations, boarding up to 4 waiting customers each turn, and remember the earliest rotation that hit the peak profit

class Solution(object):
    def minOperationsMaxProfit(self, customers, boardingCost, runningCost):
        """
        :type customers: List[int]
        :type boardingCost: int
        :type runningCost: int
        :rtype: int
        """
        waiting = 0
        profit = 0
        best_profit = 0
        best_rotation = -1
        rotation = 0
        i = 0

        while i < len(customers) or waiting > 0:
            if i < len(customers):
                waiting += customers[i]
                i += 1
            board = min(4, waiting)
            waiting -= board
            rotation += 1
            profit += board * boardingCost - runningCost
            if profit > best_profit:
                best_profit = profit
                best_rotation = rotation

        return best_rotation
