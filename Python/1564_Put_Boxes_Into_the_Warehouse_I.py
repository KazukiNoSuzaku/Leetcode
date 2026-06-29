# Author: Kaustav Ghosh
# Problem: Put Boxes Into the Warehouse I (Premium)
# Approach: A room's usable height is the prefix-min of warehouse heights (boxes enter from the left); greedily fit the smallest boxes into the rooms from the back

class Solution(object):
    def maxBoxesInWarehouse(self, boxes, warehouse):
        """
        :type boxes: List[int]
        :type warehouse: List[int]
        :rtype: int
        """
        n = len(warehouse)
        effective = [0] * n
        cur = float('inf')
        for i in range(n):
            cur = min(cur, warehouse[i])
            effective[i] = cur

        boxes.sort()
        i = 0  # pointer to the smallest unplaced box
        count = 0
        # rooms from the deepest (smallest usable height) toward the entrance
        for room in range(n - 1, -1, -1):
            if i < len(boxes) and boxes[i] <= effective[room]:
                count += 1
                i += 1
        return count
