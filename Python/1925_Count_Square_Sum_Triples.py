# Author: Kaustav Ghosh
# Problem: Count Square Sum Triples
# Approach: Enumerate ordered pairs (a, b); the triple is valid when a^2 + b^2 is a perfect square whose root c is at most n. Each valid pair contributes one ordered triple

import math

class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                s = a * a + b * b
                c = int(math.isqrt(s))
                if c <= n and c * c == s:
                    count += 1
        return count
