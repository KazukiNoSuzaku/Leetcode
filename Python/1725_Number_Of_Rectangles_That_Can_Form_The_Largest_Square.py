# Author: Kaustav Ghosh
# Problem: Number Of Rectangles That Can Form The Largest Square
# Approach: The biggest square a rectangle can yield is limited by its shorter side, so each rectangle reduces to that single number and the question becomes how many of them equal the largest such number. One pass suffices, tracking the largest side seen and how many rectangles have achieved it, resetting the count whenever a new maximum appears.

class Solution(object):
    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        largest = 0
        count = 0
        for length, width in rectangles:
            side = length if length < width else width
            if side > largest:
                largest = side
                count = 1
            elif side == largest:
                count += 1
        return count
