# Flip nodes in binary tree so that pre-order traversal matches voyage.
# Return flipped node values, or [-1] if impossible.

# Author: Kaustav Ghosh

class Solution(object):
    def flipMatchVoyage(self, root, voyage):
        self.i = 0
        self.flips = []
        def dfs(node):
            if not node: return True
            if node.val != voyage[self.i]: return False
            self.i += 1
            if node.left and node.left.val != voyage[self.i]:
                self.flips.append(node.val)
                node.left, node.right = node.right, node.left
            return dfs(node.left) and dfs(node.right)
        return self.flips if dfs(root) else [-1]
