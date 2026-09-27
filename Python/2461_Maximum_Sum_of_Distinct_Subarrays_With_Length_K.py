# Author: Kaustav Ghosh
# Problem: Maximum Sum of Distinct Subarrays With Length K
# Approach: Slide a window of exactly k elements, keeping a running sum and a count per value. The window qualifies when it holds k distinct values, which is simply when the count map has k entries, so track the best sum among qualifying windows

from collections import defaultdict


class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        counts = defaultdict(int)
        total = 0
        best = 0
        for i, x in enumerate(nums):
            counts[x] += 1
            total += x
            if i >= k:
                leaving = nums[i - k]
                counts[leaving] -= 1
                if counts[leaving] == 0:
                    del counts[leaving]
                total -= leaving
            if i >= k - 1 and len(counts) == k:
                best = max(best, total)
        return best
