# Author: Kaustav Ghosh
# Problem: Find Subsequence of Length K With the Largest Sum
# Approach: Pick the indices of the k largest values, then output those elements in original index order to preserve the subsequence

class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        top_indices = sorted(range(len(nums)), key=lambda i: nums[i], reverse=True)[:k]
        top_indices.sort()
        return [nums[i] for i in top_indices]
