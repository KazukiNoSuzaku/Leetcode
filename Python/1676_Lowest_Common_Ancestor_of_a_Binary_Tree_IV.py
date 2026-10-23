# Author: Kaustav Ghosh
# Problem: Lowest Common Ancestor of a Binary Tree IV
# Approach: The pairwise argument generalises directly to a whole set: a subtree reports the lowest node covering whichever targets lie inside it, and a node whose two subtrees both report something must itself be the meeting point, while a node with only one reporting side just passes that report upward. A node that is itself a target reports itself and need not be descended into at all, since every target below it is already covered by it. All targets are guaranteed present, so the root's report is the answer. The traversal is an explicit post-order stack rather than recursion, because ten thousand nodes arranged as a chain would recurse past Python's limit.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, nodes):
        """
        :type root: TreeNode
        :type nodes: List[TreeNode]
        :rtype: TreeNode
        """
        targets = set(node.val for node in nodes)
        covers = {}
        stack = [(root, False)]
        while stack:
            node, expanded = stack.pop()
            if node is None:
                continue
            if node.val in targets:
                covers[node] = node
                continue
            if not expanded:
                stack.append((node, True))
                stack.append((node.left, False))
                stack.append((node.right, False))
                continue
            left = covers.get(node.left)
            right = covers.get(node.right)
            covers[node] = node if (left and right) else (left or right)
        return covers.get(root)
