# Author: Kaustav Ghosh
# Problem: Valid Palindrome IV
# Approach: You may change at most two characters (to any letter). Count the mismatched pairs when comparing the string with its reverse via two pointers; each mismatch needs one change to fix, so the string can be made a palindrome exactly when there are at most two such mismatched pairs

class Solution(object):
    def makePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, j = 0, len(s) - 1
        changes = 0
        while i < j:
            if s[i] != s[j]:
                changes += 1
                if changes > 2:
                    return False
            i += 1
            j -= 1
        return True
