# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must appear as many times as it shows in both arrays
# and you may return the result in any order.

# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]

# Constraints:
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000

# Author: Kaustav Ghosh

from collections import Counter

class Solution(object):
    def intersect(self, nums1, nums2):
        c1, c2 = Counter(nums1), Counter(nums2)
        res = []
        for n in c1:
            if n in c2:
                res.extend([n] * min(c1[n], c2[n]))
        return res
