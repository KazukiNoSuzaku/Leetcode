from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def min_swaps(arr):
            # Minimum swaps to sort = n - number of cycles in value permutation
            indexed = sorted(range(len(arr)), key=lambda i: arr[i])
            visited = [False] * len(arr)
            swaps = 0
            for i in range(len(arr)):
                if visited[i] or indexed[i] == i:
                    visited[i] = True
                    continue
                cycle, j = 0, i
                while not visited[j]:
                    visited[j] = True
                    j = indexed[j]
                    cycle += 1
                swaps += cycle - 1
            return swaps

        ans = 0
        queue = deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans += min_swaps(level)
        return ans
