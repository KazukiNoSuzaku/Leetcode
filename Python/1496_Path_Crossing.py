# Author: Kaustav Ghosh
# Problem: Path Crossing
# Approach: Track visited (x, y) positions, detect revisit

class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        x, y = 0, 0
        visited = {(0, 0)}
        dirs = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
        for d in path:
            dx, dy = dirs[d]
            x, y = x + dx, y + dy
            if (x, y) in visited:
                return True
            visited.add((x, y))
        return False
