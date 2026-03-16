# Author: Kaustav Ghosh
# Problem: Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree (Premium)
# Approach: DFS checking sequence values match path to leaf

class Solution(object):
    def isValidSequence(self, root, arr):
        """
        :type root: TreeNode
        :type arr: List[int]
        :rtype: bool
        """
        def dfs(node, idx):
            if not node or idx >= len(arr) or node.val != arr[idx]:
                return False
            if not node.left and not node.right:
                return idx == len(arr) - 1
            return dfs(node.left, idx + 1) or dfs(node.right, idx + 1)

        return dfs(root, 0)
