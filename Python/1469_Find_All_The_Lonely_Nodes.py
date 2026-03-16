# Author: Kaustav Ghosh
# Problem: Find All The Lonely Nodes (Premium)
# Approach: DFS collecting nodes that have no sibling

class Solution(object):
    def getLonelyNodes(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []

        def dfs(node):
            if not node:
                return
            if node.left and not node.right:
                result.append(node.left.val)
            if node.right and not node.left:
                result.append(node.right.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return result
