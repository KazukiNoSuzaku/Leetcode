# Author: Kaustav Ghosh
# 1038. Binary Search Tree to Greater Sum Tree
# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.acc = 0

        def reverse_inorder(node):
            if not node:
                return
            reverse_inorder(node.right)
            self.acc += node.val
            node.val = self.acc
            reverse_inorder(node.left)

        reverse_inorder(root)
        return root
