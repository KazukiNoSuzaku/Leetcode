# Author: Kaustav Ghosh
# Problem: Kth Smallest Subarray Sum
# Approach: Counting how many subarrays have a sum at most some bound is easy because every element is positive: as the right end advances the window's sum only grows, so the left end never has to move backwards and one sliding pass counts them all. That count rises with the bound, which makes the kth smallest sum the smallest bound whose count reaches k, found by binary search between the smallest single element and the total of the whole array. Each probe is linear, so the whole search is linear times the logarithm of the total rather than quadratic in the array length.

class Solution(object):
    def kthSmallestSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :rtype: int
        """
        def atMost(bound):
            count = 0
            window = 0
            left = 0
            for right, value in enumerate(nums):
                window += value
                while window > bound:
                    window -= nums[left]
                    left += 1
                count += right - left + 1
            return count

        low, high = min(nums), sum(nums)
        while low < high:
            middle = (low + high) // 2
            if atMost(middle) >= k:
                high = middle
            else:
                low = middle + 1
        return low
