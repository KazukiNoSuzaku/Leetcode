# Author: Kaustav Ghosh
# Manhattan distance trick: expand absolute values into 4 combinations

class Solution(object):
    def maxAbsValExpr(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        res = 0
        for p, q in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            max_val = float('-inf')
            min_val = float('inf')
            for i in range(len(arr1)):
                val = p * arr1[i] + q * arr2[i] + i
                max_val = max(max_val, val)
                min_val = min(min_val, val)
            res = max(res, max_val - min_val)
        return res
