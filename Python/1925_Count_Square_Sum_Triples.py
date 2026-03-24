# Author: Kaustav Ghosh
# https://leetcode.com/problems/count-square-sum-triples/

class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                c_sq = a * a + b * b
                c = int(c_sq ** 0.5)
                if c <= n and c * c == c_sq:
                    count += 1
        return count
