# Given the coordinates of four points in 2D space p1, p2, p3, p4, return true if the four points
# construct a square. A square has 4 equal sides and 4 equal diagonals.

# Author: Kaustav Ghosh

class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        def d(a, b): return (a[0]-b[0])**2 + (a[1]-b[1])**2
        pts = [p1, p2, p3, p4]
        dists = sorted(d(pts[i], pts[j]) for i in range(4) for j in range(i+1, 4))
        return dists[0] > 0 and dists[0] == dists[1] == dists[2] == dists[3] and dists[4] == dists[5]
