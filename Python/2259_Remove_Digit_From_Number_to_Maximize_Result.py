# Author: Kaustav Ghosh
# Problem: 2259. Remove Digit From Number to Maximize Result
# URL: https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/
# Difficulty: Easy
#
# Approach:
# Try removing each occurrence of digit and keep the lexicographically
# largest resulting string.

class Solution(object):
    def removeDigit(self, number, digit):
        """
        :type number: str
        :type digit: str
        :rtype: str
        """
        best = ""
        for i in range(len(number)):
            if number[i] == digit:
                candidate = number[:i] + number[i + 1:]
                if candidate > best:
                    best = candidate
        return best
