# Author: Kaustav Ghosh
# Problem: Widest Pair of Indices With Equal Range Sum
# Approach: Equal range sums mean the difference array nums1[k]-nums2[k] has a zero-sum subarray. Track the first index where each running prefix sum appears; a repeat marks a zero-sum span whose width is the index gap

class Solution(object):
    def widestPairOfIndices(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        first_seen = {0: 0}
        prefix = 0
        best = 0
        for idx in range(len(nums1)):
            prefix += nums1[idx] - nums2[idx]
            pos = idx + 1
            if prefix in first_seen:
                best = max(best, pos - first_seen[prefix])
            else:
                first_seen[prefix] = pos
        return best
