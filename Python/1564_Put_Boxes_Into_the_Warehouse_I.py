# Author: Kaustav Ghosh
# Problem: Put Boxes Into the Warehouse I
# Approach: Because boxes enter only from the left and stop at the first room shorter than themselves, room j is really capped by the shortest room anywhere to its left, so I first replace the heights by that running minimum, which makes the usable heights non-increasing. Then the smallest boxes are the only ones that can reach the deepest rooms, so I sort the boxes and walk a pointer inward from the far end of the warehouse: each box takes the deepest room still tall enough, and once no room fits the smallest remaining box none will fit the larger ones either.

class Solution(object):
    def maxBoxesInWarehouse(self, boxes, warehouse):
        """
        :type boxes: List[int]
        :type warehouse: List[int]
        :rtype: int
        """
        n = len(warehouse)
        usable = list(warehouse)
        for i in range(1, n):
            if usable[i - 1] < usable[i]:
                usable[i] = usable[i - 1]

        boxes.sort()
        placed = 0
        room = n - 1
        for box in boxes:
            while room >= 0 and usable[room] < box:
                room -= 1
            if room < 0:
                break
            placed += 1
            room -= 1
        return placed
