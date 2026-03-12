# Premium problem - not available without subscription
# Author: Kaustav Ghosh
# Typical approach: Sort weights, greedily add lightest until exceeding 5000

class Solution(object):
    def maxNumberOfApples(self, weight):
        """
        :type weight: List[int]
        :rtype: int
        """
        weight.sort()
        total = 0
        for i, w in enumerate(weight):
            total += w
            if total > 5000:
                return i
        return len(weight)
