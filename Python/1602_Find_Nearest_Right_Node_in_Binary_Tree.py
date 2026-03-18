# Author: Kaustav Ghosh
# Problem: 1602 - Find Nearest Right Node in Binary Tree (Premium)
# Approach: BFS, find node then return next in same level

from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def findNearestRightNode(self, root, u):
        """
        :type root: TreeNode
        :type u: TreeNode
        :rtype: TreeNode
        """
        queue = deque([root])
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if node is u:
                    return queue[0] if queue else None
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return None
