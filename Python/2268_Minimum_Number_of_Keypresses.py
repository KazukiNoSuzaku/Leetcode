# Author: Kaustav Ghosh
# Problem: Minimum Number of Keypresses
# Approach: With 9 keys, the first letter on each key costs 1 press, the second 2, and so on. To minimize total presses assign the most frequent letters to the cheapest slots: sort letter frequencies descending, so the r-th most frequent (0-indexed) costs (r//9 + 1) presses per occurrence. Sum frequency times cost

from collections import Counter


class Solution(object):
    def minimumKeypresses(self, s):
        """
        :type s: str
        :rtype: int
        """
        freqs = sorted(Counter(s).values(), reverse=True)
        total = 0
        for r, f in enumerate(freqs):
            total += f * (r // 9 + 1)
        return total
