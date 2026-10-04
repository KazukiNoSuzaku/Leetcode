# Author: Kaustav Ghosh
# Problem: Move Sub-Tree of N-Ary Tree
# Approach: Record every node's parent, then decide which of the three cases applies. If p already sits under q there is nothing to do. If q lies inside p's subtree, detaching p would split the tree, so first lift q out of its parent and put it where p was (or make it the new root when p was the root), then hang p beneath it. Otherwise p simply leaves its parent and becomes q's last child

# Definition for a Node.
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
        if p in q.children:
            return root

        parent = {}
        stack = [root]
        while stack:
            node = stack.pop()
            for child in node.children:
                parent[child] = node
                stack.append(child)

        inside = False
        walker = q
        while walker is not None:
            if walker is p:
                inside = True
                break
            walker = parent.get(walker)

        if inside:
            parent[q].children.remove(q)
            if p is root:
                q.children.append(p)
                return q
            above = parent[p]
            above.children[above.children.index(p)] = q
            q.children.append(p)
            return root

        parent[p].children.remove(p)
        q.children.append(p)
        return root
