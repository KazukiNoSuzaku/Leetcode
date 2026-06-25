# Author: Kaustav Ghosh
# Problem: Diameter of N-Ary Tree (Premium)
# Approach: DFS returning max depth; at each node track sum of two longest child depths for diameter

class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution(object):
    def diameter(self, root):
        """
        :type root: 'Node'
        :rtype: int
        """
        self.ans = 0

        def dfs(node):
            depths = sorted([dfs(c) for c in node.children], reverse=True)
            top2 = (depths + [0, 0])[:2]
            self.ans = max(self.ans, top2[0] + top2[1])
            return top2[0] + 1

        dfs(root)
        return self.ans
