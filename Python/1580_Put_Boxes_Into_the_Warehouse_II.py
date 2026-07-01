# Author: Kaustav Ghosh
# Problem: Put Boxes Into the Warehouse II (Premium)
# Approach: Boxes enter from either side, so each room's usable height is max(prefix-min, suffix-min); greedily match smallest boxes to smallest rooms

class Solution(object):
    def maxBoxesInWarehouse(self, boxes, warehouse):
        """
        :type boxes: List[int]
        :type warehouse: List[int]
        :rtype: int
        """
        n = len(warehouse)
        INF = float('inf')

        left = [0] * n
        cur = INF
        for i in range(n):
            cur = min(cur, warehouse[i])
            left[i] = cur

        right = [0] * n
        cur = INF
        for i in range(n - 1, -1, -1):
            cur = min(cur, warehouse[i])
            right[i] = cur

        usable = sorted(max(left[i], right[i]) for i in range(n))
        boxes.sort()

        i = 0  # index into boxes (smallest unplaced)
        for h in usable:
            if i < len(boxes) and boxes[i] <= h:
                i += 1
        return i
