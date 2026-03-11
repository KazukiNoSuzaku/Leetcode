# Given the root of a binary tree and an integer targetSum, return the number of paths
# where the sum of the values along the path equals targetSum.
# The path does not need to start or end at the root or a leaf, but it must go downwards.

# Author: Kaustav Ghosh

from collections import defaultdict

class Solution(object):
    def pathSum(self, root, targetSum):
        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        self.res = 0

        def dfs(node, curr_sum):
            if not node:
                return
            curr_sum += node.val
            self.res += prefix_count[curr_sum - targetSum]
            prefix_count[curr_sum] += 1
            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)
            prefix_count[curr_sum] -= 1

        dfs(root, 0)
        return self.res
