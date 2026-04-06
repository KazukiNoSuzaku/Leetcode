# Author: Kaustav Ghosh
# Problem: 2216. Minimum Deletions to Make Array Beautiful
# URL: https://leetcode.com/problems/minimum-deletions-to-make-array-beautiful/
# Difficulty: Medium
#
# Approach:
# A beautiful array has even length and for every even index i,
# nums[i] != nums[i+1]. We greedily build the result: walk through the array
# keeping a counter of how many elements we have placed. When we're about to
# place an element at an even position and it equals the previous element
# (which sits at the position just before it in the result), we skip/delete
# it. After processing, if the result has odd length we delete one more.
# Equivalently: count deletions directly without building the array.

class Solution(object):
    def minDeletion(self, nums):
        """
        :type nums: list[int]
        :rtype: int
        """
        deletions = 0
        n = len(nums)
        i = 0
        while i < n:
            # Current effective position in the result = i - deletions
            # If it's an even position and next element (i+1) is the same,
            # we must delete nums[i].
            pos = i - deletions
            if pos % 2 == 0 and i + 1 < n and nums[i] == nums[i + 1]:
                deletions += 1
            i += 1
        # Result length after deletions = n - deletions; must be even
        if (n - deletions) % 2 == 1:
            deletions += 1
        return deletions
