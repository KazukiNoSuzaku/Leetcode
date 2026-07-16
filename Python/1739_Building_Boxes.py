# Author: Kaustav Ghosh
# Problem: Building Boxes
# Approach: Stack boxes as a staircase in the corner. Grow complete pyramid layers (layer k holds k(k+1)/2 boxes) while they fit, then place leftovers one diagonal column at a time - each such column costs only one extra floor box

class Solution(object):
    def minimumBoxes(self, n):
        """
        :type n: int
        :rtype: int
        """
        placed = 0
        layers = 0
        # Add whole pyramid layers while they still fit
        while placed + (layers + 1) * (layers + 2) // 2 <= n:
            layers += 1
            placed += layers * (layers + 1) // 2

        floor = layers * (layers + 1) // 2
        remaining = n - placed

        # Each extra column height i consumes i boxes but touches the floor once
        height = 0
        while remaining > 0:
            height += 1
            remaining -= height
            floor += 1

        return floor
