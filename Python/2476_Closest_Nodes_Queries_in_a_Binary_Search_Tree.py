import bisect
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: list[int]) -> list[list[int]]:
        vals = []

        def inorder(node):
            if node:
                inorder(node.left)
                vals.append(node.val)
                inorder(node.right)

        inorder(root)

        ans = []
        for q in queries:
            i = bisect.bisect_right(vals, q) - 1
            mn = vals[i] if i >= 0 else -1
            j = bisect.bisect_left(vals, q)
            mx = vals[j] if j < len(vals) else -1
            ans.append([mn, mx])
        return ans
