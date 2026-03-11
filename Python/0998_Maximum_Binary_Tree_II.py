# Given a maximum binary tree and a new value val, insert val into the array
# used to construct it (appended at the end) and return the new root.

# Author: Kaustav Ghosh

class Solution(object):
    def insertIntoMaxTree(self, root, val):
        if not root or root.val < val:
            node = type(root)(val) if root else type('TreeNode', (), {'val': val, 'left': None, 'right': None})()
            node.left = root
            return node
        root.right = self.insertIntoMaxTree(root.right, val)
        return root
