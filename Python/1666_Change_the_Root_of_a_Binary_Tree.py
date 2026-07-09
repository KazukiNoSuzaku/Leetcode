# Author: Kaustav Ghosh
# Problem: Change the Root of a Binary Tree (Premium)
# Approach: Walk from the leaf up to the root, re-hanging each parent as the current node's left child (moving any existing left to the right first)

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution(object):
    def flipBinaryTree(self, root, leaf):
        """
        :type root: Node
        :type leaf: Node
        :rtype: Node
        """
        cur = leaf
        parent = cur.parent
        cur.parent = None

        while cur is not root:
            grandparent = parent.parent
            # Detach cur from its parent's child pointers
            if parent.left is cur:
                parent.left = None
            else:
                parent.right = None
            # Make space on the left and re-hang the parent there
            if cur.left is not None:
                cur.right = cur.left
            cur.left = parent
            parent.parent = cur
            # Move one level up
            cur = parent
            parent = grandparent

        return leaf
