# Author: Kaustav Ghosh
# Problem: 1533 - Find the Index of the Large Integer (Premium)
# Approach: Binary search using ArrayReader API comparisons

# This is an interactive problem using an ArrayReader interface.
# class ArrayReader:
#     def compareSub(self, l, r, x, y) -> int: ...
#     def length(self) -> int: ...

class Solution(object):
    def getIndex(self, reader):
        """
        :type reader: ArrayReader
        :rtype: int
        """
        lo, hi = 0, reader.length() - 1
        while lo < hi:
            mid = (hi - lo) // 2
            l_end = lo + mid
            r_start = hi - mid
            res = reader.compareSub(lo, l_end, r_start, hi)
            if res == 1:
                hi = l_end
            elif res == -1:
                lo = r_start
            else:
                # equal, large int is in the middle (odd length)
                lo = hi = lo + mid + 1
        return lo
