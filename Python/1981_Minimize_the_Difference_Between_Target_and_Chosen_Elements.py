# Author: Kaustav Ghosh
# Problem 1981: Minimize the Difference Between Target and Chosen Elements

class Solution(object):
    def minimizeTheDifference(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: int
        :rtype: int
        """
        possible = {0}
        for row in mat:
            new_possible = set()
            for s in possible:
                for val in row:
                    new_possible.add(s + val)
            # Prune sums that are too large (keep only relevant ones)
            min_above = float('inf')
            pruned = set()
            for s in new_possible:
                if s >= target:
                    if s < min_above:
                        min_above = s
                else:
                    pruned.add(s)
            if min_above != float('inf'):
                pruned.add(min_above)
            possible = pruned
        return min(abs(s - target) for s in possible)
