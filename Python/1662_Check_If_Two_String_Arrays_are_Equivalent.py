# Author: Kaustav Ghosh
# Problem: Check If Two String Arrays are Equivalent
# Approach: Only the concatenation matters, not how it was split, so the two arrays are equivalent exactly when their joined forms are identical. The total length is bounded by a thousand characters, so joining is cheap and the comparison is a single string equality; a streaming two-pointer walk over both arrays would avoid the intermediate strings but buys nothing at this size and reads far less clearly.

class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        return ''.join(word1) == ''.join(word2)
