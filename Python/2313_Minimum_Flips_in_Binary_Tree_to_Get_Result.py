# Author: Kaustav Ghosh
# 2313. Minimum Flips in Binary Tree to Get Result
# Premium problem
# Tree DP: for each node, compute (min_flips_to_be_0, min_flips_to_be_1)
# Leaf nodes: 0 -> (0, 1), 1 -> (1, 0)
# OR node: can_be_0 = left_0 + right_0; can_be_1 = min combos with at least one 1
# AND node: can_be_1 = left_1 + right_1; can_be_0 = min combos with at least one 0
# XOR node: can_be_0 = min(l0+r0, l1+r1); can_be_1 = min(l0+r1, l1+r0)
# NOT node (one child): can_be_0 = child_1; can_be_1 = child_0

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    pass
