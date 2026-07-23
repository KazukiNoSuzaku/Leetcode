# Author: Kaustav Ghosh
# Problem: Sign of the Product of an Array
# Approach: Any zero makes the product 0; otherwise flip the sign for each negative and report it

class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sign = 1
        for x in nums:
            if x == 0:
                return 0
            if x < 0:
                sign = -sign
        return sign
