# Author: Kaustav Ghosh
# Problem: Check if All the Integers in a Range Are Covered
# Approach: Both the ranges and the interval in question live within one to fifty, so the covered values can simply be collected into a set, one range at a time, and the question becomes whether the set contains every value from left to right. That sidesteps sorting or merging the ranges, and overlapping ranges need no special handling because a set absorbs the repeats.

class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        covered = set()
        for start, end in ranges:
            covered.update(range(start, end + 1))
        return all(value in covered for value in range(left, right + 1))
