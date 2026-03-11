# Return the vertical order traversal of a binary tree.
# Nodes are sorted by column, then row, then value.

# Author: Kaustav Ghosh

from collections import defaultdict

class Solution(object):
    def verticalTraversal(self, root):
        nodes = []
        def dfs(node, row, col):
            if not node: return
            nodes.append((col, row, node.val))
            dfs(node.left, row+1, col-1)
            dfs(node.right, row+1, col+1)
        dfs(root, 0, 0)
        nodes.sort()
        res = []
        prev_col = None
        for col, row, val in nodes:
            if col != prev_col:
                res.append([])
                prev_col = col
            res[-1].append(val)
        return res
