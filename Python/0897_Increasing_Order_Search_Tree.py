# Rearrange BST in-order into a right-only tree starting at smallest.

# Author: Kaustav Ghosh

class Solution(object):
    def increasingBST(self, root):
        dummy = TreeNode(0)
        self.cur = dummy
        def inorder(node):
            if not node: return
            inorder(node.left)
            node.left = None
            self.cur.right = node
            self.cur = node
            inorder(node.right)
        inorder(root)
        return dummy.right
