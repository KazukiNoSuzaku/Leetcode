# Compute total area covered by a list of rectangles (with overlaps counted once).

# Author: Kaustav Ghosh

class Solution(object):
    def rectangleArea(self, rectangles):
        MOD = 10**9 + 7
        xs = sorted(set(x for r in rectangles for x in [r[0], r[2]]))
        ys = sorted(set(y for r in rectangles for y in [r[1], r[3]]))
        xi = {x: i for i, x in enumerate(xs)}
        yi = {y: i for i, y in enumerate(ys)}
        grid = [[0] * len(ys) for _ in range(len(xs))]
        for x1, y1, x2, y2 in rectangles:
            for i in range(xi[x1], xi[x2]):
                for j in range(yi[y1], yi[y2]):
                    grid[i][j] = 1
        return sum(grid[i][j] * (xs[i+1]-xs[i]) * (ys[j+1]-ys[j])
                   for i in range(len(xs)-1) for j in range(len(ys)-1)) % MOD
