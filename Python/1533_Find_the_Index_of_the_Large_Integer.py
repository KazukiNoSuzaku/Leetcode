# Author: Kaustav Ghosh
# Problem: Find the Index of the Large Integer (Premium, Interactive)
# Approach: Binary search using compareSub; for odd-length range compare equal halves, for even check middle element

class Solution(object):
    def getIndex(self, reader):
        """
        :type reader: ArrayReader
        :rtype: int
        """
        lo, hi = 0, reader.length() - 1
        while lo < hi:
            mid = (lo + hi) // 2
            left_len = mid - lo + 1
            right_len = hi - mid
            if left_len == right_len:
                cmp = reader.compareSub(lo, mid, mid + 1, hi)
                if cmp == 1:
                    hi = mid
                else:
                    lo = mid + 1
            else:
                # left_len = right_len + 1; compare [lo, mid-1] vs [mid+1, hi]
                cmp = reader.compareSub(lo, mid - 1, mid + 1, hi)
                if cmp == 0:
                    return mid
                elif cmp == 1:
                    hi = mid - 1
                else:
                    lo = mid + 1
        return lo
