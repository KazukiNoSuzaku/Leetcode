# Author: Kaustav Ghosh
# Problem: Move Sub-Tree of N-Ary Tree (Premium)
# Approach: Find parent of p, detach p, reattach as last child of q; handle case where q is already parent of p

class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution(object):
    def moveSubTree(self, root, p, q):
        """
        :type root: Node
        :type p: Node
        :type q: Node
        :rtype: Node
        """
        parent_p = self._find_parent(root, p)

        if parent_p == q:
            if q.children[-1] == p:
                return root
            q.children.remove(p)
            q.children.append(p)
            return root

        if parent_p:
            parent_p.children.remove(p)

        q.children.append(p)
        return root

    def _find_parent(self, node, target):
        for child in node.children:
            if child == target:
                return node
            result = self._find_parent(child, target)
            if result:
                return result
        return None
