# Author: Kaustav Ghosh
# Problem: Count Nodes Equal to Sum of Descendants
# Approach: Post-order DFS returning each subtree's total sum. At a node the descendant sum is subtree_sum minus its own value; count nodes whose value equals that descendant sum

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def equalToDescendants(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.count = 0

        def subtree_sum(node):
            if not node:
                return 0
            descendants = subtree_sum(node.left) + subtree_sum(node.right)
            if node.val == descendants:
                self.count += 1
            return descendants + node.val

        subtree_sum(root)
        return self.count
