# Find shortest word that contains all letters from a license plate.

# Author: Kaustav Ghosh

from collections import Counter

class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        plate = Counter(c.lower() for c in licensePlate if c.isalpha())
        res = None
        for word in words:
            wc = Counter(word)
            if all(wc[c] >= plate[c] for c in plate):
                if res is None or len(word) < len(res):
                    res = word
        return res
