# Author: Kaustav Ghosh
# Problem: Count Nodes Equal to Average of Subtree
# Approach: Post-order DFS returning each subtree's total sum and node count. At every node, check whether its value equals the floored average of its subtree, tallying matches

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def averageOfSubtree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.count = 0

        def dfs(node):
            if not node:
                return (0, 0)
            ls, lc = dfs(node.left)
            rs, rc = dfs(node.right)
            total = ls + rs + node.val
            cnt = lc + rc + 1
            if total // cnt == node.val:
                self.count += 1
            return (total, cnt)

        dfs(root)
        return self.count
