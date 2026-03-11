# Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

# Author: Kaustav Ghosh

class Solution(object):
    def preorder(self, root):
        if not root: return []
        res = [root.val]
        for child in root.children:
            res.extend(self.preorder(child))
        return res
