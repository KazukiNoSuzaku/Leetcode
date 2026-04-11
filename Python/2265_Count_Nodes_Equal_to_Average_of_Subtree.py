# Author: Kaustav Ghosh
# Problem: 2265. Count Nodes Equal to Average of Subtree
# URL: https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/
# Difficulty: Medium
#
# Approach:
# Post-order DFS returning (sum, count) for each subtree.
# If node.val equals sum // count, increment the result.

class Solution(object):
    def averageOfSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0

        def dfs(node):
            if not node:
                return 0, 0
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)
            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1
            if total_sum // total_count == node.val:
                self.result += 1
            return total_sum, total_count

        dfs(root)
        return self.result
