# Author: Kaustav Ghosh
# Problem: Percentage of Letter in String
# Approach: Count occurrences of the letter and return its floored percentage of the string length

class Solution(object):
    def percentageLetter(self, s, letter):
        """
        :type s: str
        :type letter: str
        :rtype: int
        """
        return s.count(letter) * 100 // len(s)
