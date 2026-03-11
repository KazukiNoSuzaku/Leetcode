# Find the maximum value v where v = |a.val - b.val| and a is an ancestor of b.

# Author: Kaustav Ghosh

class Solution(object):
    def maxAncestorDiff(self, root):
        def dfs(node, mn, mx):
            if not node:
                return mx - mn
            mn = min(mn, node.val)
            mx = max(mx, node.val)
            return max(dfs(node.left, mn, mx), dfs(node.right, mn, mx))
        return dfs(root, root.val, root.val)
