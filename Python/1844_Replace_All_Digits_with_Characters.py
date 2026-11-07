# Author: Kaustav Ghosh
# Problem: Replace All Digits with Characters
# Approach: The odd positions always hold digits and the even positions always hold letters, so each digit is replaced by shifting the letter immediately before it forward by that many places in the alphabet. Because the letter at an even position is never itself rewritten, the shift can read straight from the original string and the pieces are collected and joined once.

class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        pieces = []
        for index, character in enumerate(s):
            if index % 2 == 0:
                pieces.append(character)
            else:
                pieces.append(chr(ord(s[index - 1]) + int(character)))
        return "".join(pieces)
