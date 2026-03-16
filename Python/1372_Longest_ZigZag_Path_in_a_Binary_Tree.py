# Author: Kaustav Ghosh
# Problem: Longest ZigZag Path in a Binary Tree
# Approach: DFS tracking direction and length

class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0

        def dfs(node):
            if not node:
                return -1, -1  # left_len, right_len
            ll, lr = dfs(node.left)
            rl, rr = dfs(node.right)
            left_len = lr + 1 if node.left else 0
            right_len = rl + 1 if node.right else 0
            self.result = max(self.result, left_len, right_len)
            return left_len, right_len

        dfs(root)
        return self.result
