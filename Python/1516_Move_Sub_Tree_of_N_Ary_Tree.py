# Author: Kaustav Ghosh
# Problem: 1516 - Move Sub-Tree of N-Ary Tree (Premium)
# Approach: Reparent subtree - detach p from its parent and attach under q

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
        def find_parent(node, target, parent):
            if node is target:
                return parent
            for child in node.children:
                result = find_parent(child, target, node)
                if result:
                    return result
            return None

        def is_ancestor(ancestor, node):
            if ancestor is node:
                return True
            for child in ancestor.children:
                if is_ancestor(child, node):
                    return True
            return False

        # If q is in subtree of p, no move needed
        if is_ancestor(p, q):
            return root

        p_parent = find_parent(root, p, None)
        q_parent = find_parent(root, q, None)

        # Remove p from its parent
        if p_parent:
            p_parent.children = [c for c in p_parent.children if c is not p]

        # Add p as child of q
        q.children.append(p)

        # If p was root, return p_parent (but p_parent is None in this case)
        if p_parent is None:
            # p was root, q becomes new root effectively
            # but q is somewhere in the tree rooted at p
            # We need to find the new root
            return q if q_parent is None else root

        return root
