# Author: Kaustav Ghosh
# Problem: Detect Squares
# Approach: Keep a multiplicity counter of points and, per column x, the list of y values added (with repeats). To count squares at the query, walk points sharing the query's column: each gives a vertical side length; the two opposite columns contribute the product of the other two corners' counts. Iterating the column list already folds in the query-column corner's multiplicity

from collections import Counter, defaultdict

class DetectSquares(object):
    def __init__(self):
        self.count_map = Counter()
        self.columns = defaultdict(list)

    def add(self, point):
        """
        :type point: List[int]
        :rtype: None
        """
        x, y = point
        self.count_map[(x, y)] += 1
        self.columns[x].append(y)

    def count(self, point):
        """
        :type point: List[int]
        :rtype: int
        """
        qx, qy = point
        total = 0
        for y2 in self.columns[qx]:
            side = abs(y2 - qy)
            if side == 0:
                continue
            for x2 in (qx - side, qx + side):
                total += self.count_map[(x2, qy)] * self.count_map[(x2, y2)]
        return total
