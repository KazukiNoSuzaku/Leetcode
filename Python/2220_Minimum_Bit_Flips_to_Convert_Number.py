# Author: Kaustav Ghosh
# Problem: Minimum Bit Flips to Convert Number
# Approach: A bit must be flipped exactly where start and goal differ, which is where their XOR has set bits; count those set bits

class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        return bin(start ^ goal).count('1')
