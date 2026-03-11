# The complement of an integer is the integer you get when you flip all the 0's to 1's
# and all the 1's to 0's in its binary representation.
# Given an integer num, return its complement.

# Author: Kaustav Ghosh

class Solution(object):
    def findComplement(self, num):
        mask = (1 << num.bit_length()) - 1
        return num ^ mask
