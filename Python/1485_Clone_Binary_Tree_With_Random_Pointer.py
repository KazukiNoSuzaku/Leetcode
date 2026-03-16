# Author: Kaustav Ghosh
# Problem: Clone Binary Tree With Random Pointer (Premium)
# Approach: DFS with hashmap to clone nodes and random pointers

class Solution(object):
    def copyRandomBinaryTree(self, root):
        """
        :type root: Node
        :rtype: NodeCopy
        """
        mapping = {}

        def clone(node):
            if not node:
                return None
            if node in mapping:
                return mapping[node]
            copy = NodeCopy(node.val)
            mapping[node] = copy
            copy.left = clone(node.left)
            copy.right = clone(node.right)
            copy.random = clone(node.random)
            return copy

        return clone(root)
