# Check if a binary tree can be split into two equal-sum subtrees by removing one edge.

# Author: Kaustav Ghosh

class Solution(object):
    def checkEqualTree(self, root):
        seen = []
        def subtree_sum(node):
            if not node: return 0
            s = node.val + subtree_sum(node.left) + subtree_sum(node.right)
            seen.append(s)
            return s
        total = subtree_sum(root)
        return total / 2.0 in seen[:-1]
