# Author: Kaustav Ghosh
# Problem: Minimum Number of Vertices to Reach All Nodes
# Approach: A node with an incoming edge is reachable from somewhere else, while a node with none can only be a starting point, so every such node must be included. The graph is acyclic, so those nodes together reach everything and form the smallest possible set

class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        reachable = {target for _, target in edges}
        return [node for node in range(n) if node not in reachable]
