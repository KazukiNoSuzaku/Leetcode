# Author: Kaustav Ghosh
# Problem: Find Nearest Right Node in Binary Tree
# Approach: A level-order walk already visits a level strictly left to right, so the node immediately right of u is simply whatever comes next in the queue, provided u was not the last node of its level. Tracking how many nodes remain in the current level distinguishes those two cases without a second pass or any per-level bookkeeping, and because the traversal is a loop rather than recursion a tree that is one long chain of a hundred thousand nodes is no problem.

from collections import deque


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def findNearestRightNode(self, root, u):
        """
        :type root: TreeNode
        :type u: TreeNode
        :rtype: TreeNode
        """
        queue = deque([root])
        while queue:
            for remaining in range(len(queue) - 1, -1, -1):
                node = queue.popleft()
                if node is u:
                    return queue[0] if remaining else None
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return None
