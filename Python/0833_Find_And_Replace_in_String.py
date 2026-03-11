# Apply replacements to a string if source matches at given index.

# Author: Kaustav Ghosh

class Solution(object):
    def findReplaceString(self, s, indices, sources, targets):
        res = list(s)
        for i, src, tgt in zip(indices, sources, targets):
            if s[i:i+len(src)] == src:
                res[i] = tgt
                for j in range(i+1, i+len(src)):
                    res[j] = ''
        return ''.join(res)
