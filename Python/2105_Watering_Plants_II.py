# Author: Kaustav Ghosh
# Problem: Watering Plants II
# Approach: Two pointers move inward, Alice from the left and Bob from the right, each refilling (counting a refill) when the current can cannot cover a plant. If they meet at a middle plant, the one with more water (Alice on ties) waters it, needing a refill only if that amount is insufficient

class Solution(object):
    def minimumRefill(self, plants, capacityA, capacityB):
        """
        :type plants: List[int]
        :type capacityA: int
        :type capacityB: int
        :rtype: int
        """
        i, j = 0, len(plants) - 1
        a, b = capacityA, capacityB
        refills = 0
        while i < j:
            if a >= plants[i]:
                a -= plants[i]
            else:
                refills += 1
                a = capacityA - plants[i]
            if b >= plants[j]:
                b -= plants[j]
            else:
                refills += 1
                b = capacityB - plants[j]
            i += 1
            j -= 1
        if i == j and max(a, b) < plants[i]:
            refills += 1
        return refills
