# Author: Kaustav Ghosh
# Problem: Count Nodes Equal to Sum of Descendants
# Approach: Each node's test needs the total of its whole subtree below it, which is exactly what a post-order walk produces, so one traversal that returns each subtree's sum answers every node on the way back up. The tree can hold 10^5 nodes with no balance guarantee, so a recursive walk would overflow Python's stack on a chain; instead I keep an explicit stack of nodes paired with a flag saying whether their children have been processed, push a node back with the flag set after pushing its children, and accumulate subtree sums in a dictionary keyed by node. A node is counted when the sum of its two children's subtree totals equals its own value, which also handles a leaf correctly since both totals are zero. That is O(n) time.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def equalToDescendants(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0

        totals = {}
        matches = 0
        stack = [(root, False)]
        while stack:
            node, done = stack.pop()
            if not done:
                stack.append((node, True))
                if node.left:
                    stack.append((node.left, False))
                if node.right:
                    stack.append((node.right, False))
                continue
            below = 0
            if node.left:
                below += totals.pop(id(node.left))
            if node.right:
                below += totals.pop(id(node.right))
            if below == node.val:
                matches += 1
            totals[id(node)] = below + node.val

        return matches
