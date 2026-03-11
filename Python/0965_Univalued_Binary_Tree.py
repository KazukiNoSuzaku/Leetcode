# A binary tree is uni-valued if every node in the tree has the same value.
# Return true if and only if the given tree is uni-valued.

# Author: Kaustav Ghosh

class Solution(object):
    def isUnivalTree(self, root):
        def dfs(node):
            if not node: return True
            if node.val != root.val: return False
            return dfs(node.left) and dfs(node.right)
        return dfs(root)
