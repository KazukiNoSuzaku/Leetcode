# Author: Kaustav Ghosh
# Problem: Number of Wonderful Substrings
# Approach: Track a 10-bit parity mask (letters a..j) of the prefix. A substring is wonderful iff the XOR of its two endpoint prefix masks has at most one set bit. For each prefix, count earlier prefixes with the same mask or a mask differing in exactly one of the 10 bits

from collections import defaultdict

class Solution(object):
    def wonderfulSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        count = defaultdict(int)
        count[0] = 1
        mask = 0
        total = 0
        for ch in word:
            mask ^= 1 << (ord(ch) - ord('a'))
            total += count[mask]                    # zero odd letters
            for b in range(10):                     # exactly one odd letter
                total += count[mask ^ (1 << b)]
            count[mask] += 1
        return total
