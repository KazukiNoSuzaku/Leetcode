# Premium problem - not available without subscription
# Author: Kaustav Ghosh
# Typical approach: Count occurrences across all rows, first element appearing in all rows

class Solution(object):
    def smallestCommonElement(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        from collections import Counter
        count = Counter()
        rows = len(mat)
        for row in mat:
            for val in row:
                count[val] += 1
                if count[val] == rows:
                    return val
        return -1
