# Author: Kaustav Ghosh
# https://leetcode.com/problems/minimum-space-wasted-from-packaging/

import bisect

class Solution(object):
    def minWastedSpace(self, packages, boxes):
        """
        :type packages: List[int]
        :type boxes: List[List[int]]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        packages.sort()
        n = len(packages)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + packages[i]
        total = prefix[n]
        best = float('inf')
        for supplier in boxes:
            supplier.sort()
            if supplier[-1] < packages[-1]:
                continue
            waste = 0
            prev = 0
            for box in supplier:
                idx = bisect.bisect_right(packages, box)
                count = idx - prev
                waste += box * count - (prefix[idx] - prefix[prev])
                prev = idx
            best = min(best, waste)
        return best % MOD if best < float('inf') else -1
