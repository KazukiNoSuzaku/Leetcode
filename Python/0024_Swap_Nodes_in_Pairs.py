# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 

# Example 1:

# Input: head = [1,2,3,4]

# Output: [2,1,4,3]

# Explanation:



# Example 2:

# Input: head = []

# Output: []

# Example 3:

# Input: head = [1]

# Output: [1]

# Example 4:

# Input: head = [1,2,3]

# Output: [2,1,3]

 

# Constraints:

# The number of nodes in the list is in the range [0, 100].
# 0 <= Node.val <= 100

# Author: Kaustav Ghosh

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
    # Create a dummy node to simplify the code
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while prev.next and prev.next.next:
            # Nodes to be swapped
            first = prev.next
            second = prev.next.next
            
            # Swapping
            prev.next = second
            first.next = second.next
            second.next = first
            
            # Move prev to the node before the next pair
            prev = first
        
        return dummy.next

    # Helper function to convert a list to a linked list
    def list_to_linkedlist(lst):
        dummy = ListNode(0)
        current = dummy
        for val in lst:
            current.next = ListNode(val)
            current = current.next
        return dummy.next

    # Helper function to convert a linked list to a list
    def linkedlist_to_list(head):
        lst = []
        current = head
        while current:
            lst.append(current.val)
            current = current.next
        return lst