# Author: Kaustav Ghosh
# Problem: Minimum Swaps to Arrange a Binary Grid
# Approach: For row i, need >= n-1-i trailing zeros; greedily find nearest valid row and bubble it up

class Solution(object):
    def minSwaps(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        trailing = []
        for row in grid:
            cnt = 0
            for j in range(n - 1, -1, -1):
                if row[j] == 0:
                    cnt += 1
                else:
                    break
            trailing.append(cnt)

        ans = 0
        for i in range(n):
            need = n - 1 - i
            found = -1
            for j in range(i, n):
                if trailing[j] >= need:
                    found = j
                    break
            if found == -1:
                return -1
            while found > i:
                trailing[found], trailing[found - 1] = trailing[found - 1], trailing[found]
                found -= 1
                ans += 1
        return ans
