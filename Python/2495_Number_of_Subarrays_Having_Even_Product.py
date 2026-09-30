# Author: Kaustav Ghosh
# Problem: Number of Subarrays Having Even Product
# Approach: A product is odd only when every factor is odd, so count the subarrays made entirely of odd numbers, which a run of length L contributes L of at each step, and subtract that from all n * (n + 1) / 2 subarrays

class Solution(object):
    def evenProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        odd_run = 0
        all_odd = 0
        for x in nums:
            odd_run = odd_run + 1 if x % 2 else 0
            all_odd += odd_run
        return n * (n + 1) // 2 - all_odd
