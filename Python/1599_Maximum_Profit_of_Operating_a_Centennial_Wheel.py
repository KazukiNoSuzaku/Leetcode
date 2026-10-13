# Author: Kaustav Ghosh
# Problem: Maximum Profit of Operating a Centennial Wheel
# Approach: Profit is not monotonic, so stopping at the first dip would be wrong and stopping only when the queue empties can also be wrong; the answer is the rotation count at the best point ever reached, which means simulating the rotations and remembering the running maximum. Each turn adds that round's arrivals to the queue, boards up to four, and recomputes total profit from the cumulative boarded count against the rotations spent. The loop has to keep going while anyone is still waiting even after the arrivals list is exhausted, and a best profit that never becomes positive means operating at all is a loss.

class Solution(object):
    def minOperationsMaxProfit(self, customers, boardingCost, runningCost):
        """
        :type customers: List[int]
        :type boardingCost: int
        :type runningCost: int
        :rtype: int
        """
        waiting = 0
        boarded = 0
        rotations = 0
        best_profit = 0
        best_rotation = -1
        arrivals = len(customers)
        index = 0
        while index < arrivals or waiting > 0:
            if index < arrivals:
                waiting += customers[index]
                index += 1
            boarding = 4 if waiting > 4 else waiting
            waiting -= boarding
            boarded += boarding
            rotations += 1
            profit = boarded * boardingCost - rotations * runningCost
            if profit > best_profit:
                best_profit = profit
                best_rotation = rotations
        return best_rotation
