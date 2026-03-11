# Given a node in a BST (with parent pointer), return the in-order successor of that node.
# The successor of a node p is the node with the smallest key greater than p.val.

# Author: Kaustav Ghosh

class Solution(object):
    def inorderSuccessor(self, node):
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        while node.parent and node == node.parent.right:
            node = node.parent
        return node.parent
