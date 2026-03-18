# Author: Kaustav Ghosh
# Problem: 1557 - Minimum Number of Vertices to Reach All Nodes
# Approach: Nodes with in-degree 0 must be included

class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        has_incoming = set(v for _, v in edges)
        return [i for i in range(n) if i not in has_incoming]
