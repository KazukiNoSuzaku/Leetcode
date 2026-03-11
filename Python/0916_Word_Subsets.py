# Find words in words1 that are supersets of all words in words2.

# Author: Kaustav Ghosh

from collections import Counter

class Solution(object):
    def wordSubsets(self, words1, words2):
        max_need = Counter()
        for w in words2:
            for c, cnt in Counter(w).items():
                max_need[c] = max(max_need[c], cnt)
        return [w for w in words1 if not (max_need - Counter(w))]
