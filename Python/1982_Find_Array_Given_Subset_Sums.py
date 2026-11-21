# Author: Kaustav Ghosh
# Problem: Find Array Given Subset Sums
# Approach: With the sums sorted, the gap between the two smallest is the absolute value of some element: every subset sum either uses that element or not, and the smallest sum paired with the next one differ by exactly one element's magnitude. Removing that element splits the multiset into two halves of equal size, one being the subset sums of the remaining elements and the other that same multiset shifted by the element; the split is found by walking the sorted sums and pairing each still-available value with that value plus the gap. Which half is which decides the sign: the half that is the remaining elements' own subset sums must contain zero, because the empty subset is always there, so if zero lands in the lower half the element is positive and otherwise it is negative. Recursing n times on halves of a multiset of size 2^n costs O(2^n * n) overall.

from collections import Counter

class Solution(object):
    def recoverArray(self, n, sums):
        """
        :type n: int
        :type sums: List[int]
        :rtype: List[int]
        """
        remaining = sorted(sums)
        found = []

        for _ in range(n):
            gap = remaining[1] - remaining[0]
            available = Counter(remaining)

            lower = []
            upper = []
            for value in remaining:
                if available[value] <= 0:
                    continue
                available[value] -= 1
                available[value + gap] -= 1
                lower.append(value)
                upper.append(value + gap)

            if 0 in lower:
                found.append(gap)
                remaining = lower
            else:
                found.append(-gap)
                remaining = upper

        return found
