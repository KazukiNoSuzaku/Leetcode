# Given an integer array nums, return all the different possible non-decreasing subsequences
# of the given array with at least two elements.

# Author: Kaustav Ghosh

class Solution(object):
    def findSubsequences(self, nums):
        res = set()

        def dfs(start, path):
            if len(path) >= 2:
                res.add(tuple(path))
            for i in range(start, len(nums)):
                if not path or nums[i] >= path[-1]:
                    dfs(i + 1, path + [nums[i]])

        dfs(0, [])
        return list(res)
