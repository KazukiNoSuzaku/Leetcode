# Author: Kaustav Ghosh
# Problem: Maximum Points in an Archery Competition
# Approach: There are only 12 sections, so enumerate every subset of sections Bob tries to win. Winning section i costs aliceArrows[i]+1 arrows and yields i points. Keep the affordable subset with the most points, then assign the required arrows to those sections and dump any leftover arrows into section 0

class Solution(object):
    def maximumBobPoints(self, numArrows, aliceArrows):
        """
        :type numArrows: int
        :type aliceArrows: List[int]
        :rtype: List[int]
        """
        n = 12
        best_points = -1
        best_mask = 0
        for mask in range(1 << n):
            cost = 0
            points = 0
            for i in range(n):
                if mask & (1 << i):
                    cost += aliceArrows[i] + 1
                    points += i
            if cost <= numArrows and points > best_points:
                best_points = points
                best_mask = mask

        result = [0] * n
        used = 0
        for i in range(n):
            if best_mask & (1 << i):
                result[i] = aliceArrows[i] + 1
                used += result[i]
        # leftover arrows dumped into section 0 (scores nothing for Bob)
        result[0] += numArrows - used
        return result
