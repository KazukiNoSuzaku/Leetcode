# Author: Kaustav Ghosh
# Problem: Count Pairs in Two Arrays (Premium)
# Approach: nums1[i]+nums1[j] > nums2[i]+nums2[j] rearranges to d[i]+d[j] > 0 where d = nums1 - nums2; sort d and two-pointer count pairs with positive sum

class Solution(object):
    def countPairs(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        diff = sorted(a - b for a, b in zip(nums1, nums2))
        count = 0
        left, right = 0, len(diff) - 1
        while left < right:
            if diff[left] + diff[right] > 0:
                count += right - left  # all indices between also pair with right
                right -= 1
            else:
                left += 1
        return count
