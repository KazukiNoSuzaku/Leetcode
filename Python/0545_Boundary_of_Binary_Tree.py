# Given the root of a binary tree, return its boundary in anti-clockwise direction starting from root.
# Boundary includes: left boundary, leaves, right boundary (excluding root if leaf).

# Author: Kaustav Ghosh

class Solution(object):
    def boundaryOfBinaryTree(self, root):
        if not root: return []
        def left_boundary(node):
            if not node or (not node.left and not node.right): return []
            return [node.val] + (left_boundary(node.left) if node.left else left_boundary(node.right))
        def leaves(node):
            if not node: return []
            if not node.left and not node.right: return [node.val]
            return leaves(node.left) + leaves(node.right)
        def right_boundary(node):
            if not node or (not node.left and not node.right): return []
            return (right_boundary(node.right) if node.right else right_boundary(node.left)) + [node.val]
        return [root.val] + left_boundary(root.left) + leaves(root.left) + leaves(root.right) + right_boundary(root.right)
