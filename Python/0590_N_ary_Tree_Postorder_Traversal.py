# Given the root of an n-ary tree, return the postorder traversal of its nodes' values.

# Author: Kaustav Ghosh

class Solution(object):
    def postorder(self, root):
        if not root: return []
        res = []
        for child in root.children:
            res.extend(self.postorder(child))
        res.append(root.val)
        return res
