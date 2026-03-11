# Check if a string can be made a palindrome by deleting at most one character.

# Author: Kaustav Ghosh

class Solution(object):
    def validPalindrome(self, s):
        def is_palin(lo, hi):
            while lo < hi:
                if s[lo] != s[hi]: return False
                lo += 1; hi -= 1
            return True
        lo, hi = 0, len(s) - 1
        while lo < hi:
            if s[lo] != s[hi]:
                return is_palin(lo+1, hi) or is_palin(lo, hi-1)
            lo += 1; hi -= 1
        return True
