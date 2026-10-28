# Author: Kaustav Ghosh
# Problem: Building Boxes
# Approach: The support rule means the densest arrangement is a staircase tucked into a corner, where a pile of height h occupies a triangle of h(h+1)/2 floor cells and holds h(h+1)(h+2)/6 boxes in total. So the first step is to grow that complete staircase as far as the box count allows, which is a short loop since the totals climb cubically. Whatever boxes remain are then stacked against the existing staircase one floor cell at a time, and the k-th such cell supports k boxes, so adding floor cells until their running triangle covers the remainder gives the extra footprint. Both stages are arithmetic rather than search.

class Solution(object):
    def minimumBoxes(self, n):
        """
        :type n: int
        :rtype: int
        """
        height = 0
        placed = 0
        floor = 0
        # Grow the complete staircase while it still fits.
        while placed + (height + 1) * (height + 2) // 2 <= n:
            height += 1
            floor += height
            placed += height * (height + 1) // 2

        # Each further floor cell carries one more box than the last.
        extra = 0
        while placed < n:
            extra += 1
            placed += extra
            floor += 1
        return floor
