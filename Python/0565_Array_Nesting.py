# You are given an integer array nums of length n where nums is a permutation of [0, n-1].
# Return the longest length of a set s such that s[0], s[nums[s[0]]], s[nums[nums[s[0]]]], ...
# (s[nums[...]] forever) are all contained in nums.

# Author: Kaustav Ghosh

class Solution(object):
    def arrayNesting(self, nums):
        seen = [False] * len(nums)
        res = 0
        for i in range(len(nums)):
            if not seen[i]:
                count, j = 0, i
                while not seen[j]:
                    seen[j] = True
                    j = nums[j]
                    count += 1
                res = max(res, count)
        return res
