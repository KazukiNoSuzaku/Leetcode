# Author: Kaustav Ghosh
# Problem: Restore the Array From Adjacent Pairs
# Approach: The pairs describe the edges of a path, so every element lists its neighbours and the two endpoints are exactly the elements with a single neighbour; starting from either and walking forward reconstructs the array. The walk needs only the previous element to decide which way to go, since an interior element has two neighbours and one of them is where it came from, so no visited set over the whole array is required.

from collections import defaultdict


class Solution(object):
    def restoreArray(self, adjacentPairs):
        """
        :type adjacentPairs: List[List[int]]
        :rtype: List[int]
        """
        neighbours = defaultdict(list)
        for a, b in adjacentPairs:
            neighbours[a].append(b)
            neighbours[b].append(a)

        start = next(value for value, around in neighbours.items() if len(around) == 1)
        order = [start]
        previous = None
        current = start
        while len(order) <= len(adjacentPairs):
            nextValue = next(v for v in neighbours[current] if v != previous)
            order.append(nextValue)
            previous, current = current, nextValue
        return order
