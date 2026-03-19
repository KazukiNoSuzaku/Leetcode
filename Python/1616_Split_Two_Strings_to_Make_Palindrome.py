# Author: Kaustav Ghosh
# https://leetcode.com/problems/split-two-strings-to-make-palindrome/

class Solution(object):
    def checkPalindromeFormation(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: bool
        """
        def isPalin(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        def check(a, b):
            i, j = 0, len(a) - 1
            while i < j and a[i] == b[j]:
                i += 1
                j -= 1
            return isPalin(a, i, j) or isPalin(b, i, j)

        return check(a, b) or check(b, a)
