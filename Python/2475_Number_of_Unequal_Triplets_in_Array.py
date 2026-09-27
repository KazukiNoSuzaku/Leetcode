# Author: Kaustav Ghosh
# Problem: Number of Unequal Triplets in Array
# Approach: Only the values matter, not the positions, so group equal values. Taking each group as the middle of the triplet, it pairs with everything counted before it and everything left after it, which multiplies out to all triplets with three different values

from collections import Counter


class Solution(object):
    def unequalTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        before = 0
        n = len(nums)
        for count in Counter(nums).values():
            total += before * count * (n - before - count)
            before += count
        return total
