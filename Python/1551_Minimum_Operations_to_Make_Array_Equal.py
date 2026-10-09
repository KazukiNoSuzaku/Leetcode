# Author: Kaustav Ghosh
# Problem: Minimum Operations to Make Array Equal
# Approach: The array holds the odd numbers 1, 3, 5, ... so its average is n and every operation moves one unit from a value above the average to one below. The work is therefore the total shortfall of the lower half, which sums to n * n / 4 under integer division

class Solution(object):
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        return n * n // 4
