# Author: Kaustav Ghosh
# Problem: Sort Array by Increasing Frequency
# Approach: Both orderings are expressible as a single sort key, so no custom comparator or two-pass arrangement is needed: tally the values once, then sort by frequency ascending with the value itself negated as the tie-break, which produces decreasing value among equally frequent numbers. Sorting the original array rather than the distinct values means each value automatically appears as many times as it occurred.

from collections import Counter


class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        times = Counter(nums)
        return sorted(nums, key=lambda value: (times[value], -value))
