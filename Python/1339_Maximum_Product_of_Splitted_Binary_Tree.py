# Split a binary tree into two subtrees by removing one edge.
# Maximize the product of the two subtree sums. Return result mod 1e9+7.

# Author: Kaustav Ghosh

class Solution(object):
    def maxProduct(self, root):
        MOD = 10**9 + 7
        sums = []
        def get_sum(node):
            if not node: return 0
            s = node.val + get_sum(node.left) + get_sum(node.right)
            sums.append(s)
            return s
        total = get_sum(root)
        best = max(s * (total - s) for s in sums)
        return best % MOD
