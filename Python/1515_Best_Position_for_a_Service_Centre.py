# Author: Kaustav Ghosh
# Problem: Best Position for a Service Centre
# Approach: The total distance is a convex function of the position, so it has a single basin and local improvement cannot get stuck. Start at the centroid and repeatedly step along whichever axis direction lowers the total, halving the step whenever no direction helps, until the step is far below the required precision

class Solution(object):
    def getMinDistSum(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: float
        """
        def total(cx, cy):
            return sum(((cx - px) ** 2 + (cy - py) ** 2) ** 0.5 for px, py in positions)

        x = sum(px for px, _ in positions) / float(len(positions))
        y = sum(py for _, py in positions) / float(len(positions))
        best = total(x, y)
        step = 100.0
        while step > 1e-7:
            moved = False
            for dx, dy in ((step, 0), (-step, 0), (0, step), (0, -step)):
                candidate = total(x + dx, y + dy)
                if candidate < best:
                    best = candidate
                    x += dx
                    y += dy
                    moved = True
                    break
            if not moved:
                step /= 2
        return best
