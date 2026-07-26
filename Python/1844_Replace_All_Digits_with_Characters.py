# Author: Kaustav Ghosh
# Problem: Replace All Digits with Characters
# Approach: Even indices are letters; each odd-index digit shifts the preceding letter forward by that amount

class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        chars = list(s)
        for i in range(1, len(chars), 2):
            chars[i] = chr(ord(chars[i - 1]) + int(chars[i]))
        return ''.join(chars)
