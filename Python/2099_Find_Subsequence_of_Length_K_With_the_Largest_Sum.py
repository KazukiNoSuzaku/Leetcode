# Author: Kaustav Ghosh
# Problem 2099: Find Subsequence of Length K With the Largest Sum

class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Find the k-th largest value as threshold
        sorted_nums = sorted(nums, reverse=True)
        threshold = sorted_nums[k - 1]
        # Count how many values strictly greater than threshold we need
        greater_count = sum(1 for x in sorted_nums[:k] if x > threshold)
        equal_needed = k - greater_count
        result = []
        for num in nums:
            if num > threshold:
                result.append(num)
            elif num == threshold and equal_needed > 0:
                result.append(num)
                equal_needed -= 1
        return result
