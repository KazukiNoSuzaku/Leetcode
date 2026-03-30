# Author: Kaustav Ghosh
# Problem: 2176. Count Equal and Divisible Pairs in an Array
# URL: https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/
# Approach: Brute force O(n^2) - check every pair (i, j) where i < j,
#           nums[i] == nums[j], and (i * j) % k == 0.

class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    count += 1
        return count
