# Author: Kaustav Ghosh
# Problem: Paths in Matrix Whose Sum Is Divisible by K
# Approach: Only the running sum modulo k matters, so carry a count of paths per remainder for each cell. A cell's counts come from the cell above and the cell to the left, each remainder shifted by the cell's own value, and the answer is the count of remainder 0 at the bottom-right corner

class Solution(object):
    def numberOfPaths(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        cols = len(grid[0])
        row_counts = [[0] * k for _ in range(cols)]
        for i, row in enumerate(grid):
            new_counts = [[0] * k for _ in range(cols)]
            for j, value in enumerate(row):
                value %= k
                if i == 0 and j == 0:
                    new_counts[0][value] = 1
                    continue
                target = new_counts[j]
                for remainder in range(k):
                    total = (row_counts[j][remainder] if i else 0) + \
                            (new_counts[j - 1][remainder] if j else 0)
                    if total:
                        shifted = (remainder + value) % k
                        target[shifted] = (target[shifted] + total) % MOD
            row_counts = new_counts
        return row_counts[cols - 1][0]
