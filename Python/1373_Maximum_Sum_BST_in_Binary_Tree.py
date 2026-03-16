# Author: Kaustav Ghosh
# Problem: Maximum Sum BST in Binary Tree
# Approach: Post-order DFS validating BST and tracking max sum

class Solution(object):
    def maxSumBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0

        def dfs(node):
            # Returns (is_bst, min_val, max_val, sum)
            if not node:
                return True, float('inf'), float('-inf'), 0

            l_bst, l_min, l_max, l_sum = dfs(node.left)
            r_bst, r_min, r_max, r_sum = dfs(node.right)

            if l_bst and r_bst and l_max < node.val < r_min:
                total = l_sum + r_sum + node.val
                self.result = max(self.result, total)
                return True, min(l_min, node.val), max(r_max, node.val), total

            return False, 0, 0, 0

        dfs(root)
        return self.result
