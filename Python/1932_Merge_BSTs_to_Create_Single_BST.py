# Author: Kaustav Ghosh
# https://leetcode.com/problems/merge-bsts-to-create-single-bst/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def canMerge(self, trees):
        """
        :type trees: List[TreeNode]
        :rtype: TreeNode
        """
        # Map root values to trees
        root_map = {}
        leaf_count = {}

        for t in trees:
            root_map[t.val] = t
            for child in [t.left, t.right]:
                if child:
                    leaf_count[child.val] = leaf_count.get(child.val, 0) + 1

        # Find the root of the final BST (appears as root but not as leaf)
        root = None
        for t in trees:
            if t.val not in leaf_count:
                if root:
                    return None
                root = t

        if not root:
            return None

        # Merge trees by replacing leaf nodes with matching root trees
        used = set()

        def merge(node):
            if not node:
                return node
            if not node.left and not node.right and node.val in root_map and root_map[node.val] != node:
                if node.val in used:
                    return None
                used.add(node.val)
                node = root_map[node.val]
            node.left = merge(node.left)
            node.right = merge(node.right)
            return node

        used.add(root.val)
        root = merge(root)

        if len(used) != len(trees):
            return None

        # Validate BST
        def validate(node, lo, hi):
            if not node:
                return True
            if node.val <= lo or node.val >= hi:
                return False
            return validate(node.left, lo, node.val) and validate(node.right, node.val, hi)

        return root if validate(root, float('-inf'), float('inf')) else None
