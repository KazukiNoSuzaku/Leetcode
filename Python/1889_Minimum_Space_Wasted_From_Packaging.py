# Author: Kaustav Ghosh
# Problem: Minimum Space Wasted From Packaging
# Approach: Sort packages and each supplier's boxes. For a supplier, binary-search how many packages each box size can hold and use prefix sums to total the box capacity used; waste is that total minus the sum of package sizes. Take the best supplier

from bisect import bisect_right

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
        total_size = prefix[n]

        best = float('inf')
        for supplier in boxes:
            supplier.sort()
            if supplier[-1] < packages[-1]:
                continue  # largest box can't fit the largest package

            used = 0  # total box capacity consumed
            start = 0  # packages [0, start) already boxed
            for box in supplier:
                end = bisect_right(packages, box, start)  # packages that fit in this box size
                used += box * (end - start)
                start = end
            best = min(best, used - total_size)

        return best % MOD if best != float('inf') else -1
