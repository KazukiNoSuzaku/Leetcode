# Sum of values in BST in range [low, high].

# Author: Kaustav Ghosh

class Solution(object):
    def rangeSumBST(self, root, low, high):
        if not root: return 0
        total = root.val if low <= root.val <= high else 0
        if root.val > low: total += self.rangeSumBST(root.left, low, high)
        if root.val < high: total += self.rangeSumBST(root.right, low, high)
        return total
