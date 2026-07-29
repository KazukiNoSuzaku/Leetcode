# Author: Kaustav Ghosh
# Problem: Longer Contiguous Segments of Ones than Zeros
# Approach: Track the current run length as we scan, recording the longest run of each digit; the answer compares those two maxima

class Solution(object):
    def checkZeroOnes(self, s):
        """
        :type s: str
        :rtype: bool
        """
        best = {'0': 0, '1': 0}
        run = 0
        prev = ''
        for c in s:
            run = run + 1 if c == prev else 1
            prev = c
            best[c] = max(best[c], run)
        return best['1'] > best['0']
