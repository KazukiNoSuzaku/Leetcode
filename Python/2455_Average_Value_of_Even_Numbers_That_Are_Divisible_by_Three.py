# Author: Kaustav Ghosh
# Problem: Average Value of Even Numbers That Are Divisible by Three
# Approach: A number that is both even and divisible by three is exactly a multiple of six, so collect those and return their integer average, or 0 when there are none

class Solution(object):
    def averageValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        multiples = [x for x in nums if x % 6 == 0]
        return sum(multiples) // len(multiples) if multiples else 0
