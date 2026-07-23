# Author: Kaustav Ghosh
# Problem: Number of Different Subsequences GCDs
# Approach: A value g is achievable iff the gcd of all present multiples of g equals g. Test every candidate g by folding its multiples' gcd, which is near-linear over the harmonic series

from math import gcd

class Solution(object):
    def countDifferentSubsequenceGCDs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        present = set(nums)
        largest = max(nums)
        count = 0

        for g in range(1, largest + 1):
            current = 0
            for multiple in range(g, largest + 1, g):
                if multiple in present:
                    current = gcd(current, multiple)
                    if current == g:  # already reduced to g, no need to continue
                        break
            if current == g:
                count += 1
        return count
