# Author: Kaustav Ghosh
# Problem: Height of Binary Tree After Subtree Removal Queries
# Approach: The queries are independent, so precompute every answer in two passes. The first collects each subtree's own height; the second walks down carrying the deepest level still reachable once the current subtree is cut away, which is the best of what an ancestor's other branch offers and the ancestor's own depth. Both passes use explicit stacks, since the tree can be a chain of 100000 nodes

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def treeQueries(self, root, queries):
        """
        :type root: Optional[TreeNode]
        :type queries: List[int]
        :rtype: List[int]
        """
        order = []
        stack = [root]
        while stack:
            node = stack.pop()
            order.append(node)
            for child in (node.left, node.right):
                if child:
                    stack.append(child)
        height = {}
        for node in reversed(order):
            height[node] = 1 + max(height.get(node.left, -1), height.get(node.right, -1))

        answer = {}
        stack = [(root, 0, 0)]
        while stack:
            node, depth, without = stack.pop()
            answer[node.val] = without
            left, right = node.left, node.right
            if left:
                through = depth + 1 + height[right] if right else depth
                stack.append((left, depth + 1, max(without, through)))
            if right:
                through = depth + 1 + height[left] if left else depth
                stack.append((right, depth + 1, max(without, through)))
        return [answer[q] for q in queries]
