# Premium problem - not available without subscription
# Author: Kaustav Ghosh
# Typical approach: GCD of entire array == 1 (Bezout's identity)

class Solution(object):
    def isGoodArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        from math import gcd
        result = nums[0]
        for num in nums[1:]:
            result = gcd(result, num)
        return result == 1
