# Premium problem - not available without subscription
# Author: Kaustav Ghosh
# Typical approach: BFS from origin to target using knight moves with symmetry optimization

class Solution(object):
    def minKnightMoves(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        from collections import deque
        x, y = abs(x), abs(y)
        queue = deque([(0, 0, 0)])
        visited = {(0, 0)}
        moves = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
        while queue:
            cx, cy, steps = queue.popleft()
            if cx == x and cy == y:
                return steps
            for dx, dy in moves:
                nx, ny = cx + dx, cy + dy
                if (nx, ny) not in visited and -2 <= nx <= x + 2 and -2 <= ny <= y + 2:
                    visited.add((nx, ny))
                    queue.append((nx, ny, steps + 1))
        return -1
