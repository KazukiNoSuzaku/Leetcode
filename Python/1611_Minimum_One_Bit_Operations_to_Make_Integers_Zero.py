# Author: Kaustav Ghosh
# Problem: Minimum One Bit Operations to Make Integers Zero
# Approach: The two permitted moves are exactly the moves that step between consecutive Gray codes, so the reachable states form a single path through all numbers and the distance from n to zero is just n's position along it. That position is the inverse Gray code of n, obtained by folding n with every one of its right shifts under exclusive or, which costs one pass over the bits rather than any search.

class Solution(object):
    def minimumOneBitOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        steps = 0
        while n:
            steps ^= n
            n >>= 1
        return steps
