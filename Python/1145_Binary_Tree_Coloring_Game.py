# Author: Kaustav Ghosh
# Find node x, check if any of the 3 regions (left, right, parent) has > n/2 nodes

class Solution(object):
    def btreeGameWinningMove(self, root, n, x):
        """
        :type root: TreeNode
        :type n: int
        :type x: int
        :rtype: bool
        """
        self.left_count = 0
        self.right_count = 0

        def count(node):
            if not node:
                return 0
            l = count(node.left)
            r = count(node.right)
            if node.val == x:
                self.left_count = l
                self.right_count = r
            return l + r + 1

        count(root)
        parent_count = n - self.left_count - self.right_count - 1
        return max(self.left_count, self.right_count, parent_count) > n // 2
