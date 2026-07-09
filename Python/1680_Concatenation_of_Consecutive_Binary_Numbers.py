# Author: Kaustav Ghosh
# Problem: Concatenation of Consecutive Binary Numbers
# Approach: Fold each number in by shifting the accumulator left by that number's bit length and OR-ing it in, taking the modulus each step

class Solution(object):
    def concatenatedBinary(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        result = 0
        for i in range(1, n + 1):
            result = ((result << i.bit_length()) | i) % MOD
        return result
