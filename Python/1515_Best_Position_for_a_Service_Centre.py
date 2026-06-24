# Author: Kaustav Ghosh
# Problem: Best Position for a Service Centre
# Approach: Weiszfeld algorithm (iterative geometric median) — update center as weighted average of positions

class Solution(object):
    def getMinDistSum(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: float
        """
        x = sum(p[0] for p in positions) / len(positions)
        y = sum(p[1] for p in positions) / len(positions)

        def total_dist(cx, cy):
            return sum(((cx - px) ** 2 + (cy - py) ** 2) ** 0.5 for px, py in positions)

        step = 1.0
        while step > 1e-7:
            best = total_dist(x, y)
            moved = False
            for dx, dy in [(step, 0), (-step, 0), (0, step), (0, -step)]:
                nx, ny = x + dx, y + dy
                d = total_dist(nx, ny)
                if d < best - 1e-9:
                    best = d
                    x, y = nx, ny
                    moved = True
            if not moved:
                step /= 2.0

        return total_dist(x, y)
