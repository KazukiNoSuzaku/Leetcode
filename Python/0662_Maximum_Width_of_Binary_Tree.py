# Find the maximum width of a binary tree (widest level including null nodes between endpoints).

# Author: Kaustav Ghosh

from collections import deque

class Solution(object):
    def widthOfBinaryTree(self, root):
        if not root: return 0
        q = deque([(root, 0)])
        max_width = 0
        while q:
            level_len = len(q)
            _, first_idx = q[0]
            for _ in range(level_len):
                node, idx = q.popleft()
                if node.left: q.append((node.left, 2 * idx))
                if node.right: q.append((node.right, 2 * idx + 1))
            max_width = max(max_width, idx - first_idx + 1)
        return max_width
