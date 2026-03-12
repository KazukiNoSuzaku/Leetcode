# Author: Kaustav Ghosh
# 1120. Maximum Average Subtree
# https://leetcode.com/problems/maximum-average-subtree/

class Solution(object):
    def maximumAverageSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: float
        """
        self.max_avg = 0.0

        def dfs(node):
            if not node:
                return 0, 0
            left_sum, left_cnt = dfs(node.left)
            right_sum, right_cnt = dfs(node.right)
            total_sum = left_sum + right_sum + node.val
            total_cnt = left_cnt + right_cnt + 1
            avg = total_sum / float(total_cnt)
            if avg > self.max_avg:
                self.max_avg = avg
            return total_sum, total_cnt

        dfs(root)
        return self.max_avg
