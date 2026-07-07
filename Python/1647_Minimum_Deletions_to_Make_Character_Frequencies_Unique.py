# Author: Kaustav Ghosh
# Problem: Minimum Deletions to Make Character Frequencies Unique
# Approach: For each character frequency, keep lowering it until it hits an unused value (or 0), counting each decrement as a deletion

from collections import Counter

class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        used = set()
        deletions = 0
        for freq in Counter(s).values():
            while freq > 0 and freq in used:
                freq -= 1
                deletions += 1
            used.add(freq)
        return deletions
