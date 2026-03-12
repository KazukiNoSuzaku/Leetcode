# Author: Kaustav Ghosh
# 1080. Insufficient Nodes in Root to Leaf Paths
# https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/

class Solution(object):
    def sufficientSubset(self, root, limit):
        """
        :type root: TreeNode
        :type limit: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if not root.left and not root.right:
            return None if root.val < limit else root
        root.left = self.sufficientSubset(root.left, limit - root.val)
        root.right = self.sufficientSubset(root.right, limit - root.val)
        if not root.left and not root.right:
            return None
        return root
