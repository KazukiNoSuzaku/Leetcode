# Check if the last character must be a 1-bit character in a binary coding scheme.

# Author: Kaustav Ghosh

class Solution(object):
    def isOneBitCharacter(self, bits):
        i = 0
        while i < len(bits) - 1:
            if bits[i] == 1: i += 2
            else: i += 1
        return i == len(bits) - 1
