# Author: Kaustav Ghosh
# Problem: Paths in Maze That Lead to Same Room
# Approach: The confusion score counts triangles (length-3 cycles). For each corridor, the number of common neighbors of its two rooms counts the third vertex of a triangle; summing over edges counts each triangle three times

from collections import defaultdict

class Solution(object):
    def numberOfPaths(self, n, corridors):
        """
        :type n: int
        :type corridors: List[List[int]]
        :rtype: int
        """
        adj = defaultdict(set)
        for a, b in corridors:
            adj[a].add(b)
            adj[b].add(a)

        total = 0
        for a, b in corridors:
            total += len(adj[a] & adj[b])
        return total // 3
