# Author: Kaustav Ghosh
# Problem: Lowest Common Ancestor of a Binary Tree IV (Premium)
# Approach: Standard LCA generalized to a set of targets; a node is the answer if it is itself a target or if both subtrees each contain at least one target

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, nodes):
        """
        :type root: TreeNode
        :type nodes: List[TreeNode]
        :rtype: TreeNode
        """
        targets = set(nodes)

        def dfs(node):
            if node is None or node in targets:
                return node
            left = dfs(node.left)
            right = dfs(node.right)
            if left and right:
                return node
            return left or right

        return dfs(root)
