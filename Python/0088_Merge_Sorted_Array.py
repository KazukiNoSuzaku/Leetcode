# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two
# integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned but instead stored inside the array nums1.

# Example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]

# Example 2:
# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]

# Constraints:
# nums1.length == m + n
# nums2.length == n
# 0 <= m, n <= 200
# -10^9 <= nums1[i], nums2[i] <= 10^9

# Author: Kaustav Ghosh

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        p1, p2, p = m - 1, n - 1, m + n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
