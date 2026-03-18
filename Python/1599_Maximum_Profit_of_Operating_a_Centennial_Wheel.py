# Author: Kaustav Ghosh
# Problem: 1599 - Maximum Profit of Operating a Centennial Wheel (Premium)
# Approach: Simulate rotations, track profit per rotation

class Solution(object):
    def minOperationsMaxProfit(self, customers, boardingCost, runningCost):
        """
        :type customers: List[int]
        :type boardingCost: int
        :type runningCost: int
        :rtype: int
        """
        max_profit = 0
        best_rotation = -1
        waiting = 0
        profit = 0
        rotation = 0

        i = 0
        while i < len(customers) or waiting > 0:
            if i < len(customers):
                waiting += customers[i]
                i += 1
            board = min(4, waiting)
            waiting -= board
            profit += board * boardingCost - runningCost
            rotation += 1
            if profit > max_profit:
                max_profit = profit
                best_rotation = rotation

        return best_rotation
