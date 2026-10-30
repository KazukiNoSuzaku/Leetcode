# Author: Kaustav Ghosh
# Problem: Largest Merge Of Two Strings
# Approach: At each step the choice is only which string to draw from, and the larger result comes from taking whichever remaining suffix is lexicographically greater; comparing the whole suffixes rather than just the leading characters is what settles ties correctly, since equal leading characters must be broken by what follows them. Once one string is exhausted the rest of the other is appended as it stands. Python's slice comparison performs the suffix comparison directly, which keeps the greedy rule visible at the cost of the comparison itself.

class Solution(object):
    def largestMerge(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged = []
        i = j = 0
        while i < len(word1) and j < len(word2):
            if word1[i:] > word2[j:]:
                merged.append(word1[i])
                i += 1
            else:
                merged.append(word2[j])
                j += 1
        merged.append(word1[i:])
        merged.append(word2[j:])
        return ''.join(merged)
