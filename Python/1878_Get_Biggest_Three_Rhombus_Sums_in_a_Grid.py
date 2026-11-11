# Author: Kaustav Ghosh
# Problem: Get Biggest Three Rhombus Sums in a Grid
# Approach: A rhombus is pinned down by its top corner and its radius, so every candidate is enumerated directly and its border is walked once, adding the four sides while stepping along each diagonal. The grid is at most fifty by fifty, which caps the whole enumeration at a few million cell visits, so no diagonal prefix sums are needed to make it fast enough and the border walk stays readable. Sums go into a set rather than a list, which is what makes the three largest distinct as the problem requires, and taking the three largest of that set also covers a grid offering fewer than three.

class Solution(object):
    def getBiggestThree(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        rows, cols = len(grid), len(grid[0])
        sums = set()

        for top in range(rows):
            for left in range(cols):
                sums.add(grid[top][left])
                radius = 1
                while top + 2 * radius < rows and left - radius >= 0 and left + radius < cols:
                    total = 0
                    # Each of the four sides contributes its starting corner and
                    # stops one cell short of the next, so no corner is counted twice.
                    for step in range(radius):
                        total += grid[top + step][left + step]
                        total += grid[top + radius + step][left + radius - step]
                        total += grid[top + 2 * radius - step][left - step]
                        total += grid[top + radius - step][left - radius + step]
                    sums.add(total)
                    radius += 1

        return sorted(sums, reverse=True)[:3]
