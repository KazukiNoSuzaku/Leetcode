# Author: Kaustav Ghosh

class Solution(object):
    def restoreArray(self, adjacentPairs):
        """
        :type adjacentPairs: List[List[int]]
        :rtype: List[int]
        """
        from collections import defaultdict
        graph = defaultdict(list)
        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)
        # Find start: node with only one neighbor
        start = None
        for node in graph:
            if len(graph[node]) == 1:
                start = node
                break
        res = [start]
        prev = None
        curr = start
        while len(res) < len(adjacentPairs) + 1:
            for neighbor in graph[curr]:
                if neighbor != prev:
                    res.append(neighbor)
                    prev = curr
                    curr = neighbor
                    break
        return res
