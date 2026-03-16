# Author: Kaustav Ghosh
# Problem: Find the Longest Substring Containing Vowels in Even Counts
# Approach: Bitmask prefix XOR for vowel parity

class Solution(object):
    def findTheLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        vowels = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        first = {0: -1}
        mask = 0
        result = 0
        for i, c in enumerate(s):
            if c in vowels:
                mask ^= 1 << vowels[c]
            if mask in first:
                result = max(result, i - first[mask])
            else:
                first[mask] = i
        return result
