# Given the root of a Binary Search Tree, convert it to a Greater Tree such that every key
# of the original BST is changed to the original key plus the sum of all keys greater than it.

# Author: Kaustav Ghosh

class Solution(object):
    def convertBST(self, root):
        self.acc = 0
        def reverse_inorder(node):
            if not node: return
            reverse_inorder(node.right)
            self.acc += node.val
            node.val = self.acc
            reverse_inorder(node.left)
        reverse_inorder(root)
        return root
