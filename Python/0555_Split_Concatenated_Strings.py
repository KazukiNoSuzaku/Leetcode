# Given a list of strings, you could concatenate these strings together into a loop.
# Among all the possible loops, find the lexicographically biggest string after cutting the loop.

# Author: Kaustav Ghosh

class Solution(object):
    def splitLoopedString(self, strs):
        strs = [max(s, s[::-1]) for s in strs]
        res = ''
        for i, s in enumerate(strs):
            rest = ''.join(strs[i+1:] + strs[:i])
            for k in range(len(s)):
                res = max(res, s[k:] + rest + s[:k])
                t = s[::-1]
                res = max(res, t[k:] + rest + t[:k])
        return res
