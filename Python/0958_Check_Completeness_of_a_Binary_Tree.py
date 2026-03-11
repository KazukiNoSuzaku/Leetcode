# Given the root of a binary tree, determine if it is a complete binary tree.

# Author: Kaustav Ghosh

from collections import deque

class Solution(object):
    def isCompleteTree(self, root):
        q = deque([root])
        found_none = False
        while q:
            node = q.popleft()
            if node is None:
                found_none = True
            else:
                if found_none: return False
                q.append(node.left)
                q.append(node.right)
        return True
