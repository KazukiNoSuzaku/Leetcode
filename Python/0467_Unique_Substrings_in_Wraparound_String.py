# We define the string base to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz".
# Given a string s, return the number of unique non-empty substrings of s are present in base.

# Author: Kaustav Ghosh

class Solution(object):
    def findSubstringInWraproundString(self, s):
        dp = {}
        cur_len = 0
        for i, ch in enumerate(s):
            if i > 0 and (ord(ch) - ord(s[i-1])) % 26 == 1:
                cur_len += 1
            else:
                cur_len = 1
            dp[ch] = max(dp.get(ch, 0), cur_len)
        return sum(dp.values())
