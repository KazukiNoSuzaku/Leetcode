# Author: Kaustav Ghosh
# Problem: Minimum Split Into Subarrays With GCD Greater Than One
# Approach: Extending a subarray can only shrink its gcd, so carry the running gcd and cut only when it would drop to 1. Cutting as late as possible is optimal, since every piece of any other valid split fits inside one of these

from math import gcd


class Solution(object):
    def minimumSplits(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        splits = 1
        current = nums[0]
        for x in nums[1:]:
            current = gcd(current, x)
            if current == 1:
                splits += 1
                current = x
        return splits
