# Author: Kaustav Ghosh
# Problem: Longest Substring Of All Vowels in Order
# Approach: Map vowels to 0..4 and scan; extend the run while each char stays equal or steps to the next vowel, else restart. A run counts once all five distinct vowels appear

class Solution(object):
    def longestBeautifulSubstring(self, word):
        """
        :type word: str
        :rtype: int
        """
        idx = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        best = 0
        length = 0
        distinct = 0
        prev = -1

        for c in word:
            v = idx[c]
            if v == prev:
                length += 1
            elif v == prev + 1:
                length += 1
                distinct += 1
            else:
                length = 1
                distinct = 1
            prev = v
            if distinct == 5:
                best = max(best, length)
        return best
