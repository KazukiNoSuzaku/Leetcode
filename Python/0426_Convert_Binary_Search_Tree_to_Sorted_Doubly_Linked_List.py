# Convert a Binary Search Tree to a sorted circular doubly-linked list in-place.
# Think of the left and right pointers as synonymous to the previous and next pointers.

# Author: Kaustav Ghosh

class Solution(object):
    def treeToDoublyList(self, root):
        if not root:
            return None
        self.first = self.last = None

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if self.last:
                self.last.right = node
                node.left = self.last
            else:
                self.first = node
            self.last = node
            inorder(node.right)

        inorder(root)
        self.last.right = self.first
        self.first.left = self.last
        return self.first
