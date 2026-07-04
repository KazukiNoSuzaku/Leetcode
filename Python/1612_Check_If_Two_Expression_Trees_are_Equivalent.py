# Author: Kaustav Ghosh
# Problem: Check If Two Expression Trees are Equivalent (Premium)
# Approach: With only '+' operators, a tree just sums its leaf variables; two trees match iff their per-letter leaf counts are identical

from collections import Counter

class Node(object):
    def __init__(self, val=" ", left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def checkEquivalence(self, root1, root2):
        """
        :type root1: Node
        :type root2: Node
        :rtype: bool
        """
        def leaf_counts(node, counter):
            if node is None:
                return
            if node.val != '+':
                counter[node.val] += 1
            leaf_counts(node.left, counter)
            leaf_counts(node.right, counter)

        c1, c2 = Counter(), Counter()
        leaf_counts(root1, c1)
        leaf_counts(root2, c2)
        return c1 == c2
