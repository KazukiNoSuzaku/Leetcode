# Find minimum parentheses to add to make string valid.

# Author: Kaustav Ghosh

class Solution(object):
    def minAddToMakeValid(self, s):
        open_needed = close_needed = 0
        for c in s:
            if c == '(':
                close_needed += 1
            elif close_needed > 0:
                close_needed -= 1
            else:
                open_needed += 1
        return open_needed + close_needed
