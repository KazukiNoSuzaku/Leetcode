# Author: Kaustav Ghosh
# Problem: Count Subarrays With Median K
# Approach: The values are distinct, so only how many entries beat k matters, not which. A subarray containing k has median k exactly when the count of larger values minus the count of smaller ones is 0 or 1. Tally that balance for every stretch to the right of k, then sweep left and pair each left balance with the two right balances that complete it

from collections import defaultdict


class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        position = nums.index(k)
        right_counts = defaultdict(int)
        right_counts[0] = 1
        balance = 0
        for i in range(position + 1, len(nums)):
            balance += 1 if nums[i] > k else -1
            right_counts[balance] += 1
        total = right_counts[0] + right_counts[1]
        balance = 0
        for i in range(position - 1, -1, -1):
            balance += 1 if nums[i] > k else -1
            total += right_counts[-balance] + right_counts[1 - balance]
        return total
