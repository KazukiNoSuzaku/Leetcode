# Given the root of a binary search tree, a target value, and an integer k, return the k values
# in the BST that are closest to the target. You may return the answer in any order.

# Example 1:
# Input: root = [4,2,5,1,3], target = 3.714286, k = 2
# Output: [4,3]

# Example 2:
# Input: root = [1], target = 0.000000, k = 1
# Output: [1]

# Constraints:
# The number of nodes in the tree is n.
# 1 <= k <= n <= 10^4
# 0 <= Node.val <= 10^9

# Author: Kaustav Ghosh

import heapq

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def closestKValues(self, root, target, k):
        heap = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            heapq.heappush(heap, (-abs(node.val - target), node.val))
            if len(heap) > k:
                heapq.heappop(heap)
            inorder(node.right)
        inorder(root)
        return [val for _, val in heap]
