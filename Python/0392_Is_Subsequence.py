# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# Author: Kaustav Ghosh

class Solution(object):
    def isSubsequence(self, s, t):
        i = 0
        for ch in t:
            if i < len(s) and ch == s[i]:
                i += 1
        return i == len(s)
