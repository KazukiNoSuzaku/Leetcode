# Author: Kaustav Ghosh
# Problem: Find Distance in a Binary Tree (Premium)
# Approach: The path between two nodes bends at their lowest common ancestor, so the distance is depth(p) + depth(q) measured down from that LCA

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def findDistance(self, root, p, q):
        """
        :type root: TreeNode
        :type p: int
        :type q: int
        :rtype: int
        """
        if p == q:
            return 0

        def lca(node):
            if node is None or node.val == p or node.val == q:
                return node
            left = lca(node.left)
            right = lca(node.right)
            if left and right:
                return node
            return left or right

        def depth(node, target, d):
            if node is None:
                return -1
            if node.val == target:
                return d
            found = depth(node.left, target, d + 1)
            if found != -1:
                return found
            return depth(node.right, target, d + 1)

        ancestor = lca(root)
        return depth(ancestor, p, 0) + depth(ancestor, q, 0)
