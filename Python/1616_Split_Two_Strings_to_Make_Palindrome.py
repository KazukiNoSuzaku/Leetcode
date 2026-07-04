# Author: Kaustav Ghosh
# Problem: Split Two Strings to Make Palindrome
# Approach: Greedily match a prefix of one string with a suffix of the other from both ends; the leftover middle must itself be a palindrome in one of the two strings

class Solution(object):
    def checkPalindromeFormation(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: bool
        """
        def is_pal(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        def check(x, y):
            i, j = 0, len(x) - 1
            while i < j and x[i] == y[j]:
                i += 1
                j -= 1
            # Middle must be a palindrome within one of the strings
            return is_pal(x, i, j) or is_pal(y, i, j)

        return check(a, b) or check(b, a)
