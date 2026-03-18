# Author: Kaustav Ghosh
# Problem: 1522 - Diameter of N-Ary Tree (Premium)
# Approach: DFS tracking two longest paths from each node

class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution(object):
    def diameter(self, root):
        """
        :type root: Node
        :rtype: int
        """
        self.result = 0

        def dfs(node):
            if not node.children:
                return 0
            depths = sorted([dfs(child) + 1 for child in node.children], reverse=True)
            if len(depths) >= 2:
                self.result = max(self.result, depths[0] + depths[1])
            else:
                self.result = max(self.result, depths[0])
            return depths[0]

        dfs(root)
        return self.result
