# Author: Kaustav Ghosh
# Problem: Largest Merge Of Two Strings
# Approach: At each step take from whichever remaining suffix is lexicographically larger; comparing whole suffixes (not just the next char) settles ties correctly

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
