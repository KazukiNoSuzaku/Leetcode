# Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph.
# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

# Example 1:
# Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
# Output: [[2,4],[1,3],[2,4],[1,3]]

# Example 2:
# Input: adjList = [[]]
# Output: [[]]

# Constraints:
# The number of nodes in the graph is in the range [0, 100].
# 1 <= Node.val <= 100
# Node.val is unique for each node.
# There are no repeated edges and no self-loops in the graph.

# Author: Kaustav Ghosh

class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return None
        cloned = {}
        def dfs(n):
            if n in cloned:
                return cloned[n]
            copy = Node(n.val)
            cloned[n] = copy
            for neighbor in n.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy
        return dfs(node)
