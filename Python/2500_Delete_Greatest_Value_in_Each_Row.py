# Author: Kaustav Ghosh
# Problem: Delete Greatest Value in Each Row
# Approach: Each round strips the current largest value from every row, which after sorting the rows descending is simply their next column. So sort each row and add the largest value of each column

class Solution(object):
    def deleteGreatestValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = [sorted(row, reverse=True) for row in grid]
        return sum(max(column) for column in zip(*rows))
