# Given an integer array nums, return true if it is possible to split the array into four
# non-empty contiguous subarrays with equal sums.

# Author: Kaustav Ghosh

class Solution(object):
    def splitArray(self, nums):
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        for j in range(3, n-2):
            thirds = set()
            for i in range(1, j-1):
                if prefix[i] == prefix[j] - prefix[i+1]:
                    thirds.add(prefix[i])
            for k in range(j+2, n-1):
                if prefix[k] - prefix[j+1] == prefix[n] - prefix[k+1]:
                    if prefix[k] - prefix[j+1] in thirds:
                        return True
        return False
