# Print a binary tree in a 2D string matrix with proper spacing.

# Author: Kaustav Ghosh

class Solution(object):
    def printTree(self, root):
        def height(node):
            if not node: return 0
            return 1 + max(height(node.left), height(node.right))
        h = height(root)
        rows, cols = h, (1 << h) - 1
        res = [[''] * cols for _ in range(rows)]
        def fill(node, row, lo, hi):
            if not node: return
            mid = (lo + hi) // 2
            res[row][mid] = str(node.val)
            fill(node.left, row + 1, lo, mid - 1)
            fill(node.right, row + 1, mid + 1, hi)
        fill(root, 0, 0, cols - 1)
        return res
