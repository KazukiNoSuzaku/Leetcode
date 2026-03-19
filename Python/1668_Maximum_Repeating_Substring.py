# Author: Kaustav Ghosh
# https://leetcode.com/problems/maximum-repeating-substring/

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
