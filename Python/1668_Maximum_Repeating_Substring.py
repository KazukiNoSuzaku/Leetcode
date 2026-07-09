# Author: Kaustav Ghosh
# Problem: Maximum Repeating Substring
# Approach: Keep concatenating word to itself and increase k while that repetition is still a substring of sequence

class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        k = 0
        while word * (k + 1) in sequence:
            k += 1
        return k
