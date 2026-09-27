# Author: Kaustav Ghosh
# Problem: Number of Subarrays With LCM Equal to K
# Approach: For each start, extend the subarray while keeping the running lcm. The lcm only grows, so once it stops dividing k no longer subarray from this start can work and the scan breaks early; count the extensions whose lcm lands exactly on k

from math import gcd


class Solution(object):
    def subarrayLCM(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        total = 0
        for i in range(len(nums)):
            current = 1
            for j in range(i, len(nums)):
                current = current * nums[j] // gcd(current, nums[j])
                if k % current:
                    break
                total += current == k
        return total
