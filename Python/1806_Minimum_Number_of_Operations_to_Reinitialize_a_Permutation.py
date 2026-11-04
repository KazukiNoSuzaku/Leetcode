# Author: Kaustav Ghosh
# Problem: Minimum Number of Operations to Reinitialize a Permutation
# Approach: Written out, the operation sends the value sitting at index i to index 2i taken modulo n - 1, while the first and last indices never move. The array is therefore back to the identity exactly when that doubling map returns every index home, and since each index i travels as i times a power of two, the step count for index 1 is already a multiple of every other index's. Following index 1 alone until it returns thus gives the answer, in a handful of multiplications rather than by rebuilding the whole array over and over.

class Solution(object):
    def reinitializePermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        modulus = n - 1
        position = 1
        operations = 0
        while True:
            position = position * 2 % modulus
            operations += 1
            if position == 1:
                return operations
