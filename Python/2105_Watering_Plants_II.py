# Author: Kaustav Ghosh
# https://leetcode.com/problems/watering-plants-ii/

class Solution(object):
    def minimumRefill(self, plants, capacityA, capacityB):
        """
        :type plants: List[int]
        :type capacityA: int
        :type capacityB: int
        :rtype: int
        """
        n = len(plants)
        left, right = 0, n - 1
        a, b = capacityA, capacityB
        refills = 0

        while left < right:
            if a < plants[left]:
                refills += 1
                a = capacityA
            a -= plants[left]
            left += 1

            if b < plants[right]:
                refills += 1
                b = capacityB
            b -= plants[right]
            right -= 1

        if left == right:
            if max(a, b) < plants[left]:
                refills += 1

        return refills
