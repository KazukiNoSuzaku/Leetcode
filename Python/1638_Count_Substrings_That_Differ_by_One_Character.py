# Author: Kaustav Ghosh
# https://leetcode.com/problems/count-substrings-that-differ-by-one-character/

class Solution(object):
    def countSubstrings(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        result = 0
        for i in range(len(s)):
            for j in range(len(t)):
                diff = 0
                k = 0
                while i + k < len(s) and j + k < len(t):
                    if s[i + k] != t[j + k]:
                        diff += 1
                    if diff == 1:
                        result += 1
                    elif diff > 1:
                        break
                    k += 1
        return result
