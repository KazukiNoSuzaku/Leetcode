# Author: Kaustav Ghosh
# Problem: Distribute Repeating Integers
# Approach: A customer must take all their items of one single value, so only the multiset of per-value counts matters and there are at most fifty of them, while there are at most ten customers, which is small enough to track exactly which customers are already served as a bitmask. I precompute each subset of customers' total demand, then process the counts one at a time: a set of customers is servable using the counts seen so far if it was already servable without this count, or if some subset of it fits inside this count and the rest was servable before. Enumerating subsets of each mask rather than all mask pairs keeps the work to the sum over masks of their subset counts.

from collections import Counter


class Solution(object):
    def canDistribute(self, nums, quantity):
        """
        :type nums: List[int]
        :type quantity: List[int]
        :rtype: bool
        """
        counts = sorted(Counter(nums).values(), reverse=True)[:len(quantity)]
        customers = len(quantity)
        full = (1 << customers) - 1

        demand = [0] * (full + 1)
        for mask in range(1, full + 1):
            lowest = mask & -mask
            demand[mask] = demand[mask ^ lowest] + quantity[lowest.bit_length() - 1]

        servable = [False] * (full + 1)
        servable[0] = True
        for count in counts:
            for mask in range(full, 0, -1):
                if servable[mask]:
                    continue
                subset = mask
                while subset:
                    if demand[subset] <= count and servable[mask ^ subset]:
                        servable[mask] = True
                        break
                    subset = (subset - 1) & mask
            if servable[full]:
                return True
        return servable[full]
