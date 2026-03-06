# Given two strings s and t, return true if they are both one edit distance apart,
# otherwise return false.
# An edit is inserting a character, deleting a character, or replacing a character.

# Example 1:
# Input: s = "ab", t = "acb"
# Output: true

# Example 2:
# Input: s = "", t = ""
# Output: false

# Constraints:
# 0 <= s.length <= 10^4
# 0 <= t.length <= 10^4

# Author: Kaustav Ghosh

class Solution(object):
    def isOneEditDistance(self, s, t):
        m, n = len(s), len(t)
        if abs(m - n) > 1:
            return False
        if m > n:
            return self.isOneEditDistance(t, s)
        for i in range(m):
            if s[i] != t[i]:
                if m == n:
                    return s[i+1:] == t[i+1:]
                else:
                    return s[i:] == t[i+1:]
        return m + 1 == n
