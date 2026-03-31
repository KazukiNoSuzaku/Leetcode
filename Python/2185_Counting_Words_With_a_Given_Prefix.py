# Author: Kaustav Ghosh
# 2185. Counting Words With a Given Prefix
# https://leetcode.com/problems/counting-words-with-a-given-prefix/
# Difficulty: Easy
#
# Approach: Filter words list using str.startswith() and return the count.
# Time: O(n * m) where n = len(words), m = len(pref), Space: O(1)

class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        return sum(1 for word in words if word.startswith(pref))
