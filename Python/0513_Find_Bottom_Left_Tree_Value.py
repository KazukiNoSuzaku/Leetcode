# Given the root of a binary tree, return the leftmost value in the last row of the tree.

# Author: Kaustav Ghosh

from collections import deque

class Solution(object):
    def findBottomLeftValue(self, root):
        queue = deque([root])
        res = root.val
        while queue:
            res = queue[0].val
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return res
