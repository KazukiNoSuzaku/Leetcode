# Author: Kaustav Ghosh
# Problem: Correct a Binary Tree (Premium)
# Approach: DFS visiting right before left with a seen-set; the invalid node is the one whose right child was already seen (it points rightward on the same level), so drop it

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def correctBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        seen = set()

        def dfs(node):
            if not node:
                return None
            # Invalid node: its right child was already visited on this level
            if node.right in seen:
                return None
            seen.add(node)
            node.right = dfs(node.right)
            node.left = dfs(node.left)
            return node

        return dfs(root)
