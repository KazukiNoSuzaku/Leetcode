# Author: Kaustav Ghosh
# Problem: 2255. Count Prefixes of a Given String
# URL: https://leetcode.com/problems/count-prefixes-of-a-given-string/
# Difficulty: Easy
#
# Approach:
# Count how many strings in words are a prefix of s using startswith.

class Solution(object):
    def countPrefixes(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: int
        """
        return sum(1 for w in words if s.startswith(w))
