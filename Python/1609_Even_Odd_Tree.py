# Author: Kaustav Ghosh
# Problem: Even Odd Tree
# Approach: BFS level by level; even levels must be strictly increasing odd values, odd levels strictly decreasing even values

from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isEvenOddTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = deque([root])
        level = 0
        while queue:
            prev = None
            for _ in range(len(queue)):
                node = queue.popleft()
                v = node.val
                if level % 2 == 0:
                    if v % 2 == 0 or (prev is not None and v <= prev):
                        return False
                else:
                    if v % 2 == 1 or (prev is not None and v >= prev):
                        return False
                prev = v
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return True
