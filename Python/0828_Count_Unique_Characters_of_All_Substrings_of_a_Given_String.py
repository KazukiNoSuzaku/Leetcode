# Count sum of unique characters across all substrings.

# Author: Kaustav Ghosh

from collections import defaultdict

class Solution(object):
    def uniqueLetterString(self, s):
        index = defaultdict(list)
        for i, c in enumerate(s):
            index[c].append(i)
        res = 0
        for positions in index.values():
            positions = [-1] + positions + [len(s)]
            for i in range(1, len(positions) - 1):
                res += (positions[i] - positions[i-1]) * (positions[i+1] - positions[i])
        return res
