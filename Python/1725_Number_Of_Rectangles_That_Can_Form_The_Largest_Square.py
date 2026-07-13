# Author: Kaustav Ghosh
# Problem: Number Of Rectangles That Can Form The Largest Square
# Approach: The biggest square a rectangle yields has side min(l, w); count how many rectangles hit the largest such side

class Solution(object):
    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        sides = [min(l, w) for l, w in rectangles]
        return sides.count(max(sides))
