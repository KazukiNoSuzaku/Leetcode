# Author: Kaustav Ghosh
# Problem: Count Good Meals
# Approach: Checking every pair would be quadratic, but the target is not an arbitrary number: the sum has to be a power of two, and since each value is at most 2^20 the sum cannot exceed 2^21, leaving only twenty-two candidate totals. So the array is walked once while a tally of everything already seen is kept, and each item asks, for each candidate total, how many earlier items complete it. Counting only against earlier items is what makes every unordered pair counted exactly once, with no halving or self-pairing correction needed.

from collections import Counter


class Solution(object):
    def countPairs(self, deliciousness):
        """
        :type deliciousness: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        seen = Counter()
        pairs = 0
        powers = [1 << bit for bit in range(22)]
        for value in deliciousness:
            for total in powers:
                partner = total - value
                if partner in seen:
                    pairs += seen[partner]
            seen[value] += 1
        return pairs % MOD
