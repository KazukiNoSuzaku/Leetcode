# Author: Kaustav Ghosh
# Problem: Sum of Beauty of All Substrings
# Approach: For each start, extend the substring one char at a time, maintaining letter counts so each step's beauty (max freq - min nonzero freq) is cheap to add

from collections import Counter

class Solution(object):
    def beautySum(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        for i in range(len(s)):
            counts = Counter()
            for j in range(i, len(s)):
                counts[s[j]] += 1
                values = counts.values()
                total += max(values) - min(values)
        return total
