# Author: Kaustav Ghosh
# Problem: Erect the Fence II
# Approach: This is the smallest enclosing circle, and Welzl's observation is that the answer is pinned down by at most three of the trees sitting on its boundary. So the trees are visited one at a time, and whenever one falls outside the circle built so far it must lie on the boundary of the new answer, which makes it the anchor of a fresh pass over the earlier trees; the same argument nests twice more, giving three loops. That is quadratic or worse in the worst order, but shuffling the trees first makes a tree fall outside only rarely, so the expected work is linear. Circles through two trees take their midpoint, and through three the circumcentre, with collinear triples falling back to the widest pair.

class Solution(object):
    def outerTrees(self, trees):
        """
        :type trees: List[List[int]]
        :rtype: List[float]
        """
        import random

        points = [(float(x), float(y)) for x, y in trees]
        random.shuffle(points)

        def span(a, b):
            return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

        def encloses(circle, point):
            centre, radius = circle
            return span(centre, point) <= radius + 1e-7

        def through_two(a, b):
            return ((a[0] + b[0]) / 2.0, (a[1] + b[1]) / 2.0), span(a, b) / 2.0

        def through_three(a, b, c):
            (ax, ay), (bx, by), (cx, cy) = a, b, c
            twice = 2.0 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
            if twice == 0.0:
                widest = through_two(a, b)
                for pair in ((a, c), (b, c)):
                    candidate = through_two(*pair)
                    if candidate[1] > widest[1]:
                        widest = candidate
                return widest
            sa, sb, sc = ax * ax + ay * ay, bx * bx + by * by, cx * cx + cy * cy
            ux = (sa * (by - cy) + sb * (cy - ay) + sc * (ay - by)) / twice
            uy = (sa * (cx - bx) + sb * (ax - cx) + sc * (bx - ax)) / twice
            return (ux, uy), span((ux, uy), a)

        circle = (points[0], 0.0)
        for i in range(1, len(points)):
            if encloses(circle, points[i]):
                continue
            circle = (points[i], 0.0)
            for j in range(i):
                if encloses(circle, points[j]):
                    continue
                circle = through_two(points[i], points[j])
                for k in range(j):
                    if encloses(circle, points[k]):
                        continue
                    circle = through_three(points[i], points[j], points[k])
        (x, y), radius = circle
        return [x, y, radius]
