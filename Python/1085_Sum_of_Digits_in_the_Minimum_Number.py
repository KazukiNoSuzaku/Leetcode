# Author: Kaustav Ghosh
# 1085. Sum of Digits in the Minimum Number
# https://leetcode.com/problems/sum-of-digits-in-the-minimum-number/

class Solution(object):
    def sumOfDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = min(nums)
        digit_sum = sum(int(d) for d in str(m))
        return 0 if digit_sum % 2 == 0 else 1
