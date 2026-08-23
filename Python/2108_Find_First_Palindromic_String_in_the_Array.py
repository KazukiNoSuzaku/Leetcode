# Author: Kaustav Ghosh
# Problem: Find First Palindromic String in the Array
# Approach: Return the first word equal to its reverse, or empty string if none

class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for w in words:
            if w == w[::-1]:
                return w
        return ""
