# Author: Kaustav Ghosh
# Problem: 1536 - Minimum Swaps to Arrange a Binary Grid
# Approach: Greedy: for each row find first fitting, bubble up via swaps

class Solution(object):
    def minSwaps(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        # trailing zeros count for each row
        trailing = []
        for row in grid:
            count = 0
            for j in range(n - 1, -1, -1):
                if row[j] == 0:
                    count += 1
                else:
                    break
            trailing.append(count)

        swaps = 0
        for i in range(n):
            need = n - 1 - i
            # find first row from i that has at least 'need' trailing zeros
            found = -1
            for j in range(i, n):
                if trailing[j] >= need:
                    found = j
                    break
            if found == -1:
                return -1
            # bubble up
            while found > i:
                trailing[found], trailing[found - 1] = trailing[found - 1], trailing[found]
                found -= 1
                swaps += 1

        return swaps
