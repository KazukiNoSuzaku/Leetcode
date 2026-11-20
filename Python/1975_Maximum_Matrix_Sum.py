# Author: Kaustav Ghosh
# Problem: Maximum Matrix Sum
# Approach: One operation flips the signs of two adjacent cells, which changes the number of negative entries by exactly two or leaves it alone, so the parity of that count can never change. Within a fixed parity everything else is reachable: the grid is connected, so a negative sign can be walked along a path to be cancelled against any other negative, and a lone leftover negative can be walked to sit on whichever cell we choose. So the best achievable sum is the total of the absolute values when the count of negatives is even, and that total reduced by twice the smallest absolute value when it is odd, since one entry must stay negative and it should be the cheapest one. Zeros make the count effectively even because a zero can absorb a sign at no cost, which falls out of taking the smallest absolute value. One pass over the grid gives O(n^2).

class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        total = 0
        negatives = 0
        smallest = None
        for row in matrix:
            for value in row:
                size = abs(value)
                total += size
                if value < 0:
                    negatives += 1
                if smallest is None or size < smallest:
                    smallest = size
        if negatives % 2 == 0:
            return total
        return total - 2 * smallest
