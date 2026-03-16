# Author: Kaustav Ghosh
# Problem: Validate Binary Tree Nodes
# Approach: Find root (node with no parent), BFS to check all reachable and no cycles

from collections import deque

class Solution(object):
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        """
        :type n: int
        :type leftChild: List[int]
        :type rightChild: List[int]
        :rtype: bool
        """
        has_parent = set()
        for i in range(n):
            if leftChild[i] != -1:
                has_parent.add(leftChild[i])
            if rightChild[i] != -1:
                has_parent.add(rightChild[i])

        roots = [i for i in range(n) if i not in has_parent]
        if len(roots) != 1:
            return False

        root = roots[0]
        visited = set()
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node in visited:
                return False
            visited.add(node)
            if leftChild[node] != -1:
                queue.append(leftChild[node])
            if rightChild[node] != -1:
                queue.append(rightChild[node])

        return len(visited) == n
