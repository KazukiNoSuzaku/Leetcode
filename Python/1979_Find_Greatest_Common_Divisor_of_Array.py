# Author: Kaustav Ghosh
# Problem: Find Greatest Common Divisor of Array
# Approach: Only the smallest and the largest element are asked about, so there is nothing to accumulate across the array: one pass to find the two extremes, then one greatest common divisor. I use the Euclidean algorithm from the standard library, which runs in time logarithmic in the smaller value, so the whole thing is dominated by the single scan for the minimum and maximum and is O(n). The values are at least one, so the divisor is always well defined even when the smallest and largest coincide, in which case the answer is that shared value.

from math import gcd

class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return gcd(min(nums), max(nums))
