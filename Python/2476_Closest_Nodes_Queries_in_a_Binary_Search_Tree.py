# Author: Kaustav Ghosh
# Problem: Closest Nodes Queries in a Binary Search Tree
# Approach: An in-order walk of a search tree yields its values sorted, so collect them once with an explicit stack. Each query is then two binary searches: the last value not above it and the first value not below it, with -1 when either side runs out

from bisect import bisect_left, bisect_right


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def closestNodes(self, root, queries):
        """
        :type root: Optional[TreeNode]
        :type queries: List[int]
        :rtype: List[List[int]]
        """
        values = []
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            values.append(node.val)
            node = node.right
        answer = []
        for query in queries:
            below = bisect_right(values, query) - 1
            above = bisect_left(values, query)
            answer.append([values[below] if below >= 0 else -1,
                           values[above] if above < len(values) else -1])
        return answer
