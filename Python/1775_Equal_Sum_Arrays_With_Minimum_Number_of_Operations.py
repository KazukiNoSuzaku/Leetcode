# Author: Kaustav Ghosh
# Problem: Equal Sum Arrays With Minimum Number of Operations
# Approach: Only the gap between the two sums matters, and every single change moves it by a known amount: an element of the heavier array dropping to 1 closes the gap by value minus one, while an element of the lighter array rising to 6 closes it by six minus value. Each change is independent and worth at most five, so taking the largest available gains first is optimal, and since gains only range over one to five they are bucketed by counting instead of sorted. If the gains cannot cover the gap the arrays can never match.

class Solution(object):
    def minOperations(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        if len(nums1) * 6 < len(nums2) or len(nums2) * 6 < len(nums1):
            return -1
        if sum(nums1) < sum(nums2):
            nums1, nums2 = nums2, nums1

        gap = sum(nums1) - sum(nums2)
        gains = [0] * 6
        for value in nums1:
            gains[value - 1] += 1
        for value in nums2:
            gains[6 - value] += 1

        operations = 0
        for gain in range(5, 0, -1):
            if gap <= 0:
                break
            used = min(gains[gain], -(-gap // gain))
            operations += used
            gap -= used * gain
        return operations
