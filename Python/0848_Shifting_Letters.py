# Apply cumulative shifts to a string where each character shifts by suffix sum.

# Author: Kaustav Ghosh

class Solution(object):
    def shiftingLetters(self, s, shifts):
        total = sum(shifts) % 26
        res = []
        for i, c in enumerate(s):
            res.append(chr((ord(c) - ord('a') + total) % 26 + ord('a')))
            total = (total - shifts[i]) % 26
        return ''.join(res)
