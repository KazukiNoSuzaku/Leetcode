# Simulate squares falling onto a number line; return max height after each drop.

# Author: Kaustav Ghosh

class Solution(object):
    def fallingSquares(self, positions):
        heights = []
        res = []
        max_h = 0
        for left, size in positions:
            right = left + size
            h = size
            for l2, r2, h2 in heights:
                if l2 < right and r2 > left:
                    h = max(h, h2 + size)
            heights.append((left, right, h))
            max_h = max(max_h, h)
            res.append(max_h)
        return res
