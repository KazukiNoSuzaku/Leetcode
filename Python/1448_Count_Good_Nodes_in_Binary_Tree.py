# Author: Kaustav Ghosh
# Problem: Count Good Nodes in Binary Tree
# Approach: DFS tracking max value on path from root

class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, max_val):
            if not node:
                return 0
            count = 1 if node.val >= max_val else 0
            new_max = max(max_val, node.val)
            return count + dfs(node.left, new_max) + dfs(node.right, new_max)

        return dfs(root, root.val)
