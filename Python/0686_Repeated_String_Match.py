# Find minimum number of times to repeat string a so b is a substring.

# Author: Kaustav Ghosh

class Solution(object):
    def repeatedStringMatch(self, a, b):
        times = (len(b) + len(a) - 1) // len(a)
        for t in [times, times + 1]:
            if b in a * t:
                return t
        return -1
