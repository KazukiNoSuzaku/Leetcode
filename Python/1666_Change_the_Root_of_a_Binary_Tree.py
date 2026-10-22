# Author: Kaustav Ghosh
# Problem: Change the Root of a Binary Tree
# Approach: Rerooting only touches the chain from the leaf up to the old root, since every other edge keeps its direction; along that chain each node adopts its former parent as its left child, which means its existing left child has to move aside to the right first, and the parent must drop its pointer to the node so the old downward edge disappears. The grandparent has to be captured before any rewiring, because the node's parent pointer is overwritten in the process and the chain would otherwise be lost. Walking upward one link at a time handles the whole path, and the new root's parent is finally cleared so the tree has a genuine top.

# Definition for a Node.
# class Node(object):
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None
#         self.parent = None


class Solution(object):
    def flipBinaryTree(self, root, leaf):
        """
        :type root: Node
        :type leaf: Node
        :rtype: Node
        """
        current = leaf
        parent = current.parent
        while current is not root:
            grandparent = parent.parent
            if current.left:
                current.right = current.left
            current.left = parent
            # Sever the old downward edge before moving on.
            if parent.left is current:
                parent.left = None
            else:
                parent.right = None
            parent.parent = current
            current = parent
            parent = grandparent
        leaf.parent = None
        return leaf
