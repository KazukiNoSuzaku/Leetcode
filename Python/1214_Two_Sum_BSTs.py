# Premium problem - not available without subscription
# Author: Kaustav Ghosh
# Typical approach: Inorder traverse one BST into set, search complement in other

class Solution(object):
    def twoSumBSTs(self, root1, root2, target):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :type target: int
        :rtype: bool
        """
        vals = set()

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            vals.add(node.val)
            inorder(node.right)

        inorder(root1)

        def search(node):
            if not node:
                return False
            if target - node.val in vals:
                return True
            return search(node.left) or search(node.right)

        return search(root2)
