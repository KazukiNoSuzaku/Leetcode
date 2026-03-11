# Given the root of a binary tree, return an array of the largest value in each row.

# Author: Kaustav Ghosh

from collections import deque

class Solution(object):
    def largestValues(self, root):
        if not root: return []
        res, queue = [], deque([root])
        while queue:
            res.append(max(node.val for node in queue))
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return res
