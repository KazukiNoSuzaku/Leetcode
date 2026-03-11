# Given an integer array of even length, return true if it is possible to
# reorder such that arr[2i+1] = 2 * arr[2i] for every i.

# Author: Kaustav Ghosh

from collections import Counter

class Solution(object):
    def canReorderDoubled(self, arr):
        count = Counter(arr)
        for x in sorted(count, key=abs):
            if count[x] > count[2 * x]:
                return False
            count[2 * x] -= count[x]
        return True
