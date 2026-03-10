# Given the root of a binary tree, collect a tree's nodes as if you were doing this:
# Collect all the leaf nodes. Remove all the leaf nodes. Repeat until the tree is empty.

# Example 1:
# Input: root = [1,2,3,4,5]
# Output: [[4,5,3],[2],[1]]

# Constraints:
# The number of nodes in the tree is in the range [1, 100].
# -100 <= Node.val <= 100

# Author: Kaustav Ghosh

class Solution(object):
    def findLeaves(self, root):
        res = []

        def height(node):
            if not node:
                return -1
            h = 1 + max(height(node.left), height(node.right))
            if h == len(res):
                res.append([])
            res[h].append(node.val)
            return h

        height(root)
        return res
