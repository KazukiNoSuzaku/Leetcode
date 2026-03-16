# Author: Kaustav Ghosh
# Problem: Pseudo-Palindromic Paths in a Binary Tree
# Approach: DFS with XOR bitmask, count paths with at most 1 bit set

class Solution(object):
    def pseudoPalindromicPaths(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, mask):
            if not node:
                return 0
            mask ^= 1 << node.val
            if not node.left and not node.right:
                return 1 if mask & (mask - 1) == 0 else 0
            return dfs(node.left, mask) + dfs(node.right, mask)

        return dfs(root, 0)
