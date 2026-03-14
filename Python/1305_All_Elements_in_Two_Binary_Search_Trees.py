# Return a sorted list containing all elements from two binary search trees.

# Author: Kaustav Ghosh

class Solution(object):
    def getAllElements(self, root1, root2):
        def inorder(node, res):
            if not node: return
            inorder(node.left, res)
            res.append(node.val)
            inorder(node.right, res)
        a, b = [], []
        inorder(root1, a)
        inorder(root2, b)
        res = []
        i = j = 0
        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                res.append(a[i]); i += 1
            else:
                res.append(b[j]); j += 1
        return res + a[i:] + b[j:]
