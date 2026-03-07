# Given the root of a binary tree, return the vertical order traversal of its nodes' values.
# (i.e., from top to bottom, column by column).
# If two nodes are in the same row and column, the order should be from left to right.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[9],[3,15],[20],[7]]

# Example 2:
# Input: root = [3,9,8,4,0,1,7]
# Output: [[4],[9],[3,0,1],[8],[7]]

# Constraints:
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

# Author: Kaustav Ghosh

from collections import defaultdict, deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def verticalOrder(self, root):
        if not root:
            return []
        cols = defaultdict(list)
        q = deque([(root, 0)])
        while q:
            node, col = q.popleft()
            cols[col].append(node.val)
            if node.left:
                q.append((node.left, col - 1))
            if node.right:
                q.append((node.right, col + 1))
        return [cols[c] for c in sorted(cols)]
