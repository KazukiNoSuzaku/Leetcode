# Remove all subtrees not containing a 1 from a binary tree.

# Author: Kaustav Ghosh

class Solution(object):
    def pruneTree(self, root):
        if not root: return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if root.val == 0 and not root.left and not root.right: return None
        return root
