# Author: Kaustav Ghosh
# https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/

class Solution(object):
    def minFlips(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        # Double the string to simulate type-1 operation (rotation)
        s2 = s + s
        # Two target patterns: 010101... and 101010...
        diff0 = 0  # mismatches with pattern starting with '0'
        diff1 = 0  # mismatches with pattern starting with '1'
        res = n
        for i in range(len(s2)):
            if int(s2[i]) != i % 2:
                diff0 += 1
            else:
                diff1 += 1
            # Remove leftmost element when window exceeds n
            if i >= n:
                if int(s2[i - n]) != (i - n) % 2:
                    diff0 -= 1
                else:
                    diff1 -= 1
            if i >= n - 1:
                res = min(res, diff0, diff1)
        return res
