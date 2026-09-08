# Author: Kaustav Ghosh
# Problem: Maximum Bags With Full Capacity of Rocks
# Approach: Each bag needs capacity[i]-rocks[i] more rocks to be full. Fill the bags needing the fewest rocks first (sort the deficits ascending) while the additional rocks last, counting how many bags reach full

class Solution(object):
    def maximumBags(self, capacity, rocks, additionalRocks):
        """
        :type capacity: List[int]
        :type rocks: List[int]
        :type additionalRocks: int
        :rtype: int
        """
        deficits = sorted(c - r for c, r in zip(capacity, rocks))
        count = 0
        for need in deficits:
            if need <= additionalRocks:
                additionalRocks -= need
                count += 1
            else:
                break
        return count
