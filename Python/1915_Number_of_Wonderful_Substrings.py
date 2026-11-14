# Author: Kaustav Ghosh
# Problem: Number of Wonderful Substrings
# Approach: Only the parity of each letter's count matters, and there are ten possible letters, so a prefix is summarised by a ten-bit mask of those parities. A substring's own parity mask is the XOR of the masks at its two ends, so it is wonderful exactly when that XOR is zero, meaning every letter appears an even number of times, or has a single bit set, meaning exactly one letter is odd. Keeping a tally of how often each mask has been seen turns each new prefix into eleven lookups, one for the equal mask and one per letter, which counts every wonderful substring ending there without examining any of them.

class Solution(object):
    def wonderfulSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        seen = [0] * 1024
        seen[0] = 1
        mask = 0
        total = 0
        for letter in word:
            mask ^= 1 << (ord(letter) - 97)
            total += seen[mask]
            for bit in range(10):
                total += seen[mask ^ (1 << bit)]
            seen[mask] += 1
        return total
