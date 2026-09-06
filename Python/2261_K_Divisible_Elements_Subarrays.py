# Author: Kaustav Ghosh
# Problem: K Divisible Elements Subarrays
# Approach: Enumerate every subarray, extending each start until more than k elements are divisible by p. Collect the distinct subarrays (as tuples) in a set and return its size

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
            div = 0
            for j in range(i, n):
                if nums[j] % p == 0:
                    div += 1
                if div > k:
                    break
                seen.add(tuple(nums[i:j + 1]))
        return len(seen)
