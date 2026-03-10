# Given a non-negative integer represented as a linked list of digits, plus one to the integer.
# The digits are stored such that the most significant digit is at the head of the list.

# Example 1:
# Input: head = [1,2,3]
# Output: [1,2,4]

# Example 2:
# Input: head = [9,9,9]
# Output: [1,0,0,0]

# Constraints:
# The number of nodes in the list is in the range [1, 100].
# 0 <= Node.val <= 9
# The number represented by the linked list does not contain leading zeros except for the number 0 itself.

# Author: Kaustav Ghosh

class Solution(object):
    def plusOne(self, head):
        # Find rightmost non-9 node
        dummy = ListNode(0)
        dummy.next = head
        not_nine = dummy
        cur = head
        while cur:
            if cur.val != 9:
                not_nine = cur
            cur = cur.next
        not_nine.val += 1
        cur = not_nine.next
        while cur:
            cur.val = 0
            cur = cur.next
        return dummy if dummy.val == 1 else dummy.next
