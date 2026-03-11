# Minimum flips to make binary string monotone increasing.

# Author: Kaustav Ghosh

class Solution(object):
    def minFlipsMonoIncr(self, s):
        ones = flips = 0
        for c in s:
            if c == '1': ones += 1
            else: flips = min(flips + 1, ones)
        return flips
