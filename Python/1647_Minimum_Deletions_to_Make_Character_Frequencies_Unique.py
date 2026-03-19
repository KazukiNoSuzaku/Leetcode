# Author: Kaustav Ghosh
# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

from collections import Counter

class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = sorted(Counter(s).values(), reverse=True)
        deletions = 0
        used = set()
        for f in freq:
            while f > 0 and f in used:
                f -= 1
                deletions += 1
            used.add(f)
        return deletions
