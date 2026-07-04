# Author: Kaustav Ghosh
# Problem: Number of Sets of K Non-Overlapping Line Segments
# Approach: Endpoints may touch, so a stars-and-bars argument collapses the count to a single binomial C(n+k-1, 2k)

from math import comb

class Solution(object):
    def numberOfSets(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        return comb(n + k - 1, 2 * k) % MOD
