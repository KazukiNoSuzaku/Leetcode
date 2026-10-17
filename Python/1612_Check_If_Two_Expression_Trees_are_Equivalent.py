# Author: Kaustav Ghosh
# Problem: Check If Two Expression Trees are Equivalent
# Approach: With addition as the only operator the tree's shape carries no meaning at all, since addition is both commutative and associative, so an expression is fully described by how many times each variable appears in it. I therefore tally the leaves of the first tree upward and the leaves of the second downward in the same counter, and equivalence is exactly every tally landing on zero. The walk uses an explicit stack rather than recursion, because five thousand nodes arranged as a chain would recurse deeper than Python allows. Were subtraction allowed as well, the same tally would still work provided a leaf's sign were flipped once for every right-hand side of a subtraction above it.

from collections import Counter


# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def checkEquivalence(self, root1, root2):
        """
        :type root1: Node
        :type root2: Node
        :rtype: bool
        """
        appearances = Counter()
        for root, sign in ((root1, 1), (root2, -1)):
            stack = [root]
            while stack:
                node = stack.pop()
                if node is None:
                    continue
                if node.val != '+':
                    appearances[node.val] += sign
                stack.append(node.left)
                stack.append(node.right)
        return all(count == 0 for count in appearances.values())
