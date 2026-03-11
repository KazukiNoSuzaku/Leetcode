# Given the root of a binary search tree (BST), return all the mode(s) (the most frequently
# occurred element) in it. If the tree has more than one mode, return them in any order.

# Author: Kaustav Ghosh

from collections import Counter

class Solution(object):
    def findMode(self, root):
        count = Counter()
        def inorder(node):
            if not node: return
            inorder(node.left)
            count[node.val] += 1
            inorder(node.right)
        inorder(root)
        max_count = max(count.values())
        return [k for k, v in count.items() if v == max_count]
