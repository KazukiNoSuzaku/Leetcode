# Author: Kaustav Ghosh
# Problem: Equal Sum Arrays With Minimum Number of Operations
# Approach: Close the sum gap greedily using the moves with the largest potential change first - raising the smaller array's small values toward 6 and lowering the larger array's big values toward 1

class Solution(object):
    def minOperations(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        if 6 * len(nums1) < len(nums2) or 6 * len(nums2) < len(nums1):
            return -1  # ranges cannot possibly meet

        diff = sum(nums1) - sum(nums2)
        if diff < 0:
            nums1, nums2 = nums2, nums1
            diff = -diff

        # gains available: lower a big value in nums1 (x-1), raise a small value in nums2 (6-y)
        gains = [x - 1 for x in nums1] + [6 - y for y in nums2]
        gains.sort(reverse=True)

        operations = 0
        for g in gains:
            if diff <= 0:
                break
            diff -= g
            operations += 1
        return operations
