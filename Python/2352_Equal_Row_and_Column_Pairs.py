# Author: Kaustav Ghosh
# Problem: Equal Row and Column Pairs
# Approach: Count the rows as tuples in a hash map, then walk the columns and add the number of matching rows for each, which counts every equal (row, column) pair exactly once

from collections import Counter


class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = Counter(tuple(row) for row in grid)
        return sum(rows[col] for col in zip(*grid))
