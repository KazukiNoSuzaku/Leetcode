# Find maximum overlapping 1s after translating one binary matrix onto another.

# Author: Kaustav Ghosh

from collections import Counter

class Solution(object):
    def largestOverlap(self, img1, img2):
        n = len(img1)
        ones1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c]]
        ones2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c]]
        count = Counter((r1-r2, c1-c2) for r1,c1 in ones1 for r2,c2 in ones2)
        return max(count.values()) if count else 0
