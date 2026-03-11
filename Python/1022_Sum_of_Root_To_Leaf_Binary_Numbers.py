# Each root-to-leaf path represents a binary number. Return the sum of all such numbers.

# Author: Kaustav Ghosh

class Solution(object):
    def sumRootToLeaf(self, root):
        def dfs(node, cur):
            if not node: return 0
            cur = cur * 2 + node.val
            if not node.left and not node.right:
                return cur
            return dfs(node.left, cur) + dfs(node.right, cur)
        return dfs(root, 0)
