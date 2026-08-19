# Author: Kaustav Ghosh
# Problem: Watering Plants
# Approach: Walk plant to plant. If the can holds enough, water it in one step; otherwise walk back to the river and return, costing 2*i+1 steps, then refill. Accumulate the steps

class Solution(object):
    def wateringPlants(self, plants, capacity):
        """
        :type plants: List[int]
        :type capacity: int
        :rtype: int
        """
        steps = 0
        water = capacity
        for i, need in enumerate(plants):
            if water >= need:
                steps += 1
                water -= need
            else:
                steps += 2 * i + 1
                water = capacity - need
        return steps
