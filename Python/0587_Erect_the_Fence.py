# You are given an array trees where trees[i] = [xi, yi] represents the location of a tree.
# Return the coordinates of trees that are exactly on the fence perimeter (convex hull).

# Author: Kaustav Ghosh

class Solution(object):
    def outerTrees(self, trees):
        def cross(O, A, B):
            return (A[0]-O[0])*(B[1]-O[1]) - (A[1]-O[1])*(B[0]-O[0])
        trees.sort()
        hull = []
        # Lower hull
        for p in trees:
            while len(hull) >= 2 and cross(hull[-2], hull[-1], p) < 0:
                hull.pop()
            hull.append(p)
        # Upper hull
        lower_size = len(hull)
        for p in reversed(trees):
            while len(hull) > lower_size and cross(hull[-2], hull[-1], p) < 0:
                hull.pop()
            hull.append(p)
        return list(set(map(tuple, hull)))
