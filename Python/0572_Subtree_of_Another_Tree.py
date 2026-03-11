# Given the roots of two binary trees root and subRoot, return true if there is a subtree
# of root with the same structure and node values of subRoot and false otherwise.

# Author: Kaustav Ghosh

class Solution(object):
    def isSubtree(self, root, subRoot):
        def is_same(s, t):
            if not s and not t: return True
            if not s or not t: return False
            return s.val == t.val and is_same(s.left, t.left) and is_same(s.right, t.right)
        if not root: return False
        return is_same(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
