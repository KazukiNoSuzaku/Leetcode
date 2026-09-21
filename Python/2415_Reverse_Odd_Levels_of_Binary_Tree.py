# Author: Kaustav Ghosh
# Problem: Reverse Odd Levels of Binary Tree
# Approach: Reversing a level only permutes its values, so walk the tree level by level and, on odd levels, write the collected values back in reverse order. The tree is perfect, so every node either has both children or none

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def reverseOddLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        level = [root]
        depth = 0
        while level:
            if depth % 2:
                values = [node.val for node in level]
                for node, value in zip(level, reversed(values)):
                    node.val = value
            nxt = []
            for node in level:
                if node.left:
                    nxt.append(node.left)
                    nxt.append(node.right)
            level = nxt
            depth += 1
        return root
