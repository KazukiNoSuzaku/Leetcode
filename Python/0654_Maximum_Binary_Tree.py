# Build the maximum binary tree from an array: root is max, left/right are sub-trees.

# Author: Kaustav Ghosh

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        if not nums: return None
        idx = nums.index(max(nums))
        node = TreeNode(nums[idx])
        node.left = self.constructMaximumBinaryTree(nums[:idx])
        node.right = self.constructMaximumBinaryTree(nums[idx+1:])
        return node
