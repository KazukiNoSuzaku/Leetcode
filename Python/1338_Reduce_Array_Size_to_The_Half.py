# Remove a set of integers to reduce the array size by at least half.
# Return the minimum size of the set.

# Author: Kaustav Ghosh

from collections import Counter

class Solution(object):
    def minSetSize(self, arr):
        counts = sorted(Counter(arr).values(), reverse=True)
        removed = target = len(arr) // 2
        for i, c in enumerate(counts):
            removed -= c
            if removed <= 0:
                return i + 1
