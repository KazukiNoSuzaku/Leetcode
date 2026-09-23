# Author: Kaustav Ghosh
# Problem: Minimize XOR
# Approach: The answer must carry as many set bits as num2. Spending them on the highest bits num1 already has zeroes out the most significant differences, and any bits still owed go into the lowest free positions, where they cost the least

class Solution(object):
    def minimizeXor(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        needed = bin(num2).count('1')
        result = 0
        for bit in range(31, -1, -1):
            if needed and num1 >> bit & 1:
                result |= 1 << bit
                needed -= 1
        for bit in range(32):
            if needed and not result >> bit & 1:
                result |= 1 << bit
                needed -= 1
        return result
