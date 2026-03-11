# Find smallest subtree containing all deepest nodes.

# Author: Kaustav Ghosh

class Solution(object):
    def subtreeWithAllDeepest(self, root):
        def dfs(node):
            if not node: return None, 0
            left, ld = dfs(node.left)
            right, rd = dfs(node.right)
            if ld == rd: return node, ld + 1
            if ld > rd: return left, ld + 1
            return right, rd + 1
        return dfs(root)[0]
