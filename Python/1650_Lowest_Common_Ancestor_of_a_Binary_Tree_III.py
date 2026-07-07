# Author: Kaustav Ghosh
# Problem: Lowest Common Ancestor of a Binary Tree III (Premium)
# Approach: With parent pointers this is like finding the intersection of two linked lists; walk up from both, switching to the other start on reaching the root, and they meet at the LCA

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution(object):
    def lowestCommonAncestor(self, p, q):
        """
        :type p: Node
        :type q: Node
        :rtype: Node
        """
        a, b = p, q
        while a is not b:
            a = a.parent if a else q
            b = b.parent if b else p
        return a
