# Author: Kaustav Ghosh
# Problem: 2278. Percentage of Letter in String
# URL: https://leetcode.com/problems/percentage-of-letter-in-string/
# Difficulty: Easy
#
# Approach:
# Count occurrences of letter in s and compute floor percentage.

class Solution(object):
    def percentageLetter(self, s, letter):
        """
        :type s: str
        :type letter: str
        :rtype: int
        """
        return s.count(letter) * 100 // len(s)
