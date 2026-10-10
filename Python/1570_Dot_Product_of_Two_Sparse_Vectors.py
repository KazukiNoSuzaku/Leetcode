# Author: Kaustav Ghosh
# Problem: Dot Product of Two Sparse Vectors
# Approach: Storing the full vector would make every dot product cost O(n) regardless of how few entries are non-zero, so the constructor keeps only a dictionary of index to value for the non-zero entries. A term contributes to the product only when both vectors are non-zero at that index, so the product iterates over whichever of the two dictionaries is smaller and looks the other index up, which also answers the follow-up: when just one vector is sparse the work is bounded by that sparse vector's entry count.

class SparseVector(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.entries = {i: value for i, value in enumerate(nums) if value}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        """
        :type vec: 'SparseVector'
        :rtype: int
        """
        mine, theirs = self.entries, vec.entries
        if len(theirs) < len(mine):
            mine, theirs = theirs, mine
        return sum(value * theirs[i] for i, value in mine.items() if i in theirs)


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
