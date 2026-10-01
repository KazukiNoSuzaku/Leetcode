# Author: Kaustav Ghosh
# Problem: Count the Digits That Divide a Number
# Approach: Walk the decimal digits of num and count those that divide it; the constraints guarantee no digit is zero, so no division needs guarding

class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return sum(1 for digit in str(num) if num % int(digit) == 0)
