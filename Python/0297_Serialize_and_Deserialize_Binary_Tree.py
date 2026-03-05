# Serialization is the process of converting a data structure or object into a sequence of bits
# so that it can be stored in a file or memory buffer, or transmitted across a network connection link
# to be reconstructed later in the same or another computer environment.
# Design an algorithm to serialize and deserialize a binary tree.

# Example 1:
# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]

# Example 2:
# Input: root = []
# Output: []

# Constraints:
# The number of nodes in the tree is in the range [0, 10^4].
# -1000 <= Node.val <= 1000

# Author: Kaustav Ghosh

from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        if not root:
            return ''
        q, res = deque([root]), []
        while q:
            node = q.popleft()
            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append('#')
        return ','.join(res)

    def deserialize(self, data):
        if not data:
            return None
        vals = iter(data.split(','))
        root = TreeNode(int(next(vals)))
        q = deque([root])
        for node in q:
            left_val = next(vals)
            if left_val != '#':
                node.left = TreeNode(int(left_val))
                q.append(node.left)
            right_val = next(vals)
            if right_val != '#':
                node.right = TreeNode(int(right_val))
                q.append(node.right)
        return root
