# Author: Kaustav Ghosh
# BFS with bitmask state representing the matrix

class Solution(object):
    def minFlips(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        from collections import deque
        m, n = len(mat), len(mat[0])

        # Convert matrix to bitmask
        start = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j]:
                    start |= 1 << (i * n + j)

        if start == 0:
            return 0

        visited = {start}
        queue = deque([(start, 0)])

        while queue:
            state, flips = queue.popleft()
            for i in range(m):
                for j in range(n):
                    new_state = state
                    # Flip cell and its neighbors
                    for di, dj in [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < m and 0 <= nj < n:
                            new_state ^= 1 << (ni * n + nj)
                    if new_state == 0:
                        return flips + 1
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, flips + 1))
        return -1
