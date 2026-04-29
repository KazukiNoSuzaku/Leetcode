from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: list[int]) -> list[int]:
        height = {}

        def get_height(node):
            if not node:
                return -1
            h = 1 + max(get_height(node.left), get_height(node.right))
            height[node.val] = h
            return h

        get_height(root)

        # ans[v] = max depth of any node NOT in v's subtree = height of tree after removing v
        ans = {}

        def dfs(node, depth, best):
            if not node:
                return
            ans[node.val] = best
            lh = height[node.left.val] if node.left else -1
            rh = height[node.right.val] if node.right else -1
            # When descending into left, best reachable outside left subtree:
            # max(best, depth of deepest node in right subtree or current node if no right)
            dfs(node.left, depth + 1, max(best, depth + 1 + rh))
            dfs(node.right, depth + 1, max(best, depth + 1 + lh))

        dfs(root, 0, -1)
        return [ans[q] for q in queries]
