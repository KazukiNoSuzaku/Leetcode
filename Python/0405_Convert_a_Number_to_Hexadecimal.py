# Given an integer num, return a string representing its hexadecimal representation.
# For negative integers, two's complement method is used.
# You must not use any built-in library method to solve this problem.

# Author: Kaustav Ghosh

class Solution(object):
    def toHex(self, num):
        if num == 0:
            return '0'
        if num < 0:
            num += 2 ** 32
        hex_chars = '0123456789abcdef'
        res = ''
        while num:
            res = hex_chars[num % 16] + res
            num //= 16
        return res
