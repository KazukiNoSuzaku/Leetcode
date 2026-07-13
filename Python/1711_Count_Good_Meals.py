# Author: Kaustav Ghosh
# Problem: Count Good Meals
# Approach: Sums are bounded by 2^21, so for each item check every power of two and look up the needed complement among items already seen

from collections import Counter

class Solution(object):
    def countPairs(self, deliciousness):
        """
        :type deliciousness: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        powers = [1 << i for i in range(22)]
        seen = Counter()
        total = 0
        for d in deliciousness:
            for p in powers:
                total += seen[p - d]
            seen[d] += 1
        return total % MOD
