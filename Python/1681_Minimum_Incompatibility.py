# Author: Kaustav Ghosh
# Problem: Minimum Incompatibility
# Approach: With at most sixteen numbers the set of already-used positions fits in a bitmask, so the partition is built one complete subset at a time and the cost of each subset is charged as it is formed. The trick that keeps this cheap is always forcing the lowest unused position into the subset being built: every partition assigns that element to exactly one subset, so considering only subsets containing it loses nothing while cutting the branching enormously, and it also removes the duplicate work of reaching the same partition through different subset orderings. Sorting the numbers first means a subset's incompatibility is just its last chosen value minus its first. A value occurring more often than there are subsets cannot be placed at all, which is detected up front.

from collections import Counter
from itertools import combinations


class Solution(object):
    def minimumIncompatibility(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        size = n // k
        if max(Counter(nums).values()) > k:
            return -1

        ordered = sorted(nums)
        INF = float('inf')
        full = (1 << n) - 1
        best = [INF] * (full + 1)
        best[0] = 0

        for mask in range(full + 1):
            if best[mask] == INF:
                continue
            free = [i for i in range(n) if not (mask >> i) & 1]
            if not free:
                continue
            anchor, rest = free[0], free[1:]
            for others in combinations(rest, size - 1):
                group = (anchor,) + others
                values = [ordered[i] for i in group]
                if len(set(values)) != size:
                    continue
                reached = mask
                for i in group:
                    reached |= 1 << i
                cost = best[mask] + values[-1] - values[0]
                if cost < best[reached]:
                    best[reached] = cost

        return -1 if best[full] == INF else best[full]
