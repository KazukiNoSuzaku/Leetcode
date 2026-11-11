# Author: Kaustav Ghosh
# Problem: Minimum Space Wasted From Packaging
# Approach: Only one supplier is chosen, so each is costed independently and the cheapest wins. Within a supplier, sorting both the packages and the box sizes means each box size serves a contiguous block of packages, namely those too large for the previous size and no larger than this one, and the waste for that block is the box size times the block length minus the packages' own total. A prefix sum supplies that total and a binary search finds where each block ends, so a supplier costs only its own box count in lookups rather than a pass over every package. A supplier whose largest box cannot hold the largest package is discarded outright, and the modulus is applied once at the end so the comparison between suppliers stays exact.

class Solution(object):
    def minWastedSpace(self, packages, boxes):
        """
        :type packages: List[int]
        :type boxes: List[List[int]]
        :rtype: int
        """
        from bisect import bisect_right
        from itertools import accumulate

        MOD = 10 ** 9 + 7
        ordered = sorted(packages)
        prefix = [0] + list(accumulate(ordered))
        total = prefix[-1]
        largest = ordered[-1]

        best = None
        for supplier in boxes:
            sizes = sorted(supplier)
            if sizes[-1] < largest:
                continue
            used = 0
            placed = 0
            for size in sizes:
                reach = bisect_right(ordered, size)
                if reach > placed:
                    used += size * (reach - placed)
                    placed = reach
            if best is None or used < best:
                best = used

        return -1 if best is None else (best - total) % MOD
