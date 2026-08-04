# Author: Kaustav Ghosh
# Problem: Erect the Fence II
# Approach: This is the minimum enclosing circle of all points. Welzl's randomized incremental algorithm: process shuffled points, and whenever a point falls outside the current circle, rebuild the circle with that point forced onto the boundary (with one or two others). Expected linear time

import random

class Solution(object):
    def outerTrees(self, trees):
        """
        :type trees: List[List[int]]
        :rtype: List[float]
        """
        pts = [(float(x), float(y)) for x, y in trees]
        random.shuffle(pts)

        def dist(a, b):
            return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

        def inside(c, p):
            return dist((c[0], c[1]), p) <= c[2] + 1e-7

        def from_two(a, b):
            cx, cy = (a[0] + b[0]) / 2.0, (a[1] + b[1]) / 2.0
            return (cx, cy, dist(a, b) / 2.0)

        def from_three(a, b, c):
            ax, ay = a; bx, by = b; cx, cy = c
            d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
            if abs(d) < 1e-12:                      # collinear: use widest pair
                best = from_two(a, b)
                for pair in (from_two(a, c), from_two(b, c)):
                    if pair[2] > best[2]:
                        best = pair
                return best
            ux = ((ax * ax + ay * ay) * (by - cy) + (bx * bx + by * by) * (cy - ay) + (cx * cx + cy * cy) * (ay - by)) / d
            uy = ((ax * ax + ay * ay) * (cx - bx) + (bx * bx + by * by) * (ax - cx) + (cx * cx + cy * cy) * (bx - ax)) / d
            center = (ux, uy)
            return (ux, uy, dist(center, a))

        circle = None
        for i, p in enumerate(pts):
            if circle is not None and inside(circle, p):
                continue
            circle = (p[0], p[1], 0.0)
            for j in range(i):
                if inside(circle, pts[j]):
                    continue
                circle = from_two(p, pts[j])
                for k in range(j):
                    if inside(circle, pts[k]):
                        continue
                    circle = from_three(p, pts[j], pts[k])

        if circle is None:
            return [0.0, 0.0, 0.0]
        return [circle[0], circle[1], circle[2]]
