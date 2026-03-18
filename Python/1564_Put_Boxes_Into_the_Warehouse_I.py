# Author: Kaustav Ghosh
# Problem: 1564 - Put Boxes Into the Warehouse I (Premium)
# Approach: Sort boxes desc, preprocess warehouse heights, greedily fit left to right

class Solution(object):
    def maxBoxesInWarehouse(self, boxes, warehouse):
        """
        :type boxes: List[int]
        :type warehouse: List[int]
        :rtype: int
        """
        # Preprocess warehouse: each position can hold min height up to that point
        n = len(warehouse)
        for i in range(1, n):
            warehouse[i] = min(warehouse[i], warehouse[i-1])

        boxes.sort(reverse=True)
        count = 0
        j = 0
        for box in boxes:
            while j < n and warehouse[j] < box:
                j += 1
            if j == n:
                break
            count += 1
            j += 1

        return count
