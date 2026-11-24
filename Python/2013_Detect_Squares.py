# Author: Kaustav Ghosh
# Problem: Detect Squares
# Approach: An axis-aligned square is pinned down by the query point together with the corner diagonally opposite it, so rather than scanning every stored point the search walks only the points sharing the query's x coordinate. Each such point supplies the square's side length as its vertical distance from the query, which fixes the other two corners at that distance to the left and to the right; multiplying the three corners' stored multiplicities counts every combination of duplicate points at once. Keeping the points as a map from column to a tally of that column's y values makes both the walk and the corner lookups direct, and a zero side length is skipped since a square needs positive area.

class DetectSquares(object):

    def __init__(self):
        from collections import defaultdict, Counter
        self.columns = defaultdict(Counter)

    def add(self, point):
        """
        :type point: List[int]
        :rtype: None
        """
        self.columns[point[0]][point[1]] += 1

    def count(self, point):
        """
        :type point: List[int]
        :rtype: int
        """
        x, y = point
        column = self.columns.get(x)
        if not column:
            return 0
        total = 0
        for other_y, copies in column.items():
            side = other_y - y
            if side == 0:
                continue
            if side < 0:
                side = -side
            for other_x in (x - side, x + side):
                neighbour = self.columns.get(other_x)
                if not neighbour:
                    continue
                total += copies * neighbour[y] * neighbour[other_y]
        return total


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
