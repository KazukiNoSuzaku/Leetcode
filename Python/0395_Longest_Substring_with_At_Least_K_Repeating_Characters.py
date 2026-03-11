# Given a string s and an integer k, return the length of the longest substring of s
# such that the frequency of each character in this substring is greater than or equal to k.

# Author: Kaustav Ghosh

from collections import Counter

class Solution(object):
    def longestSubstring(self, s, k):
        if len(s) < k:
            return 0
        count = Counter(s)
        for ch in count:
            if count[ch] < k:
                return max(self.longestSubstring(part, k) for part in s.split(ch))
        return len(s)
