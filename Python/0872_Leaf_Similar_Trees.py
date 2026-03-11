# Check if two binary trees have the same leaf value sequence.

# Author: Kaustav Ghosh

class Solution(object):
    def leafSimilar(self, root1, root2):
        def leaves(node):
            if not node: return []
            if not node.left and not node.right: return [node.val]
            return leaves(node.left) + leaves(node.right)
        return leaves(root1) == leaves(root2)
