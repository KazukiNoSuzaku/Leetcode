# Author: Kaustav Ghosh
# Problem: 1551 - Minimum Operations to Make Array Equal
# Approach: Sum of (n - 2*i - 1) for i < n//2; formula: n//2 * n//2

class Solution(object):
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        return (n // 2) * (n // 2)
