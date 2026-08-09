# Author: Kaustav Ghosh
# Problem: Number of Strings That Appear as Substrings in Word
# Approach: Count how many patterns occur as a substring of word using Python's in operator

class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        return sum(1 for p in patterns if p in word)
