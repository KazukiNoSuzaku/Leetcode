# Author: Kaustav Ghosh
# Problem: Minimum Number of Operations to Reinitialize a Permutation
# Approach: Track where index 1 travels - each operation sends position i to 2i mod (n-1). Count steps until it returns to 1, which is the whole array's period

class Solution(object):
    def reinitializePermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        operations = 0
        pos = 1
        while True:
            pos = pos * 2 % (n - 1)
            operations += 1
            if pos == 1:
                return operations
