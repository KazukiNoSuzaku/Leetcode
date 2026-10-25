# Author: Kaustav Ghosh
# Problem: Maximum Units on a Truck
# Approach: Every box occupies exactly one slot on the truck regardless of what it holds, so the slots are interchangeable and each should be filled with the most valuable box still available; that makes sorting by units per box descending and taking greedily optimal, with no need to consider combinations. The last box type taken may only partially fit, so it contributes the remaining capacity rather than its whole supply, and the loop stops as soon as the truck is full.

class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        total = 0
        for count, units in sorted(boxTypes, key=lambda box: box[1], reverse=True):
            taken = count if count < truckSize else truckSize
            total += taken * units
            truckSize -= taken
            if truckSize == 0:
                break
        return total
