# Author: Kaustav Ghosh
# Problem 2079: Watering Plants

class Solution(object):
    def wateringPlants(self, plants, capacity):
        """
        :type plants: List[int]
        :type capacity: int
        :rtype: int
        """
        steps = 0
        water = capacity
        for i in range(len(plants)):
            if water >= plants[i]:
                steps += 1
                water -= plants[i]
            else:
                # Walk back to refill and return
                steps += 2 * i + 1
                water = capacity - plants[i]
        return steps
