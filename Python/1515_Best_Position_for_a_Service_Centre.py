# Author: Kaustav Ghosh
# Problem: 1515 - Best Position for a Service Centre
# Approach: Gradient descent / geometric median via simulated annealing

class Solution(object):
    def getMinDistSum(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: float
        """
        def dist(x, y):
            return sum(((x - px)**2 + (y - py)**2)**0.5 for px, py in positions)

        x = sum(p[0] for p in positions) / len(positions)
        y = sum(p[1] for p in positions) / len(positions)

        step = 1.0
        while step > 1e-6:
            moved = False
            for dx, dy in [(0, step), (0, -step), (step, 0), (-step, 0)]:
                nx, ny = x + dx, y + dy
                if dist(nx, ny) < dist(x, y):
                    x, y = nx, ny
                    moved = True
                    break
            if not moved:
                step *= 0.5

        return dist(x, y)
