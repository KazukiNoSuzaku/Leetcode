# Author: Kaustav Ghosh
# 1123. Lowest Common Ancestor of Deepest Leaves
# https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def dfs(node):
            if not node:
                return None, 0
            left_lca, left_depth = dfs(node.left)
            right_lca, right_depth = dfs(node.right)
            if left_depth == right_depth:
                return node, left_depth + 1
            elif left_depth > right_depth:
                return left_lca, left_depth + 1
            else:
                return right_lca, right_depth + 1

        return dfs(root)[0]
