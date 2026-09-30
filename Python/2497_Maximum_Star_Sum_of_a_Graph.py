# Author: Kaustav Ghosh
# Problem: Maximum Star Sum of a Graph
# Approach: A star is a centre plus up to k of its neighbours, and neighbours are optional, so never take a negative one. Collect each node's positive neighbour values, keep the k largest, and add them to the centre's own value

from collections import defaultdict


class Solution(object):
    def maxStarSum(self, vals, edges, k):
        """
        :type vals: List[int]
        :type edges: List[List[int]]
        :type k: int
        :rtype: int
        """
        positive_neighbours = defaultdict(list)
        for a, b in edges:
            if vals[b] > 0:
                positive_neighbours[a].append(vals[b])
            if vals[a] > 0:
                positive_neighbours[b].append(vals[a])
        return max(value + sum(sorted(positive_neighbours[i], reverse=True)[:k])
                   for i, value in enumerate(vals))
