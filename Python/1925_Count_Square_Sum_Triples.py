# Author: Kaustav Ghosh
# Problem: Count Square Sum Triples
# Approach: With n capped at two hundred and fifty, every ordered pair of legs can be tried directly, which is only sixty thousand combinations. For a pair the third side is forced, so the test is whether the sum of the two squares is itself a square of some value within n, and holding those squares in a set answers that by lookup rather than by a square root, which keeps everything in integers with no rounding to worry about. Ordered pairs are counted, which already matches the problem's definition of a triple.

class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        squares = {value * value for value in range(1, n + 1)}
        return sum(1 for a in range(1, n + 1) for b in range(1, n + 1)
                   if a * a + b * b in squares)
