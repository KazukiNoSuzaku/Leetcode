# Author: Kaustav Ghosh
# Problem: Maximum Number of Vowels in a Substring of Given Length
# Approach: Sliding window counting vowels

class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = set('aeiou')
        count = sum(1 for c in s[:k] if c in vowels)
        best = count
        for i in range(k, len(s)):
            count += (s[i] in vowels) - (s[i - k] in vowels)
            best = max(best, count)
        return best
