# Author: Kaustav Ghosh
# Problem: 2220. Minimum Bit Flips to Convert Number
# URL: https://leetcode.com/problems/minimum-bit-flips-to-convert-number/
# Difficulty: Easy
#
# Approach:
# XOR of start and goal gives a number whose set bits represent exactly the
# positions where start and goal differ. Count those set bits (popcount).

class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        return bin(start ^ goal).count('1')
