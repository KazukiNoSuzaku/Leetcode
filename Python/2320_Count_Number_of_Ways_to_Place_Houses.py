# Author: Kaustav Ghosh
# Problem: Count Number of Ways to Place Houses
# Approach: The two sides of the street are independent. On one side of n plots, the number of ways to place houses with no two adjacent follows a Fibonacci recurrence (each plot either empty or a house given the previous plot). Square that count (both sides) modulo 1e9+7

class Solution(object):
    def countHousePlacements(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        # ways[i] = arrangements on i plots with no two adjacent houses
        prev, cur = 1, 2  # ways[0]=1, ways[1]=2
        if n == 0:
            one_side = 1
        else:
            for _ in range(2, n + 1):
                prev, cur = cur, (prev + cur) % MOD
            one_side = cur if n >= 1 else 1
        return (one_side * one_side) % MOD
