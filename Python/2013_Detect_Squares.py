# Author: Kaustav Ghosh
# Problem 2013: Detect Squares

from collections import Counter

class DetectSquares(object):
    def __init__(self):
        self.points = Counter()
        self.x_map = {}  # x -> list of y coords

    def add(self, point):
        """
        :type point: List[int]
        :rtype: None
        """
        x, y = point
        self.points[(x, y)] += 1
        if x not in self.x_map:
            self.x_map[x] = []
        self.x_map[x].append(y)

    def count(self, point):
        """
        :type point: List[int]
        :rtype: int
        """
        x1, y1 = point
        result = 0
        # Find all points with same x but different y (diagonal partner)
        if x1 not in self.x_map:
            return 0
        for y2 in self.x_map[x1]:
            if y2 == y1:
                continue
            side = abs(y2 - y1)
            # Check two possible squares
            result += self.points[(x1, y2)] * self.points[(x1 + side, y1)] * self.points[(x1 + side, y2)]
            result += self.points[(x1, y2)] * self.points[(x1 - side, y1)] * self.points[(x1 - side, y2)]
        return result
