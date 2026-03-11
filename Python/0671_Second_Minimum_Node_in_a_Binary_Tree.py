# Find the second minimum value in a special binary tree where each parent equals min of children.

# Author: Kaustav Ghosh

class Solution(object):
    def findSecondMinimumValue(self, root):
        self.res = float('inf')
        self.min_val = root.val
        def dfs(node):
            if not node: return
            if self.min_val < node.val < self.res:
                self.res = node.val
            elif node.val == self.min_val:
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return self.res if self.res < float('inf') else -1
