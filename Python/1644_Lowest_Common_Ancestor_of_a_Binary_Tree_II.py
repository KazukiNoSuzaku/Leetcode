# Author: Kaustav Ghosh
# Problem: Lowest Common Ancestor of a Binary Tree II
# Approach: The usual lowest-common-ancestor argument breaks here because a missing node would make the other node look like the answer, so instead of returning a node up the recursion I return only whether a subtree contains a target, and record an answer at the first node that accounts for two of them, counting the node itself as one. That way an answer is produced only when both nodes genuinely exist, which also settles the follow-up of avoiding a separate existence check. The walk is an explicit post-order stack rather than recursion, since ten thousand nodes in a chain would recurse past Python's limit; post-order visits descendants first, so the first qualifying node encountered is the lowest one.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        holds_target = {}
        answer = None
        stack = [(root, False)]
        while stack:
            node, expanded = stack.pop()
            if node is None:
                continue
            if not expanded:
                stack.append((node, True))
                stack.append((node.left, False))
                stack.append((node.right, False))
                continue
            found = holds_target.get(node.left, False) + holds_target.get(node.right, False)
            if node is p or node is q:
                found += 1
            if found >= 2 and answer is None:
                answer = node
            holds_target[node] = found > 0
        return answer
