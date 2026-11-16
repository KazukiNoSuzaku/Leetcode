# Author: Kaustav Ghosh
# Problem: Maximum Number of Points with Cost
# Approach: Picking one cell per row makes this a row-by-row dynamic program, but the naive transition pays for every pair of columns and costs O(n^2) per row. The penalty |c1 - c2| splits into two cases: when the previous pick is at or left of the current column the score is best[k] + k - c, and when it is at or right of it the score is best[k] - k + c, so a running prefix maximum of best[k] + k scanned left to right and a running suffix maximum of best[k] - k scanned right to left give both cases in constant time per column. Each row is then one left sweep and one right sweep, so the whole grid is handled in O(m * n) time with one row of state.

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        width = len(points[0])
        best = list(points[0])

        for row in points[1:]:
            from_left = [0] * width
            running = best[0]
            for column in range(width):
                if best[column] + column > running:
                    running = best[column] + column
                from_left[column] = running - column

            from_right = [0] * width
            running = best[width - 1] - (width - 1)
            for column in range(width - 1, -1, -1):
                if best[column] - column > running:
                    running = best[column] - column
                from_right[column] = running + column

            best = [row[column] + max(from_left[column], from_right[column])
                    for column in range(width)]

        return max(best)
