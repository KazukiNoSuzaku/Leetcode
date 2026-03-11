# Generate all full binary trees with n nodes.

# Author: Kaustav Ghosh

class Solution(object):
    def allPossibleFBT(self, n):
        if n % 2 == 0: return []
        if n == 1: return [TreeNode(0)]
        res = []
        for left in range(1, n, 2):
            right = n - 1 - left
            for l in self.allPossibleFBT(left):
                for r in self.allPossibleFBT(right):
                    node = TreeNode(0)
                    node.left = l
                    node.right = r
                    res.append(node)
        return res
