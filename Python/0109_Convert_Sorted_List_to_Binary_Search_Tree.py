# Given the head of a singly linked list where elements are sorted in ascending order,
# convert it to a height-balanced binary search tree.

# Example 1:
# Input: head = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]

# Example 2:
# Input: head = []
# Output: []

# Constraints:
# The number of nodes in the linked list is in the range [0, 2 * 10^4].
# -10^5 <= Node.val <= 10^5

# Author: Kaustav Ghosh

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sortedListToBST(self, head):
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        def helper(lo, hi):
            if lo > hi:
                return None
            mid = (lo + hi) // 2
            root = TreeNode(nums[mid])
            root.left = helper(lo, mid - 1)
            root.right = helper(mid + 1, hi)
            return root
        return helper(0, len(nums) - 1)
