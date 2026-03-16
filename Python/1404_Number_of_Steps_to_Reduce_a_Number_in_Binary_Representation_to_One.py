# Author: Kaustav Ghosh
# Problem: Number of Steps to Reduce a Number in Binary Representation to One
# Approach: Simulate on binary string

class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        steps = 0
        carry = 0
        for i in range(len(s) - 1, 0, -1):
            digit = int(s[i]) + carry
            if digit % 2 == 1:
                steps += 2  # add 1 then divide
                carry = 1
            else:
                steps += 1  # divide
        return steps + carry
