# Author: Kaustav Ghosh
# https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/

from collections import Counter

class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        n = len(words)
        count = Counter()
        for w in words:
            count.update(w)
        return all(v % n == 0 for v in count.values())
