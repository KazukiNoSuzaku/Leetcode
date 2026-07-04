# Author: Kaustav Ghosh
# Problem: Find Nearest Right Node in Binary Tree (Premium)
# Approach: BFS level by level; when u is dequeued, its nearest right node is simply the next item still in the queue on that level

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
                    return queue[0] if i < size - 1 else None
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return None
