# Author: Kaustav Ghosh
# Problem: Even Odd Tree
# Approach: Every condition is about one level at a time, so a level-order walk is the natural shape: at each level I only need the previous value on that level to check the strict ordering, and the level's index to know whether the values must be odd and increasing or even and decreasing. Both parity and ordering are checked as each node comes off the queue, so a violation returns immediately rather than after building the level, and the traversal is iterative so depth is never a problem.

from collections import deque


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def isEvenOddTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        queue = deque([root])
        even_level = True
        while queue:
            previous = None
            for _ in range(len(queue)):
                node = queue.popleft()
                if even_level:
                    if node.val % 2 == 0 or (previous is not None and node.val <= previous):
                        return False
                else:
                    if node.val % 2 == 1 or (previous is not None and node.val >= previous):
                        return False
                previous = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            even_level = not even_level
        return True
