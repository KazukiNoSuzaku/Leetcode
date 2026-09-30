# Author: Kaustav Ghosh
# Problem: Minimum Total Cost to Make Arrays Unequal
# Approach: Every index where the arrays already collide must take part in some swap, so start by paying for exactly those. They can be permuted among themselves unless one value dominates more than half of them, in which case the surplus needs partners from elsewhere: walk the remaining indices from cheapest upward and enlist any whose values clash with neither side of that dominant value. If the collisions still cannot be broken the task is impossible

from collections import Counter


class Solution(object):
    def minimumTotalCost(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        total = 0
        involved = 0
        counts = Counter()
        for i, (a, b) in enumerate(zip(nums1, nums2)):
            if a == b:
                total += i
                involved += 1
                counts[a] += 1
        if not counts:
            return 0
        dominant = max(counts, key=counts.get)
        dominant_count = counts[dominant]
        for i, (a, b) in enumerate(zip(nums1, nums2)):
            if dominant_count * 2 <= involved:
                break
            if a != b and a != dominant and b != dominant:
                total += i
                involved += 1
        return total if dominant_count * 2 <= involved else -1
