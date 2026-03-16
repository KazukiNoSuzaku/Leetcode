# Author: Kaustav Ghosh
# Problem: Longest Happy Prefix
# Approach: KMP failure function to find longest prefix that is also suffix

class Solution(object):
    def longestPrefix(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        lps = [0] * n
        length = 0
        i = 1
        while i < n:
            if s[i] == s[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return s[:lps[-1]]
