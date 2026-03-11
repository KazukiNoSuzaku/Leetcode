# Given a string s, find the first non-repeating character in it and return its index.
# If it does not exist, return -1.

# Author: Kaustav Ghosh

from collections import Counter

class Solution(object):
    def firstUniqChar(self, s):
        count = Counter(s)
        for i, ch in enumerate(s):
            if count[ch] == 1:
                return i
        return -1
