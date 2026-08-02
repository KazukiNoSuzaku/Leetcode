# Author: Kaustav Ghosh
# Problem: Redistribute Characters to Make All Strings Equal
# Approach: Characters move freely between words, so equality is possible iff every character total divides evenly across the words

from collections import Counter

class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        counts = Counter()
        for word in words:
            counts.update(word)
        n = len(words)
        return all(total % n == 0 for total in counts.values())
