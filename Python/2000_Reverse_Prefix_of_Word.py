# Author: Kaustav Ghosh
# Problem: Reverse Prefix of Word
# Approach: Find the first occurrence of ch and reverse the segment from the start through it; if ch is absent, return the word unchanged

class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        idx = word.find(ch)
        if idx == -1:
            return word
        return word[:idx + 1][::-1] + word[idx + 1:]
