# Check if any permutation of digits of n forms a power of 2.

# Author: Kaustav Ghosh

from collections import Counter

class Solution(object):
    def reorderedPowerOf2(self, n):
        c = Counter(str(n))
        return any(Counter(str(1 << i)) == c for i in range(31))
