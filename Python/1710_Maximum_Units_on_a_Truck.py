# Author: Kaustav Ghosh
# Problem: Maximum Units on a Truck
# Approach: Greedily load box types with the most units per box first until the truck is full

class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        boxTypes.sort(key=lambda b: b[1], reverse=True)
        total = 0
        for count, units in boxTypes:
            take = min(count, truckSize)
            total += take * units
            truckSize -= take
            if truckSize == 0:
                break
        return total
