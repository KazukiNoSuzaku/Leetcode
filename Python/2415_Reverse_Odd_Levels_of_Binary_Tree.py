from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])
        level = 0
        while q:
            nodes = list(q)
            if level % 2 == 1:
                lo, hi = 0, len(nodes) - 1
                while lo < hi:
                    nodes[lo].val, nodes[hi].val = nodes[hi].val, nodes[lo].val
                    lo += 1
                    hi -= 1
            q.clear()
            for node in nodes:
                if node.left:
                    q.append(node.left)
                    q.append(node.right)
            level += 1
        return root
