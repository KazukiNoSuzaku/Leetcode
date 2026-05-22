from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root])
        root.val = 0
        while queue:
            level_sum = 0
            nodes = list(queue)
            for node in nodes:
                if node.left:
                    level_sum += node.left.val
                if node.right:
                    level_sum += node.right.val
            for node in nodes:
                sibling_sum = (node.left.val if node.left else 0) + (node.right.val if node.right else 0)
                if node.left:
                    node.left.val = level_sum - sibling_sum
                    queue.append(node.left)
                if node.right:
                    node.right.val = level_sum - sibling_sum
                    queue.append(node.right)
                queue.popleft()
        return root
