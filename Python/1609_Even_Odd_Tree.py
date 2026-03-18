# Author: Kaustav Ghosh
# Problem: 1609 - Even Odd Tree
# Approach: BFS checking even levels have odd strictly increasing, odd levels have even strictly decreasing

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
            size = len(queue)
            prev = None
            for _ in range(size):
                node = queue.popleft()
                if level % 2 == 0:
                    # Even level: values must be odd and strictly increasing
                    if node.val % 2 == 0:
                        return False
                    if prev is not None and node.val <= prev:
                        return False
                else:
                    # Odd level: values must be even and strictly decreasing
                    if node.val % 2 == 1:
                        return False
                    if prev is not None and node.val >= prev:
                        return False
                prev = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1

        return True
