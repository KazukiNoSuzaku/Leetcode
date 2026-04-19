# Author: Kaustav Ghosh
# 2343. Query Kth Smallest Trimmed Number
# https://leetcode.com/problems/query-kth-smallest-trimmed-number/
# Difficulty: Medium
#
# For each query (k, trim): trim each number to last `trim` digits,
# sort (trimmed, index) pairs, return original index of kth smallest

class Solution(object):
    def smallestTrimmedNumbers(self, nums, queries):
        """
        :type nums: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        for k, trim in queries:
            trimmed = [(num[-trim:], i) for i, num in enumerate(nums)]
            trimmed.sort()
            ans.append(trimmed[k - 1][1])
        return ans
