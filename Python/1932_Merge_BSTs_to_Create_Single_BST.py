# Author: Kaustav Ghosh
# Problem: Merge BSTs to Create Single BST
# Approach: The final root is the one tree root whose value never appears as a leaf. Map value -> root for the others; then in a single bounded DFS, whenever a leaf matches an unused root value, splice that tree in. The result is valid iff bounds hold everywhere and every tree gets consumed exactly once

import sys
from collections import Counter

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
        sys.setrecursionlimit(200000)

        leaf_count = Counter()
        root_by_val = {}
        for t in trees:
            root_by_val[t.val] = t
            if t.left:
                leaf_count[t.left.val] += 1
            if t.right:
                leaf_count[t.right.val] += 1

        overall = None
        for t in trees:
            if leaf_count[t.val] == 0:
                if overall is not None:
                    return None          # more than one possible root
                overall = t
        if overall is None:
            return None

        attach = dict(root_by_val)
        del attach[overall.val]          # the overall root is the base, not spliced

        def dfs(node, lo, hi):
            if node is None:
                return True
            if not (lo < node.val < hi):
                return False
            if node.left is None and node.right is None and node.val in attach:
                sub = attach.pop(node.val)
                node.left = sub.left
                node.right = sub.right
            return dfs(node.left, lo, node.val) and dfs(node.right, node.val, hi)

        if dfs(overall, float('-inf'), float('inf')) and not attach:
            return overall
        return None
