# Author: Kaustav Ghosh
# Problem: Max Number of K-Sum Pairs
# Approach: Pairs are formed solely by value, so only the counts matter and every value has exactly one possible partner, which means there is no choice to optimise and the greedy pairing is forced: for each value, pair it with its complement as many times as both supply. Counting the tally once and walking it halves the pairs naturally because each unordered pair is reachable from either side, and the case where a value is its own partner is separate, taking half of that value's own count.

from collections import Counter


class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        tally = Counter(nums)
        pairs = 0
        for value, times in tally.items():
            partner = k - value
            if partner < value:
                continue
            if partner == value:
                pairs += times // 2
            else:
                pairs += min(times, tally.get(partner, 0))
        return pairs
