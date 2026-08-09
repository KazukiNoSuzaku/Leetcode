# Author: Kaustav Ghosh
# Problem: Find Greatest Common Divisor of Array
# Approach: The GCD of the smallest and largest elements is the answer

from math import gcd

class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return gcd(min(nums), max(nums))
