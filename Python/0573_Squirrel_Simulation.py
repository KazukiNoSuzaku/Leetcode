# You are given the position of a squirrel, a tree, and nuts on a grid.
# The squirrel must collect all nuts and bring them to the tree one by one.
# Return the minimum distance for the squirrel to collect all the nuts.

# Author: Kaustav Ghosh

class Solution(object):
    def minDistance(self, height, width, tree, squirrel, nuts):
        def dist(a, b): return abs(a[0]-b[0]) + abs(a[1]-b[1])
        total = sum(2 * dist(tree, nut) for nut in nuts)
        # Squirrel saves: 2*dist(tree,nut) - dist(squirrel,nut) - dist(tree,nut)
        best_save = min(dist(tree, nut) - dist(squirrel, nut) for nut in nuts)
        return total + best_save
