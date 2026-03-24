# Author: Kaustav Ghosh
# Problem 2000: Reverse Prefix of Word

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
