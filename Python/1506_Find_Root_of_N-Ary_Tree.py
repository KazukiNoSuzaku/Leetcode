# Author: Kaustav Ghosh
# Problem: Find Root of N-Ary Tree
# Approach: Every node except the root appears exactly once as somebody's child, so adding up all node values and subtracting all child values leaves precisely the root's value. One more pass finds the node holding it, which keeps the whole thing linear time and constant extra space

# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution(object):
    def findRoot(self, tree):
        """
        :type tree: List['Node']
        :rtype: 'Node'
        """
        root_value = 0
        for node in tree:
            root_value += node.val
            for child in node.children:
                root_value -= child.val
        for node in tree:
            if node.val == root_value:
                return node
        return None
