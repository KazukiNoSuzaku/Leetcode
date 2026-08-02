# Author: Kaustav Ghosh
# Problem: Merge Triplets to Form Target Triplet
# Approach: Only triplets whose every component is within target can be merged; among those, take the elementwise max and check it equals target

class Solution(object):
    def mergeTriplets(self, triplets, target):
        """
        :type triplets: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        tx, ty, tz = target
        best = [0, 0, 0]
        for x, y, z in triplets:
            if x <= tx and y <= ty and z <= tz:
                best[0] = max(best[0], x)
                best[1] = max(best[1], y)
                best[2] = max(best[2], z)
        return best == target
