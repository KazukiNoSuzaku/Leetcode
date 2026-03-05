# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

# Constraints:
# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.

# Author: Kaustav Ghosh

class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        count = [0] * 26
        for cs, ct in zip(s, t):
            count[ord(cs) - ord('a')] += 1
            count[ord(ct) - ord('a')] -= 1
        return all(c == 0 for c in count)
