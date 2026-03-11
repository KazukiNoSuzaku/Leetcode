# Search for target in a sorted array of unknown size using an ArrayReader interface.

# Author: Kaustav Ghosh

class Solution(object):
    def search(self, reader, target):
        lo, hi = 0, 1
        while reader.get(hi) < target:
            lo = hi
            hi *= 2
        while lo <= hi:
            mid = (lo + hi) // 2
            val = reader.get(mid)
            if val == target: return mid
            elif val < target: lo = mid + 1
            else: hi = mid - 1
        return -1
