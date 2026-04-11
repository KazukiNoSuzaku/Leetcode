# Author: Kaustav Ghosh
# Problem: 2261. K Divisible Elements Subarrays
# URL: https://leetcode.com/problems/k-divisible-elements-subarrays/
# Difficulty: Medium
#
# Approach:
# Enumerate all subarrays, count elements divisible by p, and if count <= k
# add the subarray as a tuple to a set for deduplication.

class Solution(object):
    def countDistinct(self, nums, k, p):
        """
        :type nums: List[int]
        :type k: int
        :type p: int
        :rtype: int
        """
        n = len(nums)
        seen = set()
        for i in range(n):
            count = 0
            for j in range(i, n):
                if nums[j] % p == 0:
                    count += 1
                if count > k:
                    break
                seen.add(tuple(nums[i:j + 1]))
        return len(seen)
