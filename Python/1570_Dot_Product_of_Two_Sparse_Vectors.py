# Author: Kaustav Ghosh
# Problem: Dot Product of Two Sparse Vectors (Premium)
# Approach: Store only non-zero entries as {index: value}; for the dot product iterate the smaller map and look up matching indices

class SparseVector:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nonzero = {i: v for i, v in enumerate(nums) if v != 0}

    def dotProduct(self, vec):
        """
        :type vec: 'SparseVector'
        :rtype: int
        """
        a, b = self.nonzero, vec.nonzero
        if len(a) > len(b):
            a, b = b, a
        return sum(val * b[i] for i, val in a.items() if i in b)


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
