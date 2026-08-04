# Author: Kaustav Ghosh
# Problem: Count Good Numbers
# Approach: Even indices (there are ceil(n/2)) take one of 5 even digits; odd indices (floor(n/2)) take one of 4 prime digits. The count is 5^ceil(n/2) * 4^floor(n/2) mod 1e9+7, using fast exponentiation

class Solution(object):
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        even_positions = (n + 1) // 2
        odd_positions = n // 2
        return pow(5, even_positions, MOD) * pow(4, odd_positions, MOD) % MOD
