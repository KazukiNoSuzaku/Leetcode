# Author: Kaustav Ghosh
# Problem: Minimum Swaps to Arrange a Binary Grid
# Approach: Only each row's run of trailing zeros matters, since row i must end with at least n - 1 - i of them. Walk the rows top down and bubble up the nearest row that qualifies, which costs one swap per step; taking the nearest one is optimal because any row deeper down would travel further and serves equally well

class Solution(object):
    def minSwaps(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        trailing = []
        for row in grid:
            count = 0
            for value in reversed(row):
                if value:
                    break
                count += 1
            trailing.append(count)

        swaps = 0
        for i in range(n):
            needed = n - 1 - i
            j = i
            while j < n and trailing[j] < needed:
                j += 1
            if j == n:
                return -1
            while j > i:
                trailing[j], trailing[j - 1] = trailing[j - 1], trailing[j]
                j -= 1
                swaps += 1
        return swaps
