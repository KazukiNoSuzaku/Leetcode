# Author: Kaustav Ghosh
# Problem: Maximize the Beauty of the Garden
# Approach: Once the two ends are fixed the inside is free, so every flower strictly between them is kept exactly when its beauty is positive, which makes the best garden for a chosen pair of equal ends computable from a prefix sum that only accumulates positive values. For a given beauty value the earliest occurrence is always the better left end, because widening the span can only add non-negative contributions, so one pass remembering each value's first position scores every candidate pair as it is met.

class Solution(object):
    def maximumBeauty(self, flowers):
        """
        :type flowers: List[int]
        :rtype: int
        """
        positives = [0] * (len(flowers) + 1)
        first = {}
        best = None
        for index, beauty in enumerate(flowers):
            if beauty in first:
                inside = positives[index] - positives[first[beauty] + 1]
                candidate = inside + beauty * 2
                if best is None or candidate > best:
                    best = candidate
            else:
                first[beauty] = index
            positives[index + 1] = positives[index] + (beauty if beauty > 0 else 0)
        return best
