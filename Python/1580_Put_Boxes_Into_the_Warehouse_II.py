# Author: Kaustav Ghosh
# Problem: Put Boxes Into the Warehouse II
# Approach: Every box has to enter past whichever end it comes from, so at any moment the only two rooms a box can actually reach are the current outermost unfilled rooms on the left and on the right. I sort the boxes and offer the largest remaining one to those two rooms: if it fits either, placing it there is best, since every deeper room is reached through this one and all remaining boxes are no taller; if it fits neither, no room is reachable for it at all and it is discarded. The two pointers close inward, so one sorted pass over the boxes settles it.

class Solution(object):
    def maxBoxesInWarehouse(self, boxes, warehouse):
        """
        :type boxes: List[int]
        :type warehouse: List[int]
        :rtype: int
        """
        boxes.sort()
        left, right = 0, len(warehouse) - 1
        placed = 0
        index = len(boxes) - 1
        while left <= right and index >= 0:
            box = boxes[index]
            if box <= warehouse[left]:
                left += 1
                placed += 1
            elif box <= warehouse[right]:
                right -= 1
                placed += 1
            index -= 1
        return placed
