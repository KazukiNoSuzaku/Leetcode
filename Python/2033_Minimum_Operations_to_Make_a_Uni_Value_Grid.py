# Author: Kaustav Ghosh
# Problem: Minimum Operations to Make a Uni-Value Grid
# Approach: Every operation shifts a cell by the given step, so a cell can only ever reach values congruent to itself modulo that step, and the whole grid can be levelled only if all cells already share one remainder. Granted that, each cell's cost to reach a common target is their difference divided by the step, so the total is proportional to the sum of absolute differences from the target. That sum is minimised at the median of the values, which is why the cells are flattened and sorted and the middle one chosen, after which the costs are added up directly.

class Solution(object):
    def minOperations(self, grid, x):
        """
        :type grid: List[List[int]]
        :type x: int
        :rtype: int
        """
        values = []
        for row in grid:
            values.extend(row)
        remainder = values[0] % x
        for value in values:
            if value % x != remainder:
                return -1
        values.sort()
        target = values[len(values) // 2]
        moves = 0
        for value in values:
            moves += abs(value - target) // x
        return moves
