# Author: Kaustav Ghosh
# Problem: Merge Strings Alternately
# Approach: Zip the two words together, padding the shorter with empty strings so the longer's tail is appended after they run out

from itertools import zip_longest

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        return ''.join(a + b for a, b in zip_longest(word1, word2, fillvalue=''))
