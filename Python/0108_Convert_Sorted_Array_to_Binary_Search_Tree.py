# Given an integer array nums where the elements are sorted in ascending order,
# convert it to a height-balanced binary search tree.

# Example 1:
# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]

# Example 2:
# Input: nums = [1,3]
# Output: [3,1]

# Constraints:
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums is sorted in a strictly increasing order.

# Author: Kaustav Ghosh

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root
