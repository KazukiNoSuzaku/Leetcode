# Author: Kaustav Ghosh
# Problem: 2264. Largest 3-Same-Digit Number in String
# URL: https://leetcode.com/problems/largest-3-same-digit-number-in-string/
# Difficulty: Easy
#
# Approach:
# Check from '9' down to '0' whether three consecutive same digits exist in num.
# Return the first (largest) found.

class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        for d in range(9, -1, -1):
            triple = str(d) * 3
            if triple in num:
                return triple
        return ""
