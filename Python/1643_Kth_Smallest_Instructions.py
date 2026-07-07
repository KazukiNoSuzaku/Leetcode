# Author: Kaustav Ghosh
# Problem: Kth Smallest Instructions
# Approach: Build the path greedily; placing 'H' first covers C(remaining_H-1+V, V) paths, so take 'H' if k fits there, otherwise skip them by taking 'V'

from math import comb

class Solution(object):
    def kthSmallestPath(self, destination, k):
        """
        :type destination: List[int]
        :type k: int
        :rtype: str
        """
        v, h = destination  # V (down) moves = row, H (right) moves = col
        result = []
        for _ in range(v + h):
            if h > 0:
                # Number of paths that start with H from here
                with_h = comb(h - 1 + v, v)
                if k <= with_h:
                    result.append('H')
                    h -= 1
                else:
                    result.append('V')
                    v -= 1
                    k -= with_h
            else:
                result.append('V')
                v -= 1
        return ''.join(result)
