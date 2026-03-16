# Author: Kaustav Ghosh
# Problem: Find a Corresponding Node of a Binary Tree in a Clone of That Tree
# Approach: DFS simultaneously on both trees

class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        if not original:
            return None
        if original is target:
            return cloned
        return (self.getTargetCopy(original.left, cloned.left, target) or
                self.getTargetCopy(original.right, cloned.right, target))
