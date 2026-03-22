# Author: Kaustav Ghosh
# https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/

class Solution(object):
    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        max_side = 0
        count = 0
        for l, w in rectangles:
            side = min(l, w)
            if side > max_side:
                max_side = side
                count = 1
            elif side == max_side:
                count += 1
        return count
