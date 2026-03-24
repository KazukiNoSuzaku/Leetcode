# Author: Kaustav Ghosh
# https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/

class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        return sum(1 for p in patterns if p in word)
