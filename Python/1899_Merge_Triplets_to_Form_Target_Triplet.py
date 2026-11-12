# Author: Kaustav Ghosh
# Problem: Merge Triplets to Form Target Triplet
# Approach: A merge takes the component-wise maximum, so a value once reached can never be lowered, which means any triplet exceeding the target in any component is poison and must never be used. Every other triplet is harmless to include, since taking its maximum can only push components towards the target without overshooting, so the best achievable result is the component-wise maximum of all the usable triplets. Comparing that against the target answers the question in one pass.

class Solution(object):
    def mergeTriplets(self, triplets, target):
        """
        :type triplets: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        reached = [0, 0, 0]
        for triplet in triplets:
            if all(value <= limit for value, limit in zip(triplet, target)):
                reached = [max(have, value) for have, value in zip(reached, triplet)]
        return reached == list(target)
