# Return the sum of values of the deepest leaves in a binary tree.

# Author: Kaustav Ghosh

class Solution(object):
    def deepestLeavesSum(self, root):
        self.max_depth = 0
        self.total = 0
        def dfs(node, depth):
            if not node:
                return
            if not node.left and not node.right:
                if depth > self.max_depth:
                    self.max_depth = depth
                    self.total = node.val
                elif depth == self.max_depth:
                    self.total += node.val
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        dfs(root, 1)
        return self.total
