# Author: Kaustav Ghosh
# Problem 1844: Replace All Digits with Characters

class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = list(s)
        for i in range(1, len(s), 2):
            result[i] = chr(ord(s[i - 1]) + int(s[i]))
        return "".join(result)
