# Author: Kaustav Ghosh
# Problem: Remove Letter To Equalize Frequency
# Approach: Exactly one letter must go, and only its own count changes, so try removing one occurrence of each distinct letter in turn and check whether the remaining non-zero counts are all equal

from collections import Counter


class Solution(object):
    def equalFrequency(self, word):
        """
        :type word: str
        :rtype: bool
        """
        count = Counter(word)
        for ch in count:
            count[ch] -= 1
            remaining = {c for c in count.values() if c}
            count[ch] += 1
            if len(remaining) == 1:
                return True
        return False
