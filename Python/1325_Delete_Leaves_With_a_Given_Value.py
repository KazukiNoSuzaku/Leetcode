# Remove all leaves with value target. Repeat until no such leaf exists.

# Author: Kaustav Ghosh

class Solution(object):
    def removeLeafNodes(self, root, target):
        if not root:
            return None
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        if not root.left and not root.right and root.val == target:
            return None
        return root
