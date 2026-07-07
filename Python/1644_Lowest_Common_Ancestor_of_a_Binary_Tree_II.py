# Author: Kaustav Ghosh
# Problem: Lowest Common Ancestor of a Binary Tree II (Premium)
# Approach: Full post-order traversal (no short-circuit) that returns whether p or q is below; the LCA is where two hits meet. Also count total hits so a missing node yields None

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.ans = None
        self.count = 0

        def dfs(node):
            if not node:
                return False
            left = dfs(node.left)
            right = dfs(node.right)
            mid = node is p or node is q
            if mid:
                self.count += 1
            if mid + left + right >= 2:
                self.ans = node
            return mid or left or right

        dfs(root)
        # Only valid when both nodes are actually present
        return self.ans if self.count == 2 else None
