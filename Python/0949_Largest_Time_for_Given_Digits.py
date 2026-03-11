# Find the largest valid time using all 4 given digits.

# Author: Kaustav Ghosh

from itertools import permutations

class Solution(object):
    def largestTimeFromDigits(self, arr):
        best = ''
        for p in permutations(arr):
            h = 10*p[0]+p[1]; m = 10*p[2]+p[3]
            t = '%02d:%02d' % (h, m)
            if h < 24 and m < 60 and t > best: best = t
        return best
