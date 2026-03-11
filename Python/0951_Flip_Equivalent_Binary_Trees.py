# Two binary trees are flip equivalent if one can be made identical to the other
# by swapping left and right children any number of times.
# Return true if they are flip equivalent.

# Author: Kaustav Ghosh

class Solution(object):
    def flipEquiv(self, root1, root2):
        if not root1 and not root2: return True
        if not root1 or not root2: return False
        if root1.val != root2.val: return False
        no_flip = self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
        flip = self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)
        return no_flip or flip
