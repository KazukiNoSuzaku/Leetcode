# Author: Kaustav Ghosh
# Problem: Minimum Number of Operations to Make Array Continuous
# Approach: A continuous array of a given length is determined entirely by its smallest element, holds every value in a window of that length, and has no duplicates, so the elements worth keeping are exactly a set of distinct values all falling inside one such window. Minimising the replacements therefore means maximising how many distinct values fit in a window of that width, which a two-pointer sweep over the sorted distinct values finds in one pass: the right end advances through the values while the left end is dragged forward whenever the window grows too wide. Everything outside the best window gets rewritten, so the answer is the length minus that count.

class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = len(nums)
        distinct = sorted(set(nums))
        best = 0
        left = 0
        for right, value in enumerate(distinct):
            while value - distinct[left] > total - 1:
                left += 1
            if right - left + 1 > best:
                best = right - left + 1
        return total - best
