# Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

# Example 1:


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]
 

# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz

# Author: Kaustav Ghosh

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        
        # Move first pointer n steps ahead
        for _ in range(n + 1):
            first = first.next
        
        # Move both pointers until first reaches the end
        while first is not None:
            first = first.next
            second = second.next
        
        # Remove the nth node from end
        second.next = second.next.next
        
        return dummy.next

    # Helper function to create a list from an array
    def create_linked_list(arr):
        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for value in arr[1:]:
            current.next = ListNode(value)
            current = current.next
        return head

    # Helper function to convert linked list to array
    def linked_list_to_array(head):
        array = []
        while head:
            array.append(head.val)
            head = head.next
        return array