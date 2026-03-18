# Author: Kaustav Ghosh
# Problem: 1570 - Dot Product of Two Sparse Vectors (Premium)
# Approach: Store non-zero indices in dict, iterate over smaller dict

class SparseVector(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.data = {i: v for i, v in enumerate(nums) if v != 0}

    def dotProduct(self, vec):
        """
        :type vec: SparseVector
        :rtype: int
        """
        result = 0
        smaller, larger = (self.data, vec.data) if len(self.data) <= len(vec.data) else (vec.data, self.data)
        for i, v in smaller.items():
            if i in larger:
                result += v * larger[i]
        return result
