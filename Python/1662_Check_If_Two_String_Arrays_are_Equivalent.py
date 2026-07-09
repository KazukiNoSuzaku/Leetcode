# Author: Kaustav Ghosh
# Problem: Check If Two String Arrays are Equivalent
# Approach: Concatenate each array into one string and compare

class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        return ''.join(word1) == ''.join(word2)
