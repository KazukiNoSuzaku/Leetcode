# Author: Kaustav Ghosh
# Problem: Correct a Binary Tree
# Approach: The defect is a right pointer aimed sideways at a node of the same depth rather than downwards, so it is identified by a property that no legitimate pointer can have: a node's right child belonging to the node's own level. Walking the tree level by level and collecting each level before descending makes that test immediate, and because the faulty node is found while its level is being examined the sideways pointer is never followed, so the cycle it creates cannot trap the traversal. Carrying each node's parent through the queue allows the offending node to be detached as soon as it is spotted, which discards its subtree with it; the traversal is iterative, so a tree of ten thousand nodes in a chain is no problem.

from collections import deque


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def correctBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        level = [(root, None)]
        while level:
            on_this_level = set(node for node, _ in level)
            for node, parent in level:
                if node.right is not None and node.right in on_this_level:
                    if parent.left is node:
                        parent.left = None
                    else:
                        parent.right = None
                    return root
            following = []
            for node, _ in level:
                if node.left:
                    following.append((node.left, node))
                if node.right:
                    following.append((node.right, node))
            level = following
        return root
