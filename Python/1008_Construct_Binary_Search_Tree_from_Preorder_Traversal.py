# Return the root of the binary search tree that matches the given preorder traversal.

# Author: Kaustav Ghosh

class Solution(object):
    def bstFromPreorder(self, preorder):
        if not preorder: return None
        root = TreeNode(preorder[0])
        i = 1
        while i < len(preorder) and preorder[i] < preorder[0]:
            i += 1
        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])
        return root
