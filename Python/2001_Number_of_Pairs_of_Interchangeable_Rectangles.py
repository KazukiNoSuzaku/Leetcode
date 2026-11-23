# Author: Kaustav Ghosh
# Problem: Number of Pairs of Interchangeable Rectangles
# Approach: Two rectangles are interchangeable exactly when their width-to-height ratios agree, so the task is to group the rectangles by ratio and count the pairs inside each group. Floating-point division would risk two genuinely different ratios collapsing onto the same value, so each ratio is instead reduced to lowest terms by dividing both sides by their greatest common divisor, which gives an exact and canonical key. Once the group sizes are tallied, a group of a given size contributes that size choose two pairs.

class Solution(object):
    def interchangeableRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        from collections import Counter
        shapes = Counter()
        for width, height in rectangles:
            left, right = width, height
            while right:
                left, right = right, left % right
            shapes[(width // left, height // left)] += 1
        return sum(count * (count - 1) // 2 for count in shapes.values())
