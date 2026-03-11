# Given an array of strings strs, return the length of the longest uncommon subsequence
# between them. Return -1 if it doesn't exist.

# Author: Kaustav Ghosh

class Solution(object):
    def findLUSlength(self, strs):
        def is_subseq(s, t):
            it = iter(t)
            return all(c in it for c in s)
        res = -1
        for i, s in enumerate(strs):
            if all(not is_subseq(s, strs[j]) for j in range(len(strs)) if i != j):
                res = max(res, len(s))
        return res
