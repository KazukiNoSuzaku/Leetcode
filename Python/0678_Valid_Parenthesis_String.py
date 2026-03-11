# Check if a string with '(', ')' and '*' (can be either or empty) is valid.

# Author: Kaustav Ghosh

class Solution(object):
    def checkValidString(self, s):
        lo = hi = 0
        for c in s:
            if c == '(':
                lo += 1; hi += 1
            elif c == ')':
                lo -= 1; hi -= 1
            else:
                lo -= 1; hi += 1
            if hi < 0: return False
            lo = max(lo, 0)
        return lo == 0
