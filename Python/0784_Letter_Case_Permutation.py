# Generate all letter case permutations of a string.

# Author: Kaustav Ghosh

class Solution(object):
    def letterCasePermutation(self, s):
        res = ['']
        for c in s:
            if c.isdigit():
                res = [r + c for r in res]
            else:
                res = [r + x for r in res for x in [c.lower(), c.upper()]]
        return res
