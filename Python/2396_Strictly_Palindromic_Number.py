# Author: Kaustav Ghosh
# Problem: Strictly Palindromic Number
# Approach: Every n >= 4 is written "12" in base n - 2, because n = 1 * (n - 2) + 2, and "12" is not a palindrome. Since the constraints start at n = 4, no input can be strictly palindromic

class Solution(object):
    def isStrictlyPalindromic(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return False
