# Find longest path in a binary tree where all nodes have the same value.

# Author: Kaustav Ghosh

class Solution(object):
    def longestUnivaluePath(self, root):
        self.res = 0
        def dfs(node):
            if not node: return 0
            left = dfs(node.left)
            right = dfs(node.right)
            l = left + 1 if node.left and node.left.val == node.val else 0
            r = right + 1 if node.right and node.right.val == node.val else 0
            self.res = max(self.res, l + r)
            return max(l, r)
        dfs(root)
        return self.res
