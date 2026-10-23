# Author: Kaustav Ghosh
# Problem: Concatenation of Consecutive Binary Numbers
# Approach: Building the full binary string would run to hundreds of thousands of digits and then need converting, so instead the number is grown in place: appending the binary form of i to what is already there means shifting the running value left by however many bits i occupies and adding i. Shifting by that bit length is a multiplication by a power of two, which stays valid under the modulus, so each step is a constant amount of arithmetic and the whole thing is one pass.

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
