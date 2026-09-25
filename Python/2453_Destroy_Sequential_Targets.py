# Author: Kaustav Ghosh
# Problem: Destroy Sequential Targets
# Approach: A seed destroys every target that matches it modulo space and is not smaller, so the reachable set is fixed by the remainder alone. Count the targets per remainder and remember the smallest value in each; the answer is the smallest value of a most populous remainder

from collections import defaultdict


class Solution(object):
    def destroyTargets(self, nums, space):
        """
        :type nums: List[int]
        :type space: int
        :rtype: int
        """
        counts = defaultdict(int)
        smallest = {}
        for x in nums:
            remainder = x % space
            counts[remainder] += 1
            if remainder not in smallest or x < smallest[remainder]:
                smallest[remainder] = x
        best = max(counts.values())
        return min(smallest[r] for r, c in counts.items() if c == best)
