# Author: Kaustav Ghosh
# Problem: Find Root of N-Ary Tree (Premium)
# Approach: Root is the only node never appearing as a child

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
        children = set()
        for node in tree:
            for child in node.children:
                children.add(child.val)
        for node in tree:
            if node.val not in children:
                return node
