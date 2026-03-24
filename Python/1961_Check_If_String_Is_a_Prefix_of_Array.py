# Author: Kaustav Ghosh
# https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/

class Solution(object):
    def isPrefixString(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: bool
        """
        current = ""
        for w in words:
            current += w
            if current == s:
                return True
            if len(current) > len(s):
                return False
        return False
