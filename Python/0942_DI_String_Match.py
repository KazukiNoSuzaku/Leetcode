# Reconstruct permutation from DI string by assigning from smallest/largest ends.

# Author: Kaustav Ghosh

class Solution(object):
    def diStringMatch(self, s):
        lo, hi = 0, len(s)
        res = []
        for c in s:
            if c == 'I': res.append(lo); lo += 1
            else: res.append(hi); hi -= 1
        return res + [lo]
