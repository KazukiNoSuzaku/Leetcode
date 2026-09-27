# Author: Kaustav Ghosh
# Problem: Minimum Number of Operations to Sort a Binary Tree by Level
# Approach: Levels are independent, so each one is just "sort this array with the fewest swaps of any two elements". Writing the target positions as a permutation, every cycle of length L needs L - 1 swaps, so walk the cycles per level and add that up

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def minimumOperations(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        total = 0
        level = [root]
        while level:
            values = [node.val for node in level]
            order = sorted(range(len(values)), key=lambda i: values[i])
            visited = [False] * len(values)
            for start in range(len(values)):
                if visited[start] or order[start] == start:
                    continue
                length = 0
                i = start
                while not visited[i]:
                    visited[i] = True
                    i = order[i]
                    length += 1
                total += length - 1
            level = [child for node in level for child in (node.left, node.right) if child]
        return total
