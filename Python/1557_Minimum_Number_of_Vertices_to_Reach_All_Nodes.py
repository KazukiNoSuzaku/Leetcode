# Author: Kaustav Ghosh
# Problem: Minimum Number of Vertices to Reach All Nodes
# Approach: In a DAG, every node with no incoming edge must be a source; those are exactly the required vertices

class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        has_incoming = [False] * n
        for _, to in edges:
            has_incoming[to] = True
        return [node for node in range(n) if not has_incoming[node]]
