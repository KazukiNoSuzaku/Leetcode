# Author: Kaustav Ghosh
# Problem: Lowest Common Ancestor of a Binary Tree III
# Approach: With parent pointers the two paths to the root form two chains that merge at the ancestor, which is the same shape as two linked lists that share a tail, so the constant-space trick for that applies here: walk a pointer up from each node and, on reaching the root, restart it from the other node. Each pointer then covers one path followed by the other, so both have travelled the same total distance when they coincide, and that meeting point is the lowest common ancestor. This avoids the usual set of one node's ancestors, so the extra space is a couple of pointers rather than proportional to the tree's depth.

# Definition for a Node.
# class Node(object):
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None
#         self.parent = None


class Solution(object):
    def lowestCommonAncestor(self, p, q):
        """
        :type node: Node
        :rtype: Node
        """
        walker, other = p, q
        while walker is not other:
            walker = walker.parent if walker.parent else q
            other = other.parent if other.parent else p
        return walker
