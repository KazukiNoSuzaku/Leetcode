# Return the sum of values of nodes whose grandparent has an even value.

# Author: Kaustav Ghosh

class Solution(object):
    def sumEvenGrandparent(self, root):
        def dfs(node, parent, grandparent):
            if not node: return 0
            total = node.val if grandparent and grandparent.val % 2 == 0 else 0
            return total + dfs(node.left, node, parent) + dfs(node.right, node, parent)
        return dfs(root, None, None)
