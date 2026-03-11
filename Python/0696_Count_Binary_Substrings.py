# Count substrings with equal consecutive 0s and 1s.

# Author: Kaustav Ghosh

class Solution(object):
    def countBinarySubstrings(self, s):
        prev, cur, res = 0, 1, 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cur += 1
            else:
                res += min(prev, cur)
                prev, cur = cur, 1
        return res + min(prev, cur)
