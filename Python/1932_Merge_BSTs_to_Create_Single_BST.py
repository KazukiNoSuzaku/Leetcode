# Author: Kaustav Ghosh
# Problem: Merge BSTs to Create Single BST
# Approach: Every operation replaces a leaf by the tree whose root carries that leaf's value, so the final tree's root must be the one root value that appears nowhere else among the nodes; if the number of such candidates is not exactly one the merge is impossible. Starting from that candidate I walk the tree with an explicit stack, carrying the open interval each subtree's values must lie in, and whenever I reach a leaf whose value still has an unused tree I splice that tree's children in, consume it, and revisit the same node so its new children are checked against the same bounds. The bounds check proves the result is a binary search tree and the consumption count proves every input tree was used, so the walk alone decides the answer in O(n) time.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def canMerge(self, trees):
        """
        :type trees: List[TreeNode]
        :rtype: TreeNode
        """
        appearances = {}
        for tree in trees:
            stack = [tree]
            while stack:
                node = stack.pop()
                appearances[node.val] = appearances.get(node.val, 0) + 1
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)

        unused = {}
        for tree in trees:
            unused[tree.val] = tree

        candidates = [tree for tree in trees if appearances[tree.val] == 1]
        if len(candidates) != 1:
            return None

        root = candidates[0]
        del unused[root.val]
        consumed = 1

        stack = [(root, 0, 10 ** 9)]
        while stack:
            node, low, high = stack.pop()
            if not low < node.val < high:
                return None
            if node.left is None and node.right is None:
                other = unused.pop(node.val, None)
                if other is not None:
                    node.left = other.left
                    node.right = other.right
                    consumed += 1
                    stack.append((node, low, high))
                continue
            if node.left:
                stack.append((node.left, low, node.val))
            if node.right:
                stack.append((node.right, node.val, high))

        return root if consumed == len(trees) else None
