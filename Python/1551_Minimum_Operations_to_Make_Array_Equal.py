# Author: Kaustav Ghosh
# Problem: Minimum Operations to Make Array Equal
# Approach: Target is the mean n; total moves equal the sum of gaps on one side, which simplifies to n*n//4

class Solution(object):
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        return (n * n) // 4
