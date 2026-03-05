# Given a pattern and a string s, find if s follows the same pattern.
# Here follow means a full match, such that there is a bijection between a letter in pattern
# and a non-empty word in s.

# Example 1:
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true

# Example 2:
# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false

# Constraints:
# 1 <= pattern.length <= 300
# pattern contains only lower-case English letters.
# 1 <= s.length <= 3000
# s contains only lowercase English letters and spaces.
# s does not contain any leading or trailing spaces.
# All the words in s are separated by a single space.

# Author: Kaustav Ghosh

class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()
        if len(pattern) != len(words):
            return False
        p2w, w2p = {}, {}
        for p, w in zip(pattern, words):
            if p in p2w and p2w[p] != w:
                return False
            if w in w2p and w2p[w] != p:
                return False
            p2w[p] = w
            w2p[w] = p
        return True
