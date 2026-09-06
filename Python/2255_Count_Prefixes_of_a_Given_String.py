# Author: Kaustav Ghosh
# Problem: Count Prefixes of a Given String
# Approach: Count how many words are prefixes of s using string startswith

class Solution(object):
    def countPrefixes(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: int
        """
        return sum(1 for w in words if s.startswith(w))
