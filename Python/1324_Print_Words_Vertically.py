# Print each column of words vertically, trimming trailing spaces.

# Author: Kaustav Ghosh

class Solution(object):
    def printVertically(self, s):
        words = s.split()
        max_len = max(len(w) for w in words)
        res = []
        for i in range(max_len):
            col = ''.join(w[i] if i < len(w) else ' ' for w in words)
            res.append(col.rstrip())
        return res
