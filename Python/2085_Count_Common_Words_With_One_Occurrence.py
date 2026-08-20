# Author: Kaustav Ghosh
# Problem: Count Common Words With One Occurrence
# Approach: Count occurrences in each list; a word qualifies if it appears exactly once in both

from collections import Counter

class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        c1 = Counter(words1)
        c2 = Counter(words2)
        return sum(1 for w, c in c1.items() if c == 1 and c2.get(w) == 1)
