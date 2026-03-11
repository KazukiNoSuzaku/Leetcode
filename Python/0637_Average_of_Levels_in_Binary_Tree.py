# Return the average value of nodes at each level of a binary tree.

# Author: Kaustav Ghosh

from collections import deque

class Solution(object):
    def averageOfLevels(self, root):
        res = []
        q = deque([root])
        while q:
            level_sum, level_count = 0, len(q)
            for _ in range(level_count):
                node = q.popleft()
                level_sum += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(level_sum / float(level_count))
        return res
