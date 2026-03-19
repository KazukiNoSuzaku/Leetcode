# Author: Kaustav Ghosh
# https://leetcode.com/problems/kth-smallest-instructions/

from math import comb

class Solution(object):
    def kthSmallestPath(self, destination, k):
        """
        :type destination: List[int]
        :type k: int
        :rtype: str
        """
        v, h = destination  # vertical (down), horizontal (right)
        result = []
        for _ in range(h + v):
            if h > 0:
                # Number of paths if we choose 'H' here
                count = comb(h - 1 + v, v)
                if k <= count:
                    result.append('H')
                    h -= 1
                else:
                    result.append('V')
                    k -= count
                    v -= 1
            else:
                result.append('V')
                v -= 1
        return ''.join(result)
