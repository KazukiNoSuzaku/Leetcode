# Author: Kaustav Ghosh
# Problem: Amount of Time for Binary Tree to Be Infected
# Approach: Infection spreads to parents as well as children, so first turn the tree into an undirected graph by walking it and recording parent links. A breadth-first search from the start node then spreads one level per minute, and the number of levels beyond the start is the answer

from collections import defaultdict, deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def amountOfTime(self, root, start):
        """
        :type root: Optional[TreeNode]
        :type start: int
        :rtype: int
        """
        graph = defaultdict(list)
        stack = [root]
        while stack:
            node = stack.pop()
            for child in (node.left, node.right):
                if child:
                    graph[node.val].append(child.val)
                    graph[child.val].append(node.val)
                    stack.append(child)
        seen = {start}
        queue = deque([start])
        minutes = -1
        while queue:
            minutes += 1
            for _ in range(len(queue)):
                for nxt in graph[queue.popleft()]:
                    if nxt not in seen:
                        seen.add(nxt)
                        queue.append(nxt)
        return minutes
